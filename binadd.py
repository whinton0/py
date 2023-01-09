import sys

def main(): 
    print("Enter year: ") 
    y = int(input()) 
    if y%4==0 and y%100!=0: 
        print(f"\nIt is a Leap year") 
    elif y%400==0: 
        print(f"\nIt is a Leap year") 
    else: 
        print(f"\nIt is not a Leap year")

if (__name__) == "__main__":
    main()
