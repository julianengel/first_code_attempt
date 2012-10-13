def fizzbuzz1(num):
    for number in range(1, num):
        if number % 3 == 0 and num % 5 == 0:
            print 'FizzBuzz'
        elif number % 3 == 0:
            print 'Fizz'
        elif number % 5 == 0:
            print 'Buzz'
        else:
            print number

def fizzbuzz2(num):
    for number in range(1,21):
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        if number % 5 != 0 and number % 3 != 0:
            output += str(number)
        print output


fizzbuzz1(50)
print "   "
fizzbuzz2(50)