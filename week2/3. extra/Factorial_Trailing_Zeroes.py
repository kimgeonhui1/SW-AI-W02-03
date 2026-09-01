class Solution():
    def __init__(self):
        pass

    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return factorial(n-1) * n

    def trailingZeroes(self, n):
        cnt = 0
        i = 1
        while True:
            if n//5**i >= 1:
                cnt += n//5**i
                i += 1
            else:
                break
        return cnt
                
test1 = Solution()
test2 = Solution()
test3 = Solution()

test1_fact = test1.factorial(3)
test2_fact = test2.factorial(5)
test3_fact = test3.factorial(0)

print(test1.trailingZeroes(test1_fact))
print(test1.trailingZeroes(test2_fact))
print(test1.trailingZeroes(test3_fact))