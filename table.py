def vsub(lt: list[int], rt: list[int]) -> list[int]:
    return list(diff for (lc, rc) in zip(lt, rt) if (diff := lc - rc) != 0)

def make_table(degree: int) -> list[list[list[int]]]:
    needed_terms = degree + 1
    table = [[[n**power for power in range(degree, -1, -1)] for n in range(1, needed_terms + 1)]]

    # find differences
    while len((curr_row := table[-1])[0]) != 1:
        new_row = []
        # windows of size 2 through current list
        for i in range(0, len(curr_row)-2+1):
            rt, lt = curr_row[i:i+2]
            new_row.append(vsub(lt, rt))
        table.append(new_row)

    return table
