def isprime(num) :
    check = 0
    for i in range(1, int(num / 2) + 1) :
        if(num % i == 0) :
            check += 1
        if(check > 1) : return 1
    return 0

if __name__ == "__main__" :
    num = int(input("Enter the number: "))
    if(isprime(num) == 0) : print("The number you entered is prime")
    else : print("The number you entered is not a prime")
