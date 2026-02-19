class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        #no heuristic
        n, i=len(bits), 0
        while i < n-1:
            i+= 1+(bits[i]==1) # T/F maps to 1/0

        return i==n-1
