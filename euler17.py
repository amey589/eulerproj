d = {
        0:"",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety",
        100:"hundred",
        1000:"thousand",
    }

def to_english(n):
#print(get_thousands_place(n)+ get_hundreds_place(n)+ get_tens_place(n)+ get_ones_place())
    if n >= 0 and n <= 20:
        return d[n]
    if n>20 and n < 100:
        return d[(n//10)*10] + to_english(n % 10)
    if n>=100 and n<1000:
        return d[ n // 100] + "HundredAnd" + to_english(n%100)
    if n >= 1000:
        return d[ n // 1000] + "ThousandsAnd" + to_english(n%100)
for i in range(1,1001):
    print(to_english(i))
