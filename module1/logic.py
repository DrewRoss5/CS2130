def conjunction(p, q):
    if p == q == 'T':
        return 'T'
    return 'F'


def disjunction(p, q):
    if 'T' in (p, q):
        return 'T'
    return 'F'

def negation(p):
    return {'T': 'F', 'F': 'T'}[p]

def conditional(p, q):
    if p == 'T':
        return 'T' if p == q else 'F'
    return 'T'

def biconditional(p, q):
    if p == q:
        return 'T'
    return 'F'

def proposition1(p, q, r):
    return conjunction(negation(conjunction(p, q)), disjunction(r, q))


def proposition2(p, q, r):
    return disjunction(conditional(q, r), conjunction(negation(p), r))


def proposition3(p, q, r):
    return biconditional(conjunction(r, q), negation(disjunction(p, r)))

