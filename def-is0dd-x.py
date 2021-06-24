def isOdd(x):
    if (x>30 or x<0):
        return 'number is out of given range'
    elif (x<30 or x%2==1):
        return 'number is odd'
    else:
        return 'number is even'

print(is0dd(21))