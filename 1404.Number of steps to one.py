class Solution:
    def numSteps(self, s: str) -> int:
        def operation(n):
            if(n % 2 == 0):
                n = n//2
            elif(n % 2 != 0):
                n += 1
            return n
        cnt = 0
        n = int(s, 2)
        while(n != 1):
            n = operation(n)
            cnt += 1
        return cnt
        