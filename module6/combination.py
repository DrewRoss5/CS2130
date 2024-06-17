import collections


class Combination:
    def __init__(self, values, subset_len):
        set_values = sorted(set(values))
        self.combination_set = list(set_values)
        self.subset_length = subset_len
        self.current_combination = list(self.combination_set[:subset_len])

    def reset_combination(self):
        self.current_combination = list(self.combination_set[:self.subset_length])

    def get_combination(self):
        return list(self.current_combination)

    def set_combination(self, combo):
        set_combo = sorted(set(combo))
        if len(set_combo) != self.subset_length:
            return
        for value in set_combo:
            if value not in self.combination_set:
                return
        self.current_combination = list(combo)

    def print_all_combinations(self):
        # print all combinations until the final is reached
        self.reset_combination()
        print(self.current_combination)
        while not self.next_combination():
            print(self.current_combination)

    def next_combination(self):
        # move from right to left in both the currentCombination and the combinationSet until the numbers do not match 
        index = None
        mismatch = None
        for i in range(1, self.subset_length + 1):
            if self.current_combination[-i] != self.combination_set[-i]:
                index = self.subset_length - i
                mismatch = self.current_combination[-i]
                break 
        # check if we are are at the final permutation
        if index == None:
            self.reset_combination()
            return True
        # fill in the current combination from the set of values, starting at the position of the number that initially mismatched in the set of values
        start_pos = self.combination_set.index(mismatch) + 1
        for i in range(index, self.subset_length):
            self.current_combination[i] = self.combination_set[start_pos]
            start_pos += 1
        return False
