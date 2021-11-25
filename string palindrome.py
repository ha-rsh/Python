# to check string is palindrome or not.

# first way
def first_palindrome(s):
    if s == s[::-1]:
        print('palindrome')
    else:
        print('not palindrome')


a = True
while a:
    string = input('enter the string:')
    first_palindrome(string)
    choice = input('want to continue(y/n):')
    if choice == 'n':
        a = False


#second way
print("\t\t\t\t\t\t\t\n SECOND METHOD \n")


def palindrome(s):
    if s == ''.join(reversed(s)):
        print('palindrome')
    else:
        print('not palindrome')


a = True
while a:
    string = input('enter the string:')
    palindrome(string)
    choice = input('want to continue(y/n):')
    if choice == 'n':
        a = False

