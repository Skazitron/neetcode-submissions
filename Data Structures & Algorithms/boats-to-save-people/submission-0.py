class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1

        cnt = 0
        while (l <= r):
            k = limit
            k -= people[r]
            if (people[l] <= k):
                l += 1
            r -= 1
            cnt += 1

        return cnt