class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        return [c[0] for c in sorted(filter(lambda c: c[2] and c[1] in set(["electronics", "grocery", "pharmacy", "restaurant"]) and c[0] and all(c.isdigit() or c.isalpha() or c == '_' for c in c[0]), zip(code, businessLine, isActive)), key=lambda c: (c[1], c[0]))]
