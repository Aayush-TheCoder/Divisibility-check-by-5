def main():
    num = int(input("Enter a value : "))
    if num%5 == 0:
        print("It is divisible by 5.")
    else:
        print("It is not divisible by 5.")

while True:
    main()

    continuity = input("Want to continue? (yes: y, no: n)): ")
    
    match continuity:
        case "y": continue
        case "n": print("\nThanks for using the program. Have a good day!"); input(); break
