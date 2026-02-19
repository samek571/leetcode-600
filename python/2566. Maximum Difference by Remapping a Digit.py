class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        m9 = re.search(r'[0-8]', s)
        m0 = re.search(r'[1-9]', s)
        if m9:
            digit = m9.group()
            max_s = s.replace(digit, '9')
        else:
            max_s = s
        if m0:
            digit = m0.group()
            min_s = s.replace(digit, '0')
        else:
            min_s = s
        return int(max_s) - int(min_s)
