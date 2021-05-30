import numpy as np
def buttons(ceiling):

    result = []
    direction = [(-1,0),(1,0),(0,1),(0,-1)]

    ceiling =[[int(y) for y in x] for x in ceiling.split("\n")][1:]

    l,w = len(ceiling), len(ceiling[0])

    checked = np.zeros((l,w))

    for i in range(l):
        for j in range(w):
            if (not checked[i][j]) :
                # now is checked
                checked[i][j]=1
                if ceiling[i][j]:
                    val =ceiling[i][j]
                    cc = [(i,j)]
                    while cc:
                        (ii,jj) = cc.pop()
                        # print(ii,jj)
                        for (di, dj) in direction:

                            cur_i, cur_j = ii+di,jj+dj
                            if (-1<cur_i<l) and (-1<cur_j<w):
                                if not checked[cur_i][cur_j]:
                                    checked[cur_i][cur_j] =1
                                    cur = ceiling[cur_i][cur_j]
                                    if cur:
                                        val+=cur
                                        cc.append((cur_i,cur_j))
                    result.append(val)


    return sorted(result)[::-1]

if __name__ == '__main__':
    print("Example:")
    print(buttons('''
001203
023001
100220'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert buttons('''
001203
023001
100220''') == [8, 4, 4, 1]

    assert buttons('''
000000
000055
000055''') == [20]

    assert buttons('''
908070
060504
302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
