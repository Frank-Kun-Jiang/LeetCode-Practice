def isAnagram(s: str, t: str) -> bool:
    Sdict,Tdict={},{}
    for i in s:
        if Sdict.get(i,0)==0:
            Sdict[i]=1
        else:
            Sdict[i]+=1
    for i in t:
        if Tdict.get(i,0)==0:
            Tdict[i]=1
        else:
            Tdict[i]+=1
    for x in Sdict:
        if Tdict.get(x,0)==0:
            return False
        elif Tdict[x]!=Sdict[x]:
            return False
    for x in Tdict:
        if Sdict.get(x,0)==0:
            return False
        elif Sdict[x]!=Tdict[x]:
            return False
    return True

print(isAnagram("rst","rsty"))