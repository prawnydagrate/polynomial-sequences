from core import *
import math

def make_table(degree: int) -> list[list[Term]]:
    needed_terms = degree + 2
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

def to_html(table: list[list[Term]]) -> str:
    ncols = math.lcm(*(len(row) for row in table))
    css = ".table { width: fit-content; display: grid; grid-template-columns: min-content repeat(%s, 1fr); gap: 1px; background-color: black; border: 1px solid black; } " % ncols \
        + '.td, .th { padding: 4px; text-align: center; background-color: white; font-family: "Courier New", Courier, monospace; } ' \
        + ".th { font-weight: bold } "
    html = '<!DOCTYPE html><html><head></head><body><div class="table">'
    for (i, row) in enumerate(table):
        rowlen = len(row)
        colspan = ncols//rowlen
        style = f"grid-column: span {colspan}"
        if i == 0:
            html += '<div class="th td">n</div>'
            for n in range(rowlen):
                html += f'<div class="td" style="{style}">{n+1}</div>'
        html += f'<div class="th td">{"u" if i == 0 else f"d<sub>{i}</sub>"}</div>'
        for term in row:
            html += f'<div class="td" style="{style}">'
            html += " + ".join(f"{comp.coefficient if comp.coefficient != 1 else ""}a<sub>{comp.var}</sub>" for comp in term.components if comp.coefficient != 0)
            html += "</div>"
    html += f"</div><style>{css}</style></body></html>"
    return html
