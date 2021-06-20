def to_camel_case(name: str) -> str:
    #replace this for solution
    return ''.join([w.title() for w in name.split("_")])