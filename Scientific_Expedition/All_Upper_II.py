def is_all_upper(text: str) -> bool:
    # your code here
    text = text.replace(" ","")
    text = "".join([c for c in text if c.isalpha()])
    return all(c.isupper() for c in text) and len(text)>0