def isIsomorphic(s: str, t: str) -> bool:
    test={}
    if len(s)!=len(t):
        return False
    if len(s)==len(t)==0:
        return True
    else:
        for i in range(len(s)):
            if test.get(s[i],0)==0:
                if t[i] in test.values():
                    return False
                test[s[i]]=t[i]
            else:
                if test[s[i]]!=t[i]:
                    return False
        return True
                
    
print(isIsomorphic("babc","baba"))