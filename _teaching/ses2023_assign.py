import gurobipy as gp
from gurobipy import GRB


choices = {}
names = []

for line in open('SES2023-Fall.tsv', 'r').readlines():
    if line.startswith('#'):
        continue
    tokens = line.split('\t')
    choices[tokens[1]] = [t.strip() for t in tokens[3:] if t.strip() != '']
    names.append( ( tokens[1], tokens[2].strip() ) )
papers = list(set([choices[email][i] for email in choices.keys() for i in range(len(choices[email]))]))
paper2id = {}
for i in range(len(papers)):
    paper2id[papers[i]] = i
num_real_papers = len(papers)

for i in range(len(papers), len(names)):
    new_id = f'Fake paper {i}'
    paper2id[new_id] = i
    papers += [ new_id ]

with gp.Env() as env:
    env.setParam('OutputFlag', 0)
    env.setParam('LogToConsole', 0)
    env.start()
    m = gp.Model(env=env)
    assignment_var = m.addMVar((len(names),len(papers)), vtype=GRB.BINARY)
    obj = gp.LinExpr()
    for person_id, name in enumerate(names):
        name, _ = name
        paper_ch = choices[name]
        ch_num = len(paper_ch)
        constr = gp.LinExpr()
        for i in range( len(papers) ):
            constr += assignment_var[person_id,i]
        for i in range(num_real_papers, len(papers)):
            paper_ch += [papers[i]]
        paper_ch = [ paper2id[i] for i in paper_ch ]
        for i in range(ch_num):
            obj += assignment_var[person_id,paper_ch[i]]*(i+1)
        for i in range(ch_num, len(paper_ch)):
            obj += assignment_var[person_id,paper_ch[i]]*(50 +  len(names) - person_id )
        for i in range( len(papers) ):
            if i in paper_ch:
                continue
            obj += assignment_var[person_id,i]*(50 + len(names) - person_id )
        m.addConstr(constr == 1)
    for paper in papers:
        pid = paper2id[ paper ]
        constr = gp.LinExpr()
        for i in range(len(names)):
            constr += assignment_var[i,pid]
        m.addConstr(constr <= 1)
    obj =  m.setObjective(obj, GRB.MINIMIZE)

    m.optimize()

    for person_id, name in enumerate(names):
        paper_id = None
        for i in range( len(papers) ):
            if assignment_var[person_id, i].X.item() == 1:
                paper_id = i
                break
        assert not paper_id is None
        paper_name = [ k for k in paper2id.keys() if paper2id[k] == paper_id ][0]
        if paper_id >= num_real_papers:
            score = -1
        else:
            score = -2 
            for i, c in enumerate( choices[name[0]] ):
                if paper_name == c:
                    score = i + 1 
                    break
        print('{}\t{}\t{}\t{}'.format(name[1], name[0], paper_name, score))
