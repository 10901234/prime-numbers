def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    

end_num = int(input("Enter a number \n"))
sum = 0
for i in range(2, end_num):
    if isPrime(i):
        print(i)
        sum = sum + i

print(sum)