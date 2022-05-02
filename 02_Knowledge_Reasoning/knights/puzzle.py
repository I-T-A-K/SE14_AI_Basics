from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
## Puzzle-specific sentence
sentence = And(AKnight, AKnave)

knowledge0 = And(
    ## General knowledge
    # Each person is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # No person can be both - not knight and knave at the same time
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    ## Puzzle-specific knowledge
    # If the person is a knight, then the senctence is true, else it is false
    # otherwise if A is a knave, the sentence is not true and than A can not be a knight
    Biconditional(AKnight, sentence)
        ## First I had the below, but it is shorter and better readable just using a biconditional
        # Implication(AKnight, sentence)
        # Implication(AKnave, Not(sentence))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

## Puzzle-specific sentence
sentenceA = And(AKnave, BKnave)

knowledge1 = And(
    ## General knowledge 
    # Each person is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # No person can be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    ## Puzzle-specific knowledge
    # If the person is a knight, then the senctence is true, else it is false and A is not a knight 
    Biconditional(AKnight, sentenceA)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

## Puzzle-specific sentences
# SentenceA either we are both knaves or both knights
sentenceA = Or(And(AKnave, BKnave), And(AKnight, BKnight))
# SenctenceB either we are knight and knave or knave and knight 
sentenceB = Or(And(AKnight,BKnave), And(BKnight, AKnave))

knowledge2 = And(
    ## General knowledge
    # Each person is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # No person can be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    ## Puzzle-specific knowledge
    # If the person is a knight, then the senctence is true, else it is false and A is not a knight 
    Biconditional(AKnight, sentenceA),
    Biconditional(BKnight, sentenceB)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

## Puzzle-specific sentences
sentenceA = Biconditional(AKnight, Not(AKnave))
# A and C is a knave
sentenceB = And(AKnave, CKnave)
sentenceC = AKnight

knowledge3 = And(
    ## General knowledge
    # Each person is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # No person can be both
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    ## Puzzle-specific knowledge
    # A said either or but we do not know
    Biconditional(AKnight, sentenceA),
    # If A said he is a knave and C is a knave
    Biconditional(BKnight, sentenceB),
    # A is a knight
    Biconditional(CKnight, sentenceC)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
