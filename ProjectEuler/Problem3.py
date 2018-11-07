def findListOfPrimeNumbers(maxValue):
    listOfPrimeNumbers = [2, 3]

    valueToCheck = listOfPrimeNumbers[-1]
    isPrime = True

    while not valueToCheck > maxValue:

        valueToCheck += 2
        isPrime = True

        for prime in listOfPrimeNumbers:
            if valueToCheck % prime == 0:
                isPrime = False
                break

        if isPrime:
            listOfPrimeNumbers.append(valueToCheck)

    return listOfPrimeNumbers

def FindLargestPrimeFactor(number):

    divider = int(number / 2)

    for i in range(2, int(number / 2), 1):
        if (number % i == 0) and ((number / i) % 2 != 0):
            divider = number / i
            break

    listOfPrimeNumbers = findListOfPrimeNumbers(divider)

    for prime in reversed(listOfPrimeNumbers):
        if number % prime == 0:
            return prime

import time

start = time.time()
print("Largest prime factor = ", FindLargestPrimeFactor(600851475143))
end = time.time()
print("Found in (seconds) = ", end - start)
