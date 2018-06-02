def calculateTip(amt,rate):
    return amt * rate;

def printAnswer(amt,tip):
    # prints total, restarts program
    print("Your total bill is $ {:0.2f}.".format(amt + tip));
    print("Your tip is ${:0.2f}".format(tip));
    print("\n");
    main();

def main():
    # Parse input
    amt = input("How much is your bill? ");
    if(type(amt) != int and type(amt) != float):
	amt = input("Please input a number. How much is your bill? ");
    rate = input("What is the rate of your tip? ");
    if(type(rate) != int and type(rate) != float): 
	rate = input("Please input a number. What is the rate of your tip? ");

    # Convert numbers
    rate = rate / 100.0;
    tip = calculateTip(amt, rate);

    printAnswer(amt,tip)

main();
