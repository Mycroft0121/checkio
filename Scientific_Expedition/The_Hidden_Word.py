def checkio(text, word):
    array = []
    word = word.lower()

    for x in text.split('\n'):

        array.append(x.replace(" ", "").lower())


    H,wl = len(array),len(word)

    for i in range(H):
        row = array[i]
        for ii in range(len(row)):
            if row[ii] ==word[0]:
                # horizontal:
                start =ii

                if row[start:start+wl] ==word:

                    return [i+1, start+1, i+1, start+wl]

                #vertical
                if i+wl>H:

                    continue
                else:
                    found = 1
                    for j in range(1,wl):
                        print(array[i+j][start],word[j])
                        if array[i+j][start]!=word[j]:
                            found*=0
                            break
                    if found:
                        return [i+1, start+1, i+wl, start+1]