def cut_sentence(line, length):

    if len(line)<=length:
        return line

    line = line.split()
    cur_l = 0
    for i in range(len(line)):
        cur = i

        #perfect
        if cur_l + len(line[i])==length:
            return ' '.join(line[:i+1])+'...'

        # discard current letter
        if cur_l + len(line[i])>length:
            return ' '.join(line[:i])+'...'
        else:
            cur_l+=len(line[i])+1



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    print('Done! Do you like it? Go Check it!')
