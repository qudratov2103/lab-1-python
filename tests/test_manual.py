from src.rpn_engine import ReversePolishMachine

calc = ReversePolishMachine()
result = calc.calculate("3 4 2 * +")
print("Result:", result)
print("Stack at end:", calc.stack)