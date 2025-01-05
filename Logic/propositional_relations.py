from truthtable import *

# Syntax of expressions should be written as specified in main() of "truthtable.py"

def is_equivalent(expression_1, expression_2) -> bool:
    """Checks if two propositions has same truthvalues."""
    compound = f"({expression_1}) bimp ({expression_2})"
    return all(generate_truthtable(compound)[3])

def is_tautology(expression) -> bool:
    """Checks if a proposition always is True."""
    truthtable = generate_truthtable(expression)
    outputs = truthtable[3]
    return all(outputs)

def is_contingency(expression) -> bool:
    """Checks if a proposition sometimes is True
    and sometimes is False.
    """
    truthtable = generate_truthtable(expression)
    outputs = truthtable[3]
    return any(outputs) and not all(outputs)

def is_contradiction(expression) -> bool:
    """Checks if a proposition always is False"""
    truthtable = generate_truthtable(expression)
    outputs = truthtable[3]
    return not any(outputs)
