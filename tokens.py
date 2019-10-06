################################
## MINIJAVA LEXICAL TOKEN
################################


# Constants
LOWERCASELETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASECASELETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"

KEYWORDS = {
    "private": "T#PRIVATE",
    "public":  "T#PUBLIC",
    "static":  "T#STATIC",
    "new":     "T#NEW",
    "boolean": "T#TYPE_BOOLEAN",
    "int":     "T#TYPE_INTEGER",
    "true":    "T#TRUE",
    "false":   "T#FALSE",
    "if":      "T#IF",
    "else":    "T#ELSE",
    "while":   "T#WHILE",
    "for":   "T#FOR",
    "return":  "T#RETURN",
    "void":    "T#VOID",
    "null":    "T#NULL",
    "this":    "T#THIS",
    "class":   "T#CLASS"
}

PUNCTUATION = {
    ".": "T#DOT",
    ",": "T#COMMA",
    ";": "T#DOT_COMMA",
    "(": "T#LEFT_PARENTHESIS",
    ")": "T#RIGHT_PARENTHESIS",
    "[": "T#LEFT_SQUARE_BRACKET",
    "]": "T#RIGHT_SQUARE_BRACKET",
    "{": "T#LEFT_BRACKET",
    "}": "T#RIGHT_BRACKET"
}

ARITHMETIC_OPERATORS = {
    "+": "T#SUM",
    # [INCODE]: "T#SUBTRACTION",
    "*": "T#MULTIPLICATION"
    # [INCODE]: "T#DIVISION"
}

# RELATIONAL OPERATORS
# [INCODE]: "T#GREATERTHAN"
# [INCODE]: "T#LESSERTHAN"
# [INCODE]: "T#EQUALS"
# [INCODE]: "T#NOTEQUALS"
# [INCODE]: "T#GREATEREQUALS"
# [INCODE]: "T#LESSEREQUALS"
# [INCODE]: "T#AND"
# [INCODE]: "T#OR"
# [INCODE]: "T#NOT"

# GENERAL
# [INCODE]: "T#SPACE"
# [INCODE]: "T#TAB"
# [INCODE]: "T#NEWLINE"
# [INCODE]: "T#POSITIVE_INTEGER"
# [INCODE]: "T#POSITIVE_FLOAT"
# [INCODE]: "T#NEGATIVE_INTEGER"
# [INCODE]: "T#NEGATIVE_FLOAT"
# [INCODE]: "T#IDENTIFIER"
# [INCODE]: "T#ATTRIBUTION"
# [INCODE]: "T#ERROR"

class Token(object):
    def __init__(self, p_type, p_lexem, p_line, p_column):
        self.type = p_type
        self.lexem = p_lexem
        self.line = p_line
        self.column = p_column