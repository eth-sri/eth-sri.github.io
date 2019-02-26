from z3 import *

choices = {}
names = {}

for line in open('bsec2019_choices.txt', 'r').readlines():
	tokens = line.split('\t')
	choices[tokens[1]] = [tokens[3], tokens[4], tokens[5], tokens[6], tokens[7]]
	names[tokens[1]] = tokens[2]

papers = list(set([choices[email][i] for i in range(5) for email in choices.keys()]))
paper2id = {}
for i in range(len(papers)):
	paper2id[papers[i]] = i

assignments = {}
scores = {}
opt = Optimize()
sum_of_scores = None
for email in choices.keys():
	assignment = Int(email + '_assignment')
	score = Int(email + '_score')
	assignments[email] = assignment
	scores[email] = score
	opt.add(z3.If(assignment == paper2id[choices[email][0]], score == 1, z3.If(assignment == paper2id[choices[email][1]], score == 2, z3.If(assignment == paper2id[choices[email][2]], score == 3, z3.If(assignment == paper2id[choices[email][3]], score == 4, z3.If(assignment == paper2id[choices[email][4]], score == 5, score == 999))))))
	if sum_of_scores is None:
		sum_of_scores = score
	else:
		sum_of_scores += score
	opt.add(score < 5)

opt.add(z3.Distinct([assignments[x] for x in assignments.keys()]))

opt.minimize(sum_of_scores)
opt.check()

for email in assignments.keys():
	assignment = opt.model()[assignments[email]].as_long()
	paper = papers[assignment]
	score = opt.model()[scores[email]]
	print('{}\t{}\t{}\t{}'.format(email, names[email], paper, score))
