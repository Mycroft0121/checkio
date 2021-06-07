def words_order(text: str, words: list) -> bool:
    # your code here
    if len(words)!=len(set(words)):
        return False
    text = [x for x in text.split()]
    text = [x for x in text if x in words]
    return text==words