from src.rpn_engine import ReversePolishMachine

def main() -> None:
    """
    типа точка входа
    """

    calc = ReversePolishMachine()

    print("Можно вводить выражения со скобками вот так:")
    print("( 3 4 + )")
    print("( 3 4 + ) ( 5 2 - ) *") #пример Самира
    print("( 8 ( 3 2 + ) - ) 4 *") #пример Самира
    print("Если надоело - пиши 'закончить' или жми ctrl+c")

    while True:
        try:
            user_input = input("\nВведи выражение: ").strip()

            if user_input.lower() in ["закончить"]:
                print("Пока!")
                break

            if user_input == "":
                continue

            result = calc.calculate(user_input)
            print(f"Получилось: {result}")

        except ValueError as e:
            print(f"Ой, ошибка: {e}")
        except KeyboardInterrupt:
            print("\nНу ладно, пока!")
            break
        except Exception as e:
            print(f"Что-то пошло не так: {e}")

if __name__ == "__main__":
    main()
