a = [1, 1, 1, 1]
b = [1, 1, 0, 1]

class Solution(object):
    def addBinary(self, a, b):
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += a[i]
                i -= 1
            if j >= 0:
                total += b[j]
                j -= 1
            result.append(total % 2)
            carry = total // 2

        return result[::-1]

Sol = Solution()
print(Sol.addBinary(a, b))
