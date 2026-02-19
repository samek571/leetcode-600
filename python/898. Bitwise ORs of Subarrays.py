class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        _internal_list, l = [], 0

        for elem in arr:
            h = len(_internal_list)
            _internal_list.append(elem)

            for idx in range(l, h):

                _expr = _internal_list[idx] | elem
                if _expr != _internal_list[-1]:
                    _internal_list.append(_expr)
            l = h

        return len(set(_internal_list))
