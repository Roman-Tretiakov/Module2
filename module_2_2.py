first = int(input('Please enter first any integer: '))
second = int(input('Please enter second any integer: '))
third = int(input('Please enter first any integer: '))

if first == second == third:
    print('3: All numbers are equals')

elif first != second and second != third and third != first:
    print('0: All numbers are not equals')

else:
    print('2: At least two numbers are equals')
