def keys_and_locks(lock, some_key):
    # replace this for solution
    lock_list = [list(x) for x in lock.split("\n")]
    key_list = [list(x) for x in some_key.split("\n")]
    for i in range(4):
        while key_list and '#' not in key_list[0]:
            key_list = key_list[1:]
        while lock_list and '#' not in lock_list[0]:
            lock_list = lock_list[1:]
        if key_list:
            key_list = list(zip(*key_list[::-1]))
        if lock_list:
            lock_list = list(zip(*lock_list[::-1]))

    if key_list and lock_list:
        # print(lock_list,key_list,lock_list==key_list)
        for i in range(4):
            key_list = list(zip(*key_list[::-1]))
            # print(lock_list,key_list,lock_list==key_list)
            if lock_list == key_list:
                return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
                         '''
                         00000
                         000##
                         #####
                         ##000
                         00000'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
                          '''
                          00000
                          000##
                          #####
                          ##000
                          00000''') == True

    assert keys_and_locks('''
###0
00#0''',
                          '''
                          00000
                          00000
                          #0000
                          ###00
                          0#000
                          0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
                          '''
                          ##000
                          #0000
                          00000
                          00000
                          00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
                          '''
                          ##00
                          ##00''') == False

    print("Coding complete? Click 'Check' to earn cool rewards!")
