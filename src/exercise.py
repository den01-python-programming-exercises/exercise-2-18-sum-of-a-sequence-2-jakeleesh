def main():
    #write your code below this line
    first = int(input("First number?"))
    last = int(input("Last number?"))
    sum = 0
    for i in range(first, last + 1):
        sum += i
    print("The sum is " + str(sum))

if __name__ == '__main__':
    main()
