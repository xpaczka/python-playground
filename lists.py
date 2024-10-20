from random import randrange
from math import sqrt, gcd, floor
from functools import reduce


def createString(list):
    stringList = ""

    for item in list:
        stringList += f"{str(item)} "

    return stringList.strip()


def createList(input):
    itemsList = []

    for x in input:
        itemsList.append(x)

    return itemsList


def createListInRange(start, end, length):
    rangeList = []

    for _ in range(length):
        rangeList.append(randrange(start, end + 1))

    return rangeList


def createSquareMatrix(start, end, size):
    matrix = []

    for _ in range(size):
        matrix.append(createListInRange(start, end, size))

    return matrix


def task1():
    numList = createListInRange(-10, 10, 10)

    minNumber = min(numList)
    maxNumber = max(numList)

    # Manually determining min and max number
    # minNumber = sorted(numList)[0]
    # maxNumber = sorted(numList)[-1]

    average = sum(numList) / len(numList)

    smallerThanAverageValues = filter(lambda x: x < average, numList)
    greaterThanAverageValues = filter(lambda x: x > average, numList)

    reversedNumList = list(reversed(numList))

    print(f"Numbers list: {createString(numList)}")
    print(f"Min: {str(minNumber)}, Max: {str(maxNumber)}")
    print(f"Average: {str(average)}")
    print(f"Smaller than average: {len(createList(smallerThanAverageValues))}")
    print(f"Greater than average: {len(createList(greaterThanAverageValues))}")
    print(f"Reverse order: {createString(reversedNumList)}")


def task2():
    numbers = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }

    numList = createListInRange(1, 10, 20)

    for x in numList:
        numbers[x] += 1

    for value, count in numbers.items():
        print(f"{value} - {count}")


def task3():
    numRange = 5
    matrix = createSquareMatrix(-numRange, numRange, numRange)

    print("Original matrix:")

    for i in range(len(matrix)):
        print(matrix[i])

    transposedMatrix = list(zip(*matrix))

    maxValues = []
    minValues = []

    for i in range(len(transposedMatrix)):
        maxValues.append(max(transposedMatrix[i]))
        minValues.append(min(transposedMatrix[i]))

    print("Max values:")
    print(maxValues)
    print("Min values:")
    print(minValues)


def task4():
    aNum = int(input("Enter first positive number: "))

    while aNum < 1:
        print("Number must be greater than zero")
        aNum = int(input("Enter first positive number: "))

    bNum = int(input("Enter second positive number: "))

    while bNum < 1:
        print("Number must be greater than zero")
        bNum = int(input("Enter second positive number: "))

    numRange = sorted([aNum, bNum])
    numList = []

    for x in range(numRange[0], numRange[1] + 1):
        if x % 2 != 0:
            numList.append(x)

    print(numList)
    print(list(map(lambda x: (x, 2**x, sqrt(x)), numList)))


def task5():
    aNum = int(input("Enter first number: "))
    bNum = int(input("Enter second number: "))
    size = int(input("Enter matrix size: "))

    numRange = sorted([aNum, bNum])
    matrix = createSquareMatrix(numRange[0], numRange[1], size)

    squares = []

    for x in range(1, size + 1):
        squares.append([row[:x] for row in matrix[:x]])

    intersectionsSums = []
    oddsSum = 0

    for i in range(len(squares)):
        for j in range(len(squares[i])):
            if i == j:
                sum = reduce(lambda a, b: a + b, squares[i][j])
                intersectionsSums.append(sum)

            if i % 2 != 0 and j % 2 != 0:
                oddsSum += matrix[i][j]

    reversedMatrix = list(reversed(list(map(lambda x: list(reversed(x)), matrix))))

    print(f"Sum of intersections: {intersectionsSums}")
    print(f"Odd indexes sum: {oddsSum}")
    print(reversedMatrix)


def task6():
    size = int(input("Enter size: "))

    while size < 1:
        print("Value must be greater than 0")
        size = int(input("Enter size: "))

    valuesList = []

    for i in range(size):
        sublist = []

        for j in range(size):
            if gcd(i + 1, j + 1) == 1:
                sublist.append("+")
            else:
                sublist.append(".")

        valuesList.append(sublist)

    headers = ["  "]

    for i in range(size):
        headers.append(str(i + 1).rjust(2, " "))

    print(" ".join(headers))

    for i in range(len(valuesList)):
        formattedList = list(map(lambda x: x.rjust(2, " "), valuesList[i]))
        values = [str(i + 1).rjust(2, " ")] + formattedList
        print(" ".join(values))


def task7a():
    numRange = int(input("Enter a number: "))

    while numRange <= 2:
        print("Number must be grater than 2")
        numRange = int(input("Enter a number: "))

    numList = []

    for x in range(2, numRange + 1):
        numList.append(x)

    for num in range(2, floor(sqrt(numRange)) + 1):
        for i in range(len(numList)):
            if numList[i] != None and numList[i] != num and numList[i] % num == 0:
                numList[i] = None

    primeNumsList = list(filter(lambda a: a != None, numList))
    print(", ".join(list(map(lambda a: str(a), primeNumsList))))
