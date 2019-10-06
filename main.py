################################
## MINIJAVA LEXICAL ANALYSIS
################################


# Native Modules
import os, sys
# Downloaded Modules

# Custom Modules
from lexicalanalyzer import LexicalAnalyzer


if(__name__ == "__main__"):
    if(len(sys.argv) == 2):
        if(os.path.isfile(sys.argv[1])):
            lex = LexicalAnalyzer(sys.argv[1])

            print("Número de tokens: " + str(len(lex.tokens)))
            
            for token in lex.tokens:
                if(token.type != "T#ERROR"):
                    print("Encontrado o token \"{0}\" com lexema \"{1}\" na linha {2} coluna {3}".format(token.type, token.lexem, token.line, token.column))
                else:
                    print("Encontrado o token inválido \"{0}\" na linha {1} coluna {2}".format(token.lexem, token.line, token.column), end="<ERROR>\n")
        else:
            print("O arquivo \"{0}\" não é um arquivo válido ou não existe.".format(sys.argv[1]))
    else:
        print("Argumentos inválidos!")
        print("Modo de uso: python lexicalanalyzer.py <nome_do_arquivo_a_ser_analisado>")