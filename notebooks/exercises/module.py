def primalityTest (number):

    divisible = True

    if (number > 1):

        dividers = []

        for divisor in range (2, int(number**(1/2)) + 1):
            if (number % divisor == 0):
                dividers.append (divisor)

        if (len (dividers) == 0):
            divisible = False

    return divisible