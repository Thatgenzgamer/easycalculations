class Calc:

    def calc(opr, num1, num2):
        if (opr.lower() == "+") or (opr.lower() == "sum") or (opr.lower() == "plus"):
            print(num1 + num2)
        elif (opr.lower() == "-") or (opr.lower() == 'subtract') or (opr.lower() == 'minus'):
            print(num1 - num2)
        elif (opr.lower() == "*") or (opr.lower() == "multiply") or (opr.lower() == 'product'):
            print(num1 * num2)
        elif (opr == "/") or (opr == 'divide') or (opr == 'division'):
            print(num1 / num2)
        elif (opr.lower() == "**") or (opr.lower() == 'power') or (opr.lower() == 'power_of'):
            print(num1 ** num2)
