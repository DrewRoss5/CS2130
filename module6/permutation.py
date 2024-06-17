
class Permutation:
    def __init__(self, values):
        set_values = sorted(set(values))
        self.current_permutation = list(set_values)

    def reset_permutation(self):
        self.current_permutation.sort()

    def get_permutation(self):
        return list(self.current_permutation)

    def set_permutation(self, perm):
        set_perm = sorted(set(perm))
        if len(set_perm) != len(self.current_permutation) and len(set_perm) != len(perm):
            return
        for value in set_perm:
            if value not in self.current_permutation:
                return
        self.current_permutation = list(perm)

    def print_all_permutations(self):
        # print all perutations until the final is reached
        self.reset_permutation()
        print(self.current_permutation)
        while not self.next_permutation():
            print(self.current_permutation)

    def next_permutation(self):
        perm_len = len(self.current_permutation) - 1
        # check if we are already at the final permutation, and reset it if so
        reset = True
        for i in range(1, perm_len + 1):
            if self.current_permutation[i] > self.current_permutation[i - 1]:
                reset = False
        if reset == True:
            self.reset_permutation()
            return True
        # move from right to left until the current number is less than the previous one
        index = perm_len
        prev = self.current_permutation[index]
        current = self.current_permutation[index - 1]
        while current >= prev:
            index -= 1
            prev = self.current_permutation[index]
            current = self.current_permutation[index - 1]  
        current_index = index - 1
        # start at the right and find the first number greater than current.
        greater_index = perm_len
        greater = self.current_permutation[greater_index]
        while greater <= current:
            greater_index -= 1
            greater = self.current_permutation[greater_index]
        # swap the numbers
        self.current_permutation[current_index] = greater
        self.current_permutation[greater_index] = current
        # reverse the order of the numbers to the right of the swapped value
        beg = current_index + 1
        end = perm_len
        while (end - beg) >= 1:
            tmp = self.current_permutation[beg]
            self.current_permutation[beg] = self.current_permutation[end]
            self.current_permutation[end] = tmp
            end -= 1
            beg += 1
        return False
    