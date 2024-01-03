import cv2

im = cv2.imread("xmem_masks_handtuned.png")

colors = set()

for row in im:
    for pixel in row:
        colors.add(tuple([int(p) for p in pixel]))
colors.remove((0, 0, 0))
assert len(colors) == 22

names = (
    "Martin, Jingxuan, Robin, Yuhao, Mark, Mislav, Batuhan, Marc, Timon, Anouk,"
    " SamuelSimko, Hanna, Benjamin, Jasper, Max, Nikola, Luca, Momchil, Slobodan,"
    " Tobias, MarkVero, Fiorella"
)
names = [n.strip() for n in names.split(",")]

cons = []
for i, c in enumerate(colors):
    mask = cv2.inRange(im, c, c)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    con = contours[0]
    cons.append(con)
cons = list(sorted(cons, key=lambda c: c[:, :, 0].min()))


polys = []
for i, con in enumerate(cons):
    # cv2.drawContours(im, [con], 0, (0, 255, 0), 3)
    # cv2.imwrite(f"polys{i}.png", im)
    cc = ",".join([",".join([str(n) for n in p[0]]) for p in con.tolist()])
    print(f"{names[i]};{cc}", end="")
    if i < len(cons) - 1:
        print("")
