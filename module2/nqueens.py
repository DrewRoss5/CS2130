class Nqueens:
    def __init__(self, n):
        self.n = n
        self.queens = [-1] * n

    def print_solution(self):
        if self.queens[0] == -1:
            print("No Solution")
        for i in self.queens:
            chars = list(' '  * self.n)
            chars[i] = 'Q'
            print(f"|{'|'.join(chars)}|")


    def is_valid(self, rows):
        """Check if the positioning listed in the queens arrays is valid up to "rows"
        Ignore queens with an index >= rows.
        A valid position is one which does not share a column or diagonal with
        any other queen."""
        for i in range(rows - 1):
            # check if any two queens share this column
            if self.queens[i] in self.queens[i + 1:] or self.queens[i] in self.queens[:i]:
                return False
            # check the diagonals
            left = self.queens[i] - 1
            right = self.queens[i] + 1
            above = i - 1
            below = i + 1
            while (below < rows or above > -1) and (right < rows or left > -1):
                # check the diagonals above the cell 
                if above > -1:
                    if self.queens[above] == left or self.queens[above] == right:
                        return False
                if below < rows:
                    if self.queens[below] == left or self.queens[below] == right:
                        return False
                # increment and decrement left, right, above, and below respectivele
                below += 1
                above -= 1
                right += 1
                left -= 1
        return True


    def backtrack(self, row):
        if row == self.n:
            return self.is_valid(row)

        for col in range(self.n):
            self.queens[row] = col
            if self.is_valid(row + 1) and self.backtrack(row + 1):
                return True
            self.queens[row] = -1

        return False

    def backtracking_find_solution(self):
        self.backtrack(0)

    def bruteforce(self, row):
        if row == self.n:
            return self.is_valid(row)

        for col in range(self.n):
            self.queens[row] = col
            if self.bruteforce(row + 1):
                return True
            self.queens[row] = -1

        return False

    def brute_force_find_solution(self):
        self.bruteforce(0)
