def findListOfPrimeNumbers(maxValue):
    listOfPrimeNumbers = [2, 3]

    valueToCheck = listOfPrimeNumbers[-1] + 2
    prime = True

    while not valueToCheck > maxValue:

        isPrime = True
        for prime in listOfPrimeNumbers:
            if valueToCheck % prime == 0:
                isPrime = False
                break

        if isPrime:
            listOfPrimeNumbers.append(valueToCheck)

        valueToCheck += 2

    return listOfPrimeNumbers

def FindLargestPrimeFactor(number):

    halfNumber = number / 2

    if number % 2 != 0:
        halfNumber = (number + 1) / 2

    listOfPrimeNumbers = findListOfPrimeNumbers (halfNumber)

    for prime in reversed(listOfPrimeNumbers):
        if 600851475143 % prime == 0:
            return prime

import time

start = time.time()
print("Biggest prime factor = ", FindLargestPrimeFactor(1000000))
end = time.time()
print("Found in (seconds) = ", end - start)

