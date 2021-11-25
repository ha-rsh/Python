# program to take string of characters and convert each character of string into its ASCII value and take xor of all.

def xor_ch(string):
    int_1=ord(string[0])
    print('ASCII value of {} is:{}'.format(string[0], ord(string[0])))
    for i in range(1,len(string)):
        int_1=int_1 ^ ord(string[i])
        print('ASCII value of {} is:{}'.format(string[i],ord(string[i])))
    print('\nXOR of each ASCII value of character in string=',int_1)

string = input('Enter the string:')
xor_ch(string)