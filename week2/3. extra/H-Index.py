class Solution():
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations.sort(reverse=True)

        cnt = 0
        for x in range(len(citations)):
            if citations[x] >= x+1:
                cnt += 1
            else:
                break
        return cnt

test = Solution()

print(test.hIndex)