def canConstruct(ransomNote: str, magazine: str) -> bool:
    myDictionary={}
    for x in magazine:
        myDictionary[x]= myDictionary.get(x,0)+1
    
    for y in ransomNote:
        if myDictionary.get(y,0)==0:
            return False
        myDictionary[y]-=1
    return True
            


print(canConstruct("aaab","ab"))