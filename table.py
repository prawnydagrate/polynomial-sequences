from core import *

def make_table(degree: int) -> list[list[Term]]:
    needed_terms = degree + 1
    table = [[Term([Component(n**power, power) for power in range(degree, -1, -1)]) for n in range(1, needed_terms + 1)]]

    # find differences
    while len((curr_row := table[-1])[0].components) != 1:
        new_row = []
        # windows of size 2 through current list
        for i in range(0, len(curr_row)-2+1):
            rt, lt = curr_row[i:i+2]
            new_row.append(term_sub(lt, rt))
        table.append(new_row)

    return table
