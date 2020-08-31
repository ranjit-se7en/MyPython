if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    listed=list(arr)
    uniquelist=[]
    for i in listed:
        if i not in uniquelist:
            uniquelist.append(i)
    length=list.__len__(uniquelist)
    list.sort(uniquelist)
    print(uniquelist[length-2 ])
