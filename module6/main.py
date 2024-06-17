from permutation import Permutation
from combination import Combination


def numeric_input(prompt):
    while True:
        response_str = input(prompt)
        if response_str.removeprefix('-').isdigit():
            return int(response_str)
        else:
            print("Please provide a valid integer")
def main():
    # prompt the user for their numbers
    vals = []
    print("Enter the numbers you would like in the set (-1 to stop)")
    num = 0
    while num >= 0:
        num = numeric_input("")
        if num >= 0:
            vals.append(num)
    # get the target sum
    target_sum = numeric_input("Target sum: ")
    # prompt user to enter the subset length
    subset_len = numeric_input("Subset length: ")
    combo = Combination(vals, subset_len)
    # use the combination class to find all subsets of length n that sum to x
    print(f"All combinations that add to {target_sum}")
    reset  = False
    while not reset:
        reset = combo.next_combination()
        if sum(combo.current_combination) == target_sum:
            print(combo.current_combination)
    print("All permutations:")
    Permutation(vals).print_all_permutations()


# Run the main function
if __name__ == "__main__":
    main()
