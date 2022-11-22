#Convert Roman numerals to integer

#Time Submitted 	Status		Runtime	Memory	Language
#06/19/2022 12:26	Accepted	42 ms	13.8 MB	python3

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  # Dictionary with all roman symbols
        sum_num = 0
        j = None  # Need it in loop as previous iteration index
        re_s = list((s[::-1]))  # reverse input list

        for i, char in enumerate(re_s):  # numerate all char in list re_s
            if j != None:
                if rom_dict[re_s[i]] >= rom_dict[re_s[j]]:  # compare roman symbols value
                    sum_num += rom_dict[re_s[i]]
                else:
                    sum_num -= rom_dict[re_s[i]]
            else:
                sum_num += rom_dict[re_s[i]]
            j = i  # previous iteration index
        return sum_num