def isSubsequence(s: str, t: str) -> bool:
    sPointer,tPointer=0,0
    if len(s)==0:
        return True
    for tPointer in range(len(t)):
        if s[sPointer]==t[tPointer]:
            if sPointer==len(s)-1:
                return True
            sPointer+=1
    return False

print(isSubsequence("axc","ahbgdc"))