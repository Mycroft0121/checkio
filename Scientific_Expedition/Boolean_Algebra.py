OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    x, y =  bool(x), bool(y)
    if operation =="conjunction":
        return x and y
    if operation =="disjunction":
        return x or y
    if operation =="implication":
        return (not x) or y
    if operation =="exclusive":
        return x != y
    if operation =="equivalence":
        return x==y