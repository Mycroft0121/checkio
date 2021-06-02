def hypercube(grid):

    l,w = len(grid), len(grid[0])


    direction = [(-1,0),(1,0),(0,1),(0,-1)]

    grid =[[y.lower() for y in x] for x in grid]

    valid= [(y,x) for y in range(l) for x in range(w)]

    start = []
    for i in range(l):
        row = grid[i]
        try:
            if row.index('h')>=0:
                start.append((i,row.index('h')))
        except ValueError:
            pass


    if not len(start):
        return False

    found = []


    target = 'hypercube'

    def path_finder(y,x,valid, target):

        if len(target)==0:

            found.append(True)
            return

        if (y,x) not in valid:
            return

        valid.remove((y,x))
        if grid[y][x] == target[0]:
            for (dy,dx) in direction:
                ny,nx =y+dy, x+dx
                path_finder(ny,nx,valid[:],target[1:])

        return

    for (sy,sx) in start:

        path_finder(sy,sx,valid,target)


    return bool(sum(found))

if __name__ == '__main__':
    print("Example:")
    # print(hypercube([
    #     ['g', 'f', 'H', 'Y', 'v'],
    #     ['z', 'e', 'a', 'P', 'u'],
    #     ['s', 'B', 'T', 'e', 'y'],
    #     ['k', 'u', 'c', 'R', 't'],
    #     ['l', 'O', 'k', 'p', 'r']]))
    #
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert hypercube([
    #     ['g', 'f', 'H', 'Y', 'v'],
    #     ['z', 'e', 'a', 'P', 'u'],
    #     ['s', 'B', 'T', 'e', 'y'],
    #     ['k', 'u', 'c', 'R', 't'],
    #     ['l', 'O', 'k', 'p', 'r']]) == True
    # assert hypercube([
    #     ['H', 'a', 't', 's', 'E'],
    #     ['a', 'Y', 'p', 'u', 'B'],
    #     ['a', 'a', 'P', 'y', 'U'],
    #     ['x', 'x', 'x', 'E', 'C'],
    #     ['z', 'z', 'z', 'z', 'R']]) == False

    assert hypercube([
        ["H","a","t","s","E"],
        ["h","Y","p","e","B"],
        ["a","a","P","r","U"],
        ["x","x","U","c","C"],
        ["z","E","B","z","R"]]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
