# A simple Python code to print truth tables for propositions and boolean
# expressions

# Import the Logic and Boolean modules
import logic
import boolean

# prints a truth table given a proposition or expression and inputs
def truth_table(vals, proposition):
    for i in vals:
        print(f'  {i[0]} | {i[1]} | {i[2]} | {proposition(*i)}')

def main():
    logic_values = ('TTT', 'TTF', 'TFT', 'TFF', 'FTT', 'FTF', 'FFT', 'FFF')
    bool_values = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1))
    # Print truth table for proposition 1
    print("  p | q | r | proposition 1")
    truth_table(logic_values, logic.proposition1)
    print()


    # Print truth table for proposition 2
    print("  p | q | r | proposition 2")
    truth_table(logic_values, logic.proposition2)
    print()


    # Print truth table for proposition 3
    print("  p | q | r | proposition 3")
    truth_table(logic_values, logic.proposition3)
    print()


    # Print truth table for Boolean expression 1
    print("  x | y | z | expression 1")
    truth_table(bool_values, boolean.expression1)
    print()


    # Print truth table for Boolean expression 2
    print("  x | y | z | expression 2")
    truth_table(bool_values, boolean.expression2)
    print()


    # Print truth table for Boolean expression 3
    print("  x | y | z | expression 3")
    truth_table(bool_values, boolean.expression3)
    print()


if __name__ == '__main__':
    main()
