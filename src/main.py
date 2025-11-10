from src.rpn_enigne import ReversePolishMachine


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    instanceofRPN = ReversePolishMachine()

    print("Калькулятор Обратной Польской Нотации")
    print("Можно вводить выражения со скобками:")
    print("( 3 4 + ) ( 5 2 - ) *")
    print("( 8 ( 3 2 + ) - ) 4 *") 
    print("\nДля выхода введите 'закончить' или ctrl + c (-_-)")

    while True:
        try:
            expression_input = input("\nВведите выражение: ").strip()

            if expression_input.lower() in ["Закончить"]:
                break

            if not expression_input:
                continue

            final_result = instanceofRPN.calculate(expression_input)
            print(f"Результат: {final_result}")
            # print(SAMPLE_CONSTANT)

        except ValueError as e:
            print(f"Ошибка: {e}")
        except KeyboardInterrupt:
            print("\nПрограмма завершена")
            break
        
if __name__ == "__main__":
    main()
