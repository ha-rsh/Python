# occurance of all the  even numbers in the list.

print('\n************** occurance of all the  even numbers in the list *******************\n\n')


def check_even_list(arr):
    even_list = []
    for number in arr:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    return even_list


choice = 'y'
num_list = []
while choice == 'y':
    num = int(input('enter the element in the list:'))
    num_list.append(num)
    choice = input('want to add more elements(y/n):')
a = check_even_list(num_list)
print('the list of even numbers are: ', end='')
print(a)
