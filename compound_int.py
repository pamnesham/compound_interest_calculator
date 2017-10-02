#!python3

#This function calculates compund interest
def compInterest(starting, target, intRate):
    years = 0
    while starting <= target:
        starting = starting * (intRate/100 + 1)
        years += 1
    return years

#Ask the user for input and call compInterest on input
def main():
    print("Enter the starting balance.")
    starting = float(input())
    print("Enter your target balance.")
    target = float(input())
    print("Enter the interest rate.")
    intRate = float(input())
    finalBal = compInterest(starting, target, intRate)
    print("It will take " + str(finalBal)+ " years to reach this balance.")

if __name__ == '__main__':
    main()
