from collections import Counter
s_idx = [(1,4,2,5),(0,4,3,5),(0,1,3,2)]

# given a cube, return all possible side color combinations starting with the 'min' color
def cube_sides(cube):
    sides = []
    for s in s_idx:
        side = cube[s[0]]+cube[s[1]]+cube[s[2]]+cube[s[3]]
        idx = side.index(min(side))
        side = side[idx:]+side[:idx]
        sides.append(side)
        # flip the cube
        flip = side[::-1][-1]+ side[::-1][:-1]
        sides.append(flip)
    return set(sides)

def tower(cubes):
    all_sides = Counter()
    for c in cubes:
        all_sides.update(cube_sides(c))

    print(all_sides)
    return all_sides.most_common()[0][1]





if __name__ == '__main__':
    # print("Example:")
    # print(tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']))
    assert tower(["GYCABW","ARCGYW","RGBCAW","RGBCAY","OCYWBA","WCAVBR","ACYVWR","OCYWBA","WCAVBR","ACYVWR"]) ==2
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']) == 3
    assert tower(['ABCGYW', 'CAYRGO', 'OCYWBA', 'ACYVBR', 'GYVABW']) == 1
    assert tower(['GYCABW', 'GYCABW', 'GYCABW', 'GYCABW', 'GYCABW']) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
