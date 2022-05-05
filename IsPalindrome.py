 def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum,s))
        s=s.lower()
        
        i = 0
        j = len(s)-1
        #while( i < j)
        while (i < len(s)//2 and j > len(s)//2 -1 ):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
        s = list(s)
        r = s[::-1]
        return s == r
    i = 0
j = len(s) - 1
while i < j and s[i] == s[j]:
    i += 1
    j -= 1
return i >= j

re.sub(r'[^A-Za-z0-9]+', '', s).lower()