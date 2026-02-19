class Solution:
    def findWordsContaining(self, arr: List[str], x: str) -> List[int]:
        return [i for i in range(len(arr)) if x in arr[i]]
