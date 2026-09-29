class Person:
    def __init__(self, name: str, age: int, nationality: str) -> None:
        self.name: str = name
        self.age: int = age
        self.nationality: str = nationality


class Greeter:
    def __init__(self, person: Person) -> None:
        self.person: Person = person

    def greet(self) -> str:
        return f"Have a nice day, {self.person.name}. It must be nice to be {self.person.age} and {self.person.nationality}!"


def main() -> None:
    prompts = (
        "What is your name: ",
        "What is your age: ",
        "What is your nationality: ",
    )
    user_inputs = []
    for prompt in prompts:
        user_value = input(prompt)
        user_inputs.append(user_value)

    user = Person(name=user_inputs[0], age=user_inputs[1], nationality=user_inputs[2])
    greeter = Greeter(user)
    print(greeter.greet())


if __name__ == "__main__":
    main()
