class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #s string p pattern
        def matching(i, j):
            if(j == len(p)):
                return i == len(s) #controllo se ho consumato il pattern e la stringa, in caso affermativo ho raggiunto la "meta"
            
            match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            #controllo se il prossimo carattere del pattern è un asterisco che è la wild card di questa regex
            if(((j+1) < len(p)) and p[j+1] == '*'):
                return matching(i, j+2) or (match and matching(i+1, j)) #nel primo caso skippo i due caratteri (considero zero)
                #nel secondo caso se già matcha qua aumento il conto della stringa e mantengo la j al carattere da confrontare
            if(match):
                return matching(i+1, j+1)
            
            return False
        
        return matching(0,0)



        