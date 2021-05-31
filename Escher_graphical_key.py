

def g_key(grid, path):
    l,w = len(grid),len(grid[0])

    direction = [(0, -1),(0, 1),(-1, -1),(-1, 1),(-1, 0),(1, -1),(1, 0),(1, 1)]
    valid= [(y,x) for y in range(l) for x in range(w)]

    result = []

    def find_path(y,x, not_visited, steps, s):
        # no valid steps
        if not steps:
            return

        x_left = w-x
        y_left = l-y
        # have visited or not enough steps
        if (not (y,x) in not_visited) or y_left>steps or x_left>steps:
            return


        #if reached the final
        if x==w-1 and y==l-1:
            s+=grid[l-1][w-1]
            result.append(s)
            return



        not_visited.remove((y,x))
        for (dy,dx) in direction:
            find_path(y+dy,x+dx,not_visited[:],steps-1,s+grid[y][x])

        return
    if l*w ==path:
        return sum([sum(x) for x in grid])
    find_path(0,0,valid,path,0)

    return max(result)




if __name__ == '__main__':
    print("Example:")
    print(g_key([[1, 6, 7, 2, 4],
                 [0, 4, 9, 5, 3],
                 [7, 2, 5, 1, 4],
                 [3, 3, 2, 2, 9],
                 [2, 6, 1, 4, 0]], 9))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert g_key([[1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9) == 46

    assert g_key([[2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]], 6) == 27

    assert g_key([[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]], 25) == 75

    assert g_key([[1, 6],
                  [5, 1]], 2) == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")
