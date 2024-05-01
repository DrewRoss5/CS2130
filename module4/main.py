from matrix_relation import MatrixRelation

def print_matrix(mat):
    for i in mat.matrix:
        print(i)
    print('\n')

def main():
    # Create the MatrixRelation that represents
    # the image in the instructions
    matrix = MatrixRelation([[0, 0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1],
                             [1, 1, 0, 1, 0, 0]])
    # Print the MatrixRelation
    print_matrix(matrix)
    # Print the reflexive closure of the relation
    print_matrix(matrix.reflexive_closure())
    # Print the symmetric closure of the relation
    print_matrix(matrix.symmetric_closure())
    # Print a statement indicating if the relation
    # is a rooted tree or not
    if matrix.is_rooted_tree():
        print("The relation is a rooted tree")
    else:
        print("The relation is NOT a rooted tree")

if __name__ == '__main__':
    main()
