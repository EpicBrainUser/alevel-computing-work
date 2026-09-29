from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int

    def sum(self) -> int:
        return self.x + self.y + self.z


def main():
    integer_list: list[int] = []
    for i in range(120, 123):
        while True:
            try:
                value = input(f"Enter integer value for {chr(i)}: ")
                casted_value: int = int(value)
                integer_list.append(casted_value)
                break
            except ValueError as e:
                print(f"Failed to parse as int: {e}. \nEnter an integer.\n")

    point = Point(integer_list[0], integer_list[1], integer_list[2])
    print(f"Sum of entered values: {point.sum()}")


if __name__ == "__main__":
    main()
