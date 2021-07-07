class FormulaError(Exception):
    pass


class Calculator:

    @staticmethod
    def calculate(lst):
        if lst[1] == "+":
            return int(lst[0]) + int(lst[2])
        if lst[1] == "-":
            return int(lst[0]) - int(lst[2])
        if lst[1] == "*":
            return int(lst[0]) * int(lst[2])
        if lst[1] == "/":
            return int(lst[0]) / int(lst[2])
        else:
            raise FormulaError("invalid operator")


def main():
    val = input("Enter your value: ")
    print(val)
    calci = Calculator()
    lst = []
    lst = val.split(" ")
    print(lst)
    if len(lst) != 3:
        raise FormulaError("greater than 3")

    try:
        float_value = float(lst[0])
        float_value_new = float(lst[2])
    except ValueError as ve:
        raise FormulaError("Not able to convert to float")

    result = calci.calculate(lst)
    print(result)


if __name__ == "__main__":
    main()
