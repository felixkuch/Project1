# Detect Prime Numbers

# Choose random number
num = 138

# Prime number has to meet the following:
# 1. natural number
# 2. >1
# 3. only divisible by itself and 1

# prime numbers are greater than 1
if num > 1:
    # check if num
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            #print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# prime number has to be >1
else:
    print(num, "is not a prime number")