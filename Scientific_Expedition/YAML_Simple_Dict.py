def yaml(a):
    # your code here


    ans = {}
    entries = a.splitlines()

    for e in entries:
        if len(e):
            ent =  e.split(": ")
            try:
                ans[ent[0]]=int(ent[1])
            except:

                ans[ent[0]]=ent[1]
    return ans
