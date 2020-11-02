def lexer(string:str):
    code = []
    for char in string:
        if ord(char) == 9:
            code.append("\t")
        elif ord(char) == 10:
            code.append("\n")
        elif ord(char) == 32:
            code.append(" ")
        elif ord(char) == 33:
            code.append(("OPR", "NOT"))
        elif ord(char) == 34:
            code.append(("CTL", "DQT")) #Double quotes
        elif ord(char) == 35:
            code.append(("CTL", "CMT")) #Comments
        elif ord(char) == 36:
            code.append(("OPR", "ASN")) #Assignment
        elif ord(char) == 37:
            code.append(("OPR", "MOD"))
        elif ord(char) == 38:
            code.append(("OPR", "AND"))
        elif ord(char) == 39:
            code.append(("CTL", "SQT")) #Single quotes
        elif ord(char) == 40:
            code.append(("CTL", "LPN")) #left parens
        elif ord(char) == 41:
            code.append(("CTL", "RPN")) #right parens
        elif ord(char) == 42:
            code.append(("OPR", "MUL"))
        elif ord(char) == 43:
            code.append(("OPR", "ADD"))
        elif ord(char) == 44:
            code.append(("CTL", "CMA")) #Comma
        elif ord(char) == 45:
            code.append(("OPR", "SUB"))
        elif ord(char) == 46:
            code.append(("CTL", "DOT"))
        elif ord(char) == 47:
            code.append(("OPR", "DIV"))
        elif 48 <= ord(char) <= 57:
            code.append(("NUM", str(char))) #Numbers
        elif ord(char) == 58:
            code.append(("CTL", "CLN")) #Colon
        elif ord(char) == 59:
            code.append(("CTL", "SCN")) #Semicolon
        elif ord(char) == 60:
            code.append(("OPR", "LST")) #Less than
        elif ord(char) == 61:
            code.append(("OPR", "EQU")) #Equal to
        elif ord(char) == 62:
            code.append(("OPR", "GRT")) #Greater than
        elif ord(char) == 63:
            code.append(("OPR", "CND")) #Terternary conditional
        elif ord(char) == 64:
            code.append(("CTL", "MDL")) #@ would be used for module imports
        elif 65 <= ord(char) <= 90:
            code.append(("CHR", str(char))) #capital letters
        elif ord(char) == 91:
            code.append(("CTL", "LBK")) #left brackets
        elif ord(char) == 92:
            code.append(("CTL", "BSL")) #backslash
        elif ord(char) == 93:
            code.append(("CTL", "RBK")) #right brackets
        elif ord(char) == 94:
            code.append(("OPR", "EXP")) #exponetation
        elif ord(char) == 95 or ord(char) == 96:
            code.append(("CHR", str(char))) #_ and `
        elif 97 <= ord(char) <= 122:
            code.append(("CHR", str(char))) #lowercase letters
        elif ord(char) == 123:
            code.append(("CTL", "LBC")) #Left braces
        elif ord(char) == 124:
            code.append(("OPR", "IOR")) #inclusive OR
        elif ord(char) == 125:
            code.append(("CTL", "RBC")) #right braces
        elif ord(char) == 126:
            code.append(("OPR", "XOR")) #~ is the XOR operator
        else:
            code.append("NUL")
    return code      


def parse(code:list):
    pass


def transpile(code:list):
    pass