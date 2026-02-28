class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        value = ''
        for i in range(n+1):
            value += str(bin(i)[2:])
        value = int(value, 2)
        if(value > pow(10, 9) + 7):
            value = value % (pow(10,9) + 7)
        return value 