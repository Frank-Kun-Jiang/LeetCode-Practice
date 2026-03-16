def isPalindrome( s: str) -> bool:
    s = s.lower()
    if len(s)==0: return True
    right=len(s)-1
    for left in range(len(s)):
        if s[left].isalnum():
            while not s[right].isalnum():
                right-=1
            if s[left]!=s[right]:
                return False
            if left-right in [-1,0,1]:
                return True
            right-=1
    return True
        
            



print(isPalindrome("0P"))