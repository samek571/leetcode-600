class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:

        #lazy evaluation of factorial
        f_hashmap = {0:1}
        def lazy_fact(n):
            if n not in f_hashmap:
                f_hashmap[n] = n*lazy_fact(n-1)
            return f_hashmap[n]


        #getting rid of duplicates by sorting and set
        seen = set()
        def helper(s):
            s = ''.join(sorted(s))
            if s in seen: return 0

            d = [0]*10
            for c in s:
                d[int(c)] += 1

            tmp = sum(d)
            num = (tmp-d[0]) * lazy_fact(tmp-1)
            _div = 1
            for d in d:
                _div *= lazy_fact(d)
            seen.add(s)
            return num//_div


        #doing reverse and truncating last digit for odd
        res = 0
        for i in range(10**((n-1)//2), 10**((n+1)//2)):
            _tmp = str(i) + str(i)[-1-n%2::-1]
            if int(_tmp)%k==0:
                res += helper(_tmp)
        return res
