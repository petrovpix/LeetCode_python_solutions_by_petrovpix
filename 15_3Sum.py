#3Sum 


#Time Submitted     Status      Runtime Memory  Language
#06/23/2022 11:35   Accepted    4494 ms 17.3 MB python3

class Solution:
    def threeSum(self, num: list[int]) -> list[list[int]]:
        num.sort()
        ran = len(num) 
        res = set()

        if ran != 0 and num[0] <= 0 and 3 <= ran <= 3000:
            for i in range(0, ran):
                j = i+1
                k = ran-1
                while j < k:
                    if i != j and j != k and i != k and num[i]+num[j]+num[k] == 0:
                        res.add((num[i], num[j], num[k]))
                        k -= 1
                    elif num[i]+num[j]+num[k] < 0:
                        j += 1
                    elif num[i]+num[j]+num[k] > 0:
                        k -= 1

        return res