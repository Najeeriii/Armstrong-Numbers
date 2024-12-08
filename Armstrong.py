def count_digits(number):

    digits = 0

    while number != 0:
        number = number//10
        digits +=1

    return digits

def is_armstrong(n):
    
    number_of_digits=count_digits(n)

    temp = n
    sum= 0

    while temp != 0:
        digit = temp % 10
        temp = temp // 10
        sum += digit ** number_of_digits

    return sum == n
print(is_armstrong(153))