def main() -> None:
    temperature = int(input("Enter temperature in Celsius: "))
    if temperature < 1:
        print("Water is frozen")
    elif temperature > 100:
        print("Water is boiling")
    else:
        print("it is a liquid")

if __name__ == "__main__":
    main()
