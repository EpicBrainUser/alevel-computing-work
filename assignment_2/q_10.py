from dataclasses import dataclass

# by providing default values (None) in the dataclass, we can initialise it without giving any values,
# then as the values are input by the user the default None values are replaced with the user values


@dataclass
class Garden:
    length: float | None = None
    width: float | None = None

    # this decorator @property makes surface area an attribute in the class meaning you can access it
    # with the dot syntax as if it were a normal value

    # the None checks are needed incase the garden has not been given values

    @property
    def surface_area(self) -> float | None:
        if self.length is None or self.width is None:
            return None

        return self.length * self.width


def main() -> None:
    garden = Garden()
    while True:
        try:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            if length <= 0 or width <= 0:
                raise ValueError("Values must be positive and cannot be zero")
            garden.length = length
            garden.width = width
            break

        except ValueError as e:
            print(f"Values must be positive numbers: {e}")

    if garden.surface_area is None:
        raise ValueError("Garden's values not set!")
    print(f""" \n\nBehold the garden:
    length: {garden.length}
    width: {garden.width}
    area: {garden.surface_area}
    """)


if __name__ == "__main__":
    main()
