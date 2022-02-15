from sys import stdin
from collections import Counter

def check_palindrome(my_dict, list_of_num):
    n = len(list_of_num)
    count = 0
    my_dict_keys = []
    for key, item in my_dict.items():
        my_dict_keys.append(key)
        if item % 2:
            count += 1

    my_dict_keys.sort(reverse=True)
    if count >= 2: 
        print(-1) 
        return

    else:
        result = [None] * n
        start = 0
        end = n - 1
        for i in my_dict_keys:
            value = my_dict[i]
            while value > 0:
                if value % 2:
                    result[n//2] = i
                    value -= 1

                if value != 0:
                    result[start] = i
                    result[end] = i
                    value -= 2
                    start += 1
                    end -= 1

        outnum = ""
        for i in result:
            outnum += str(i)

        print(int(outnum))

innum = int(stdin.readline().strip())
list_of_num = list(map(int, str(innum)))
my_dict = Counter(list_of_num)
check_palindrome(my_dict, list_of_num)
