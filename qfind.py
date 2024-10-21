from table import make_table, to_html
import sys, math, pprint

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
stop = int(sys.argv[2]) if len(sys.argv) > 2 else math.inf

def find_q(degree: int):
    table = make_table(degree)
    with open(f"table_{degree}.html", "w") as f:
        f.write(to_html(table))
    return table[-1][0].components[0].coefficient

d = start
while d <= stop:
    print(f"q_{d} = {find_q(d)}")
    d += 1
