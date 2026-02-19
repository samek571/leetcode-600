class Solution:
    def numRabbits(self, responses: List[int]) -> int:
        return sum(ceil(val / (key + 1)) * (key + 1) for key, val in Counter(responses).items())

        # we are taking incomplete but started color groups (ceil).
        #If its not started then / key+1 * key+1 is just an inverse operation which kills itself.
        #Counter just makes hashmap quickly, iterating its key and val which is rabbit:response
