import re

# Palabras clave
KEYWORDS = {"var", "int", "string", "bool", "if", "while", "print", "true", "false"}

# Tokens y patrones
token_specs = [
    ("COMMENT", r"#.*"),                        # Comentario
    ("VAR", r"var"),                            # var
    ("TYPE", r"(int|string|bool)"),             # Tipos
    ("BOOL", r"(true|false)"),                  # Booleanos
    ("NUMBER", r"\d+"),                         # Números
    ("ID", r"[a-zA-Z_][a-zA-Z_0-9]*"),          # Identificadores
    ("ASSIGN", r"="),                           # Asignación
    ("SEMICOLON", r";"),                        # ;
    ("COLON", r":"),                            # :
    ("LPAREN", r"\("),                          # (
    ("RPAREN", r"\)"),                          # )
    ("LBRACE", r"\{"),                          # {
    ("RBRACE", r"\}"),                          # }
    ("STRING", r'"[^"]*"'),                     # Cadenas
    ("OP", r"[+\-*/]"),                         # Operadores aritméticos
    ("CMP", r"(==|!=|<=|>=|<|>)"),              # Comparadores
    ("NEWLINE", r"\n"),                         # Fin de línea
    ("SKIP", r"[ \t]+"),                        # Espacios
    ("MISMATCH", r"."),                         # Cualquier otro carácter
]

# Compilar los patrones
tok_regex = "|".join("(?P<%s>%s)" % pair for pair in token_specs)
get_token = re.compile(tok_regex).match


def lexer(code):
    line_num = 1
    pos = 0
    tokens = []

    while pos < len(code):
        match = get_token(code, pos)
        if not match:
            raise SyntaxError(f"Carácter inesperado en la posición {pos}")
        typ = match.lastgroup
        lexeme = match.group(typ)

        if typ == "NEWLINE":
            line_num += 1
        elif typ == "SKIP" or typ == "COMMENT":
            pass
        elif typ == "MISMATCH":
            raise SyntaxError(f"Token inválido '{lexeme}' en la línea {line_num}")
        else:
            tokens.append((typ, lexeme, line_num))

        pos = match.end()
    return tokens

codigo_correcto = '''
# njbpc rup
# ajhik zmtbot
var ubkmqoyf: bool;
var thf: string;
var ohp: int;
ubkmqoyf = true;
thf = fdi;
ohp = 27;
if (33 <= "trhwx") {
    print(false);
    myirccie = 49;
    # vsd dlwfeb ysyey
}
while (26 > 47) {
    print(true);
    iirj = false;
    # ygmlczbc tuept wngnrva ykw
}
'''

tokens = lexer(codigo_correcto)
for t in tokens:
    print(t)

