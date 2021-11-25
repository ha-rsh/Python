# occurance of first even number in the list.

print('\n************** occurance of first even number in the list *******************\n\n')


def check_even_list(arr):
    for number in arr:
        if number % 2 == 0:
            return True, number
        else:
            pass
    return False


choice = 'y'
num_list = []
while choice == 'y':
    num = int(input('enter the element in the list:'))
    num_list.append(num)
    choice = input('want to add more elements(y/n):')
print('\nthe list is as follows:', num_list)
a, b = check_even_list(num_list)
print(a, end='')
print(' the number is ', end='')
print(b)
