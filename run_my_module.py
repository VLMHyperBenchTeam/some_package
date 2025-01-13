from some_package.my_module import Calculator, greet


if __name__ == "__main__":
    print(greet(name="Ivan"))

    calc = Calculator()
    print(calc.add(1, 3))
