class Solution:
    def pushDominoes(self, d: str) -> str:
        #it could have been done via regex but this one is simplier

        tmp = ''
        while d != tmp:
            tmp = d
            #xxx is just helper we finish that at the end, necesarry condition so we dont trigger false movement
            d = (d.replace('R.L', 'xxx').replace('.L' , 'LL' ).replace('R.' , 'RR' ))#resolve moving

        return d.replace('xxx', 'R.L')#and resolve stationary
