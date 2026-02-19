class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        dry_acc, seen, res = [], dict(), [-1] * len(rains) #-1 for infinity simulation

        for i in range(0, len(rains)):
            if rains[i] == 0:
                dry_acc.append(i)
            else:
                lake = rains[i]
                if lake in seen:
                    j=0
                    while j < len(dry_acc) and dry_acc[j] < seen[lake]-1:
                        j += 1

                    if j >= len(dry_acc):
                        return []
                    else:
                        res[dry_acc[j]] = lake
                        dry_acc.remove(dry_acc[j])
                        seen[lake] = i+1
                else:
                    seen[lake] = i+1

        #correction of infinity
        for i in range(0, len(rains)):
            if res[i] == -1 and rains[i] == 0:
                res[i] = 1

        return res
