example_relation = {('a','b'),('a','c'),('b','a')}
example_set = {'a','b','c','d'}

def is_equivalence(relation: set[tuple[str]], input_set: set[str]):
    return (is_reflexive(relation, input_set) and
            is_transitive(relation) and
            is_symmetric(relation)
            )

def is_total_order(relation: set[tuple[str]], input_set: set[str]):
    n = len(input_set)
    return (is_partial_order(relation, input_set) and
            len(relation) == n*(n+1)/2
            )

def is_partial_order(relation, input_set: set[str]):
    return (is_reflexive(relation, input_set) and
            is_transitive(relation) and
            is_antisymmetric(relation)
            )


def is_reflexive(relation: set[tuple[str]], input_set: set[str]):
    for element in input_set:
        if (element, element) not in relation:
            print(element, element)
            return False
    return True

def is_symmetric(relation: set[tuple[str]]):
    for pair in relation:
        if (pair[1],pair[0]) not in relation:
            return False
    return True

def is_antisymmetric(relation: set[tuple[str]]):
    for pair in relation:
        if pair[0] != pair[1] and (pair[1],pair[0]) in relation:
            return False
    return True

def is_transitive(relation: set[tuple[str]]):
    for pair_a in relation:
        for pair_b in relation:
            if (pair_b[0] == pair_a[1] and
                (pair_a[0], pair_b[1]) not in relation
                ):
                    return False
    return True


def reflexive_closure(relation: set[tuple[str]], input_set: set[str]):
    closed_relation = {pair for pair in relation}
    for var in input_set:
        closed_relation.add((var, var))
    return closed_relation

def symmetric_closure(relation: set[tuple[str]]):
    closed_relation = {pair for pair in relation}
    for pair in relation:
        closed_relation.add((pair[1], pair[0]))
    return closed_relation

def transitive_closure(relation: set[tuple[str]]):
    closed_relation = {pair for pair in relation}
    for pair_a in relation:
        for pair_b in relation:
            if pair_b[0] == pair_a[1] and pair_a[0] != pair_a[1]:
                closed_relation.add((pair_a[0], pair_b[1]))
    if is_transitive(closed_relation):
        return closed_relation
    else:
        return transitive_closure(closed_relation)

def power_relation(relation: set[tuple[str]], exponent):
    """Returns the power of a relation.
    Input '*' as a string for kleene star exponent. 
    """
    if exponent == 1:
        return relation
    elif exponent == '*':
        kleene_result = set()
        _kleene_star(kleene_result, relation)
        return kleene_result
    else:
        return _relation_product(relation, power_relation(relation, exponent-1))

# Aux functions for power_relation

def _kleene_star(result: set, relation: set[tuple[str]], exponent: int = 0):
    """Adds the relation pairs of all power relations to result"""
    if exponent == 0:
        [result.add((pair[0], pair[0])) for pair in relation]
        _kleene_star(result, relation, exponent + 1)
    elif not all([pair in result for pair in relation]):
        [result.add(pair) for pair in relation]
        _kleene_star(result, power_relation(relation, exponent + 1))

def _relation_product(relation1: set[tuple[str]], relation2: set[tuple[str]]):
    closed_relation = set()
    for pair_a in relation1:
        for pair_b in relation2:
            if pair_b[0] == pair_a[1]:
                closed_relation.add((pair_a[0], pair_b[1]))
    return closed_relation
