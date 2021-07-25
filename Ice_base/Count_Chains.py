from typing import List, Tuple
import math
from itertools import combinations

def count_chains(circles: List[Tuple[int, int, int]]) -> int:

    n_cir = len(circles)
    groups = list(range(n_cir))
    comb = list(combinations(circles,2))
    idx_comb = list(combinations(list(range(n_cir)),2))


    def connected(a,b):
        return (a[2]+b[2])>math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)>abs(a[2]-b[2])


    def root(i):
        while groups[i] !=i:
            i = groups[i]
        return i

    def union(c1,c2):
        p1 = root(c1)
        p2 = root(c2)
        groups[p1] =p2


    edges = [idx_comb[i] for i in range(len(comb)) if connected(comb[i][0],comb[i][1])]
    for e in edges:
        union(e[0],e[1])


    roots = [root(i) for i in range(n_cir)]
    return len(set(roots))





if __name__ == '__main__':
    print("Example:")
    #print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")

