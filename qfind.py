import sys

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1

def find_q(degree: int):
    needed_terms = degree + 1

    def vsub(lt: list[int], rt: list[int]) -> list[int]:
        return list(diff for (lc, rc) in zip(lt, rt) if (diff := lc - rc) != 0)

    # generate terms
    terms = []
    for n in range(1, needed_terms + 1):
        term = []
        for power in range(degree, -1, -1):
            term.append(n**power)
        terms.append(term)

    # find differences
    curr = terms
    level = 0
    while len(curr) != 1:
        level += 1
        newcurr = []
        # windows of size 2 through current list
        for i in range(0, len(curr)-2+1):
            rt, lt = curr[i:i+2]
            newcurr.append(vsub(lt, rt))
        curr = newcurr

    q = curr[0][0]
    return q

d = start
while True:
    print(f"q_{d} = {find_q(d)}")
    d += 1
