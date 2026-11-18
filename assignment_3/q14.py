# def alternative_approach(month: int) -> str:
#     # guard clause
#     if month < 1 or month > 12:
#         raise ValueError("invalid month number")
#         # the assignment said 'output', and an error is an output
#         # having said that, errors should be handled with a try/except block and then outputted but
#         # this is a simple demo so it's fine
#         # alternatively I could have said 'return "invalid number month", and just print the return value,
#         # as if it was a season, but I wanted to separate errors from values
#
#     # if the previous 'if' goes through, code won't reach here, so no elif needed
#     if month in (1, 2, 12):
#         return "Winter"
#     elif month in (3, 4, 5):
#         return "Spring"
#     elif month in (6, 7, 8):
#         return "Summer"
#     elif month in (9, 10, 11):
#         return "Autumn"
#     else:
#         raise
#         # this code should be unreachable so we use a bare 'raise' to inspect the stack trace


def main() -> None:
    MONTHS_MAPPING = {
        (1, 2, 12): "Winter",
        (3, 4, 5): "Spring",
        (6, 7, 8): "Summer",
        (9, 10, 11): "Winter",
    }

    month = int(input("Pick a month between 1 and 12 to see what season it is: "))
    # usage of alternative approach
    # print(alternative_approach(month))
    if month < 1 or month > 12:
        print("invalid number month")
        return
    for key, value in MONTHS_MAPPING.items():
        if month in key:
                print(value)


if __name__ == "__main__":
    main()
