def main() -> None:
    temperature = int(input("Enter temperature in Celsius: "))
    if temperature < 1:
        print("It is freezing.")
    else:
        print("It is not freezing.")

if __name__ == "__main__":
    main()
