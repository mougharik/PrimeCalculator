#!/usr/bin/python

import math

#menu skeleton
def menu():
    print('                 Menu\r')
    print('B - Determines if a particular value is prime\r')
    print('L - Lists the prime numbers in a given range\r')
    print('M - Prints the Prime Calculator menu\r')
    print('Q - Exits program\n\n')

#checks if value given is prime
def isprime(n):
    if n in [0,1]:
        return False

    if (n > 2) and (n % 2 == 0):
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

#outputs prime list
def primeList(x):
    prime = []
    for i in range(x+1):
        if isprime(i):
            prime.append(i)
    print(prime)
    print('\n')

#main
def main():
    print('\n')
    print('             Prime Calculator\r')
    print('___________________________________________\n\n')

    loop = 1
    while loop == 1:
        menu()
        choice = input('>')
        print('\n')
        if (choice == 'b') or (choice == 'B'):
            x = int(input('Enter a positive integer: '))
            if (isprime(x)):
                print(str(x) + ' is prime\n')
            else:
                print(str(x) + ' is not prime\n')
        elif (choice == 'l') or (choice == 'L'):
            x = int(input('Enter a positive integer: '))
            primeList(x)
        elif (choice == 'm') or (choice == 'M'):
            continue
        elif (choice == 'q') or (choice == 'Q'):
            loop = 0
        else:
            print('Please enter a valid menu option!')


if __name__ == "__main__":
    main()

