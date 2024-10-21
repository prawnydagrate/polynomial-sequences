from collections import namedtuple

Component: type[tuple[int, int]] = namedtuple("Component", ["coefficient", "var"])
Term: type[tuple[list[Component]]] = namedtuple("Term", ["components"])

def comp_sub(lc: Component, rc: Component) -> Component | None:
    assert lc.var == rc.var
    return Component(diff, lc.var) if (diff := lc.coefficient-rc.coefficient) != 0 else None

def term_sub(lt: Term, rt: Term) -> Term:
    return Term([diff for (lc, rc) in zip(lt.components, rt.components) if (diff := comp_sub(lc, rc))])
