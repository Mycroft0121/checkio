def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    if first == second or first not in word or second not in word:
        return False
    return word.index(first)+1==word.index(second)