from heapq import heappush, heappop

class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))

        n = numberOfUsers
        direct = [0]*n
        here_acc = [0]*n
        here_mark = [0]*n
        online = [True]*n
        all_cnt = 0
        here_cnt = 0
        pq = []

        i, m = 0, len(events)
        while i < m:
            t = int(events[i][1])
            while pq and pq[0][0] <= t:
                _, u = heappop(pq)
                if not online[u]:
                    online[u] = True
                    here_mark[u] = here_cnt

            j = i
            while j < m and int(events[j][1]) == t:
                j += 1

            for k in range(i, j):
                typ, _, arg = events[k]
                if typ == "OFFLINE":
                    u = int(arg)
                    if online[u]:
                        here_acc[u] += here_cnt - here_mark[u]
                        online[u] = False
                        heappush(pq, (t + 60, u))

            for k in range(i, j):
                typ, _, arg = events[k]
                if typ == "MESSAGE":
                    for tok in arg.split():
                        if tok == "ALL":
                            all_cnt += 1
                        elif tok == "HERE":
                            here_cnt += 1
                        else:
                            direct[int(tok[2:])] += 1

            i = j

        return [
            direct[u] + here_acc[u] + (here_cnt - here_mark[u] if online[u] else 0) + all_cnt
            for u in range(n)
        ]
