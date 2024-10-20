from random import random


def task1():
    height = float(input("Input your height (m): "))
    weight = float(input("Input your weight (kg): "))

    bmi = weight / (height**2)

    if bmi < 18.5:
        print(f"{bmi}: Underweight")
    elif bmi < 24.9:
        print(f"{bmi}: Correct weight")
    else:
        print(f"{bmi}: Overweight")


def task2():
    price = float(input("Product's price: "))

    while price < 100 or price > 10_000:
        print("Price must be in range: 100 - 10.000")
        price = float(input("Product's price: "))

    instalmentsCount = int(input("Number of instalments: "))

    while instalmentsCount < 6 or instalmentsCount > 48:
        print("Number of instalments must be in range: 6 - 48")
        instalmentsCount = int(input("Number of instalments: "))

    if instalmentsCount < 13:
        price *= 1.025
    elif instalmentsCount < 25:
        price *= 1.05
    else:
        price *= 1.1

    monthlyInterest = price / instalmentsCount

    print(f"Calculated monthly interest: {round(monthlyInterest, 2)}")


def task3():
    number = int(input("Enter number: "))

    while number < 1:
        print("Number must be greater than 0")
        number = int(input("Enter number: "))

    numList = []

    for x in range(number):
        if x % 2 != 0:
            numList.append(str(x))

    print(", ".join(numList))


def task4():
    number = int(input("Enter number: "))

    while number < 1:
        print("Number must be greater than 0")
        number = int(input("Enter number: "))

    power = 0

    while 2**power <= number:
        print(str(2**power))
        power += 1


def task5():
    sum = 0
    number = int(input("Enter number: "))

    while number != 0:
        sum += number
        number = int(input("Enter number: "))

    print(str(sum))


def task6():
    numList = []
    number = int(input("Enter number: "))

    while number != 0:
        numList.append(number)
        number = int(input("Enter number: "))

    sortedNumList = sorted(numList)

    listSum = sortedNumList[0] + sortedNumList[-1]
    average = sum(sortedNumList) / len(sortedNumList)

    print(f"Sum: {str(listSum)}, Average: {str(average)}")


def task7():
    computerNumber = int(random() * 100)
    userNumber = int(input("Enter number: "))

    while userNumber != computerNumber:
        if userNumber > computerNumber:
            print("Number too big")
        else:
            print("Number too small")
        userNumber = int(input("Enter number: "))

    print("Number correct")


def task8():
    number = int(input("Enter number: "))

    if number < 10:
        print(f"Sum: {str(number)}, Average ratio: 0")
        return

    numberSum = 0
    evenNumbers = []
    oddNumbers = []

    for num in str(number):
        numberSum += int(num)

        if int(num) % 2 == 0:
            evenNumbers.append(int(num))
        else:
            oddNumbers.append(int(num))

    evenAverage = sum(evenNumbers) / len(evenNumbers)
    oddAverage = sum(oddNumbers) / len(oddNumbers)

    print(evenAverage, oddAverage)

    print(f"Sum: {str(numberSum)}, Average ratio: {str(evenAverage / oddAverage)}")


def task9():
    number = int(input("Enter number: "))
    numList = []

    for x in range(number + 1):
        if x > 0 and number % x == 0:
            numList.append(str(x))

    print(", ".join(numList))


def task10():
    number = int(input("Enter number: "))

    while number < 2:
        print("Number must be greater than 1")
        number = int(input("Enter number: "))

    for x in range(2, number):
        if number % x == 0:
            print(f"{number} is not a prime number")
            return False

    print(f"{number} is a prime number")
    return True
