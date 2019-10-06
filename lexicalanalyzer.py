################################
## MINIJAVA LEXICAL ANALYZER
################################


# Native Modules

# Downloaded Modules

# Custom Modules
from tokens import LOWERCASELETTERS, UPPERCASECASELETTERS, DIGITS
from tokens import ARITHMETIC_OPERATORS, KEYWORDS, PUNCTUATION
from tokens import Token


class LexicalAnalyzer(object):
    def __init__(self, p_filename):
        self.filename = p_filename
        self.line = 1
        self.column = 1
        self.tokens = []

        f = open(self.filename)
        while True:
            char = f.read(1)
            if(char):
                # recognizes and handles spaces
                if(char == " "):
                    self.column += 1

                # recognizes and handles tabs
                elif(char == "\t"):
                    self.column += 1

                # recognizes and handles newlines
                elif(char in "\n"):
                    self.line += 1
                    self.column = 1

                # recognizes and handles singleline comments and division "/"
                elif(char == "/"):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar == "/"):
                        self.column += 2
                        while char not in "\n":
                            char = f.read(1)
                            self.column += 1
                        if(char == "\n"):
                            self.column = 1
                            self.line += 1
                    else:
                        _type = "T#DIVISION"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1
                        f.seek(last_column)

                # recognizes and handles positive numbers (integers and decimals)
                elif(char in DIGITS):
                    number = char
                    last_column = f.tell()
                    char = f.read(1)
                    while char in DIGITS + ".":
                        number += char
                        last_column = f.tell()
                        char = f.read(1)
                    if(number.count(".") > 1):
                        raise SyntaxError("O número '{0}' é inválido.".format(number))
                    f.seek(last_column)
                    if("." in number):
                        _type = "T#POSITIVE_FLOAT"
                    else:
                        _type = "T#POSITIVE_INTEGER"
                    self.tokens.append(Token(_type, number, self.line, self.column))
                    self.column += len(number)

                # recognizes and handles negative numbers and subtractions
                elif(char == "-"):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar in DIGITS + "."):
                        # char is a '-' and next char is digit
                        number = char
                        while nextchar != " ":
                            number += nextchar
                            last_column = f.tell()
                            nextchar = f.read(1)
                        if(number.count(".") > 1):
                            raise SyntaxError("O número '{0}' é inválido.".format(number))
                        f.seek(last_column)
                        if("." in number):
                            _type = "T#NEGATIVE_FLOAT"
                        else:
                            _type = "T#NEGATIVE_INTEGER"
                        self.tokens.append(Token(_type, number, self.line, self.column))
                        self.column += len(number)
                    else:
                        # char is a '-' and next char is space
                        _type = "T#SUBTRACTION"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1

                # recognizes and handles keywords/identifiers
                elif(char in LOWERCASELETTERS + UPPERCASECASELETTERS + "_"):
                    word = char
                    last_column = f.tell()
                    char = f.read(1)
                    while char in LOWERCASELETTERS + UPPERCASECASELETTERS + "_" + DIGITS:
                        word += char
                        last_column = f.tell()
                        char = f.read(1)
                    f.seek(last_column)
                    if(word in KEYWORDS.keys()):
                        _type = KEYWORDS[word]
                    else:
                        _type = "T#IDENTIFIER"
                    self.tokens.append(Token(_type, word, self.line, self.column))
                    self.column += len(word)

                # recognizes and handles "=" and "=="
                elif(char == "="):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar == "="):
                        _type = "T#EQUALS"
                        char += nextchar
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 2
                    else:
                        _type = "T#ATTRIBUTION"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1
                        f.seek(last_column)

                # recognizes and handles "!" and "!="
                elif(char == "!"):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar == "="):
                        _type = "T#NOT_EQUALS"
                        char += nextchar
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 2
                    else:
                        _type = "T#NOT"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1
                        f.seek(last_column)

                # recognizes and handles ">" and ">="
                elif(char == ">"):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar == "="):
                        _type = "T#GREATER_EQUALS"
                        char += nextchar
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 2
                    else:
                        _type = "T#GREATER_THAN"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1
                        f.seek(last_column)

                # recognizes and handles "<" and "<="
                elif(char == "<"):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar == "="):
                        _type = "T#LESSER_EQUALS"
                        char += nextchar
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 2
                    else:
                        _type = "T#LESSER_THAN"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1
                        f.seek(last_column)

                # recognizes and handles "&&"
                elif(char == "&"):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar == "&"):
                        _type = "T#AND"
                        char += nextchar
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 2
                    else:
                        _type = "T#ERROR"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1
                        f.seek(last_column)

                # recognizes and handles "||"
                elif(char == "|"):
                    last_column = f.tell()
                    nextchar = f.read(1)
                    if(nextchar == "|"):
                        _type = "T#OR"
                        char += nextchar
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 2
                    else:
                        _type = "T#ERROR"
                        self.tokens.append(Token(_type, char, self.line, self.column))
                        self.column += 1
                        f.seek(last_column)

                # recognizes and handles punctuation
                elif(char in PUNCTUATION.keys()):
                    _type = PUNCTUATION[char]
                    self.tokens.append(Token(_type, char, self.line, self.column))
                    self.column += 1

                # recognizes and handles arithmetic operators
                elif(char in ARITHMETIC_OPERATORS.keys()):
                    _type = ARITHMETIC_OPERATORS[char]
                    self.tokens.append(Token(_type, char, self.line, self.column))
                    self.column += 1

                else:
                    _type = "T#ERROR"
                    self.tokens.append(Token(_type, char, self.line, self.column))
                    self.column += 1

            else:
                # END OF FILE
                f.close()
                break