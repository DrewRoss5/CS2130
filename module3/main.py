import functions
import sets

# prints out the domain, target, and range of a function, and prints the properties of the function
def print_function(domain, target, range):
    print(f"Domain: {domain}\nTarget: {target}\nRange: {range}")
    print(f"One-to-One: {functions.is_one_to_one(domain, target, range)}\nOnto: {functions.is_onto(domain, target, range)}\nBijection: {functions.is_bijection(domain, target, range)}")

def main():
    # Part 1 Sets
    print("Part 1 Sets")
    set_a = [1, 4, 3 ,6, 7]
    set_b = [2, 3, 4, 7, 9]
    set_c = [1, 2, 4, 5, 6, 7, 8]
    print(f"Lists that represent sets A, B, and C\n{set_a}\n{set_b}\n{set_c}")

    # set opperations that need to be referenced more than once
    a_b_union = sets.union_of_sets(set_a, set_b)
    a_b_intersect = sets.intersection_of_sets(set_a, set_b)

    print("\nSet Operations")
    print(f"A union B {a_b_union}")
    print(f"A intersect B:  {a_b_intersect}")
    print(f"A union B union C: {sets.union_of_sets(a_b_union, set_c)}")
    print(f"(A union B) intersect C: {sets.intersection_of_sets(a_b_union, set_c)}")
    print(f"A union (B intersect C): {sets.intersection_of_sets(set_a, sets.intersection_of_sets(set_b, set_c))}")
    print(f"(A intersect C) union B: {sets.union_of_sets(sets.intersection_of_sets(set_a, set_c), set_b)}")
    print(f"A union (C intersect B): {sets.union_of_sets(set_a, sets.intersection_of_sets(set_c, set_b))}")
    # Part 2 Functions
    print("\nPart 2 Functions")

    print("\nFunction f")
    print_function([3, 8, 11, 13, 22], [3, 5, 7, 9, 15], [7, 9, 3, 15, 5])

    print("\nFunction g")
    print_function([3, 8, 11, 13, 22], [8, 11, 16, 18], [18, 16, 11, 8, 11])

    print("\nFunction h")
    print_function([2, 4, 5, 6, 9], [1, 4, 7, 8, 11, 13], [4, 7, 1, 8, 11])


if __name__ == '__main__':
    main()

