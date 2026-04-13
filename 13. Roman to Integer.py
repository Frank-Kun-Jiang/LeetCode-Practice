def romanToInt(s: str) -> int:
    dict= {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result,index=0,0
    lengStr=len(s)
    while index < lengStr:
        if index != lengStr-1 and dict[s[index]] < dict[s[index+1]]:
            result += dict[s[index+1]]-dict[s[index]]
            index+=2
        else:
            result += dict[s[index]]
            index+=1
    return result
            
        

print(romanToInt(""))