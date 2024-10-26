def printrev(s, end):
    if(end == -1):
        return
    print(s[end],end="")
    printrev(s,end-1)

name = "alianwar"
printrev(name, len(name)-1)