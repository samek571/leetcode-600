class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [sorted(l) for l in languages]

        people = set()
        for u, v in friendships:
            a, b = langs[u-1], langs[v-1]
            i = j = 0
            ok = False
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    ok = True
                    break
                if a[i] < b[j]:
                    i += 1
                else:
                    j += 1
            if not ok:
                people.add(u-1)
                people.add(v-1)

        lang_freq = defaultdict(int)
        for p in people:
            for lang in langs[p]:
                lang_freq[lang] += 1

        best_count = max(lang_freq.values()) if lang_freq else 0
        return len(people) - best_count
