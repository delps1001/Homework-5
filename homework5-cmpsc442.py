############################################################
# CMPSC442: Homework 5
############################################################

student_name = "Dalton DelPiano"

############################################################
# Imports
############################################################


############################################################
# Section 1: Propositional Logic
############################################################
class Expr(object):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))


class Atom(Expr):
    def __init__(self, name):
        self.name = name
        self.hashable = name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __repr__(self):
        return "Atom(" + str(self.name) + ")"

    def atom_names(self):
        return set([self.name])

    def evaluate(self, assignment):
        pass

    def to_cnf(self):
        return self


class Not(Expr):
    def __init__(self, arg):
        self.arg = arg
        self.hashable = arg

    def __eq__(self, other):
        if self.arg == other.arg:
            return True
        return False

    def __repr__(self):
        return "Not(" + repr(self.arg) + ")"

    def atom_names(self):
        return self.arg.atom_names()

    def evaluate(self, assignment):
        pass

    def to_cnf(self):
        temp_list = []
        # First case ~(a v b) === ~a ^ ~b
        cnf = self.arg.to_cnf()
        if isinstance(cnf, Or):
            for y in cnf.hashable:
                temp_list.append(Not(y).to_cnf())
            return And(*temp_list).to_cnf()
        elif isinstance(cnf, And):
            for y in cnf.hashable:
                temp_list.append(Not(y).to_cnf())
            return Or(*temp_list).to_cnf()
        elif isinstance(cnf, Not):
            return self.arg.arg
        elif isinstance(cnf, Atom):
            return self



class And(Expr):
    def __init__(self, *conjuncts):
        self.conjuncts = frozenset(conjuncts)
        self.hashable = self.conjuncts

    def __eq__(self, other):
        if self.conjuncts == other.conjuncts:
            return True
        return False

    def __repr__(self):
        string = "And("
        for x in self.hashable:
            string += repr(x) + ", "
        string = string[:-2]
        string += ")"
        return string

    def atom_names(self):
        atom_name = set()
        for x in self.conjuncts:
                atom_name = atom_name.union(x.atom_names())
        return atom_name

    def evaluate(self, assignment):
        pass

    def to_cnf(self):
        temp_list = []
        return_list = []
        for x in self.hashable:
            temp_list.append(x.to_cnf())
        for y in temp_list:
            if isinstance(y, And):
                for z in y.hashable:
                    return_list.append(z)
            else:
                return_list.append(y)
        return And(*return_list)


class Or(Expr):
    def __init__(self, *disjuncts):
        self.disjuncts = frozenset(disjuncts)
        self.hashable = self.disjuncts

    def __eq__(self, other):
        if self.disjuncts == other.disjuncts:
            return True
        return False

    def __repr__(self):
        string = "Or("
        for x in self.hashable:
            string += repr(x) + ", "
        string = string[:-2]
        string += ")"
        return string

    def atom_names(self):
        atom_name = set()
        for x in self.disjuncts:
                atom_name = atom_name.union(x.atom_names())
        return atom_name

    def evaluate(self, assignment):
        pass

    def to_cnf(self):
        pass

class Implies(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.hashable = (left, right)

    def __eq__(self, other):
        if self.hashable == other.hashable:
            return True
        return False

    def __repr__(self):
        return "Implies(" + repr(self.left) + ", " + repr(self.right) + ")"

    def atom_names(self):
        return self.left.atom_names().union(self.right.atom_names())

    def evaluate(self, assignment):
        pass

    def to_cnf(self):
        return Or(Not(self.left), self.right).to_cnf()

class Iff(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.hashable = (left, right)

    def __eq__(self, other):
        if self.hashable[0] in other.hashable and self.hashable[1] in other.hashable:
            return True
        return False

    def __repr__(self):
        return "Iff(" + repr(self.left) + ", " + repr(self.right) + ")"

    def atom_names(self):
        return self.left.atom_names().union(self.right.atom_names())
    def evaluate(self, assignment):
        pass
    def to_cnf(self):
            return And(Or(Not(self.left), self.right), Or(Not(self.right), self.left)).to_cnf()

def satisfying_assignments(expr):
    pass

class KnowledgeBase(object):
    def __init__(self):
        pass
    def get_facts(self):
        pass
    def tell(self, expr):
        pass
    def ask(self, expr):
        pass


a, b, c = map(Atom, "abc")
print And(a, And(b, c)).to_cnf()



############################################################
# Section 2: Logic Puzzles
############################################################

# Puzzle 1

# Populate the knowledge base using statements of the form kb1.tell(...)
kb1 = KnowledgeBase()

# Write an Expr for each query that should be asked of the knowledge base
mythical_query = None
magical_query = None
horned_query = None

# Record your answers as True or False; if you wish to use the above queries,
# they should not be run when this file is loaded
is_mythical = None
is_magical = None
is_horned = None

# Puzzle 2

# Write an Expr of the form And(...) encoding the constraints
party_constraints = None

# Compute a list of the valid attendance scenarios using a call to
# satisfying_assignments(expr)
valid_scenarios = None

# Write your answer to the question in the assignment
puzzle_2_question = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

# Puzzle 3

# Populate the knowledge base using statements of the form kb3.tell(...)
kb3 = KnowledgeBase()

# Write your answer to the question in the assignment; the queries you make
# should not be run when this file is loaded
puzzle_3_question = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

# Puzzle 4

# Populate the knowledge base using statements of the form kb4.tell(...)
kb4 = KnowledgeBase()

# Uncomment the line corresponding to the guilty suspect
# guilty_suspect = "Adams"
# guilty_suspect = "Brown"
# guilty_suspect = "Clark"

# Describe the queries you made to ascertain your findings
puzzle_4_question = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
