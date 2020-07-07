class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num *= 10
            num += d
        
        num += 1
        output = []

        while num:
            temp = num % 10
            num //= 10
            output.append(temp)
        
        return output[::-1]