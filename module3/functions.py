def is_one_to_one(domain, target, range):
    # create a list of all previously encountered y-values and return false if the same value is encountered twice
    prev = []
    for i in range:
        if i in prev:
            return False
        prev.append(i)
    return True

def is_onto(domain, target, range):
    # ensure every element in the target also appears in the range, making the function onto
    for i in target:
        if i not in range:
            return False
    return True

def is_bijection(domain, target, range):
    # return if the function is a bijection by ensuring that it is both one to one AND onto
    return is_onto(domain, target, range) and is_one_to_one(domain, target, range)

