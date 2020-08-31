import sys
if __name__ == '__main__':
    i=0
    name=[]
    scores=[]
    combined=[]
    while i <= 2:
        n=input("Enter the name")
        s=float(input("Enter the scores"))
        name.append(n)
        scores.append(s)
        tes=[scores[i],name[i]]
        combined.append(tes)
        i += 1

    minscore=min(scores)
    maxscore=max(scores)





    print(name)
    print(scores)
    print(combined)
    print()
    print(minscore)
    #print(maxscore)
    print(name[minscore])
