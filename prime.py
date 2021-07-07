#check whether a number is prime or not.

num = 7

def check_prime(num):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            print(f"divisible by {i}")
            count = count + 1
        i = i + 1
    if count == 2:
        print("prime")
    else:
        print("Not prime")


if __name__ == '__main__':
    check_prime(num)