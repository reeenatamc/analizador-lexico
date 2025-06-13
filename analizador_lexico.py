import re
import sys

# 1) Conjunto de palabras clave (actualizado para incluir todas las palabras clave del lenguaje)
PALABRAS_CLAVE = {
    "main", "number", "string", "Boolean", "True", "False",
    "for", "while", "if", "else", "echo", "input",
    "and", "or", "not"
}

# 2) Definición de patrones para tokens
patrones_tokens = [
    # Comentarios de una línea que empiezan con //
    ('COMENTARIO_LINEA', r'//.*'),

    # Palabras clave
    ('PALABRA_CLAVE',  r'\b(?:' + '|'.join(PALABRAS_CLAVE) + r')\b'),

    # Operadores aritméticos y lógicos dobles
    ('OPERADOR_DUP', r'\+\+|--|==|!=|<=|>=|&&|\|\|'),

    # Operadores simples
    ('OPERADOR', r'[=<>+\-*/!]'),

    # Literales de cadena con comillas dobles
    ('LITERAL_CADENA', r'"[^"\n]*"'),

    # Números flotantes con o sin parte entera
    ('NUM_FLOTANTE', r'(\d+\.\d*|\.\d+)'),

    # Números enteros
    ('NUM_ENTERO', r'\d+'),

    # Paréntesis y llaves y puntuación
    ('LLAVE_ABRE', r'\{'),
    ('LLAVE_CIERRA', r'\}'),
    ('PAR_IZQ', r'\('),
    ('PAR_DER', r'\)'),
    ('COMA', r','),
    ('PUNTO_Y_COMA', r';'),

    # Identificadores: letra inicial, seguido de letras, dígitos o guion bajo
    ('IDENTIFICADOR', r'[A-Za-z_][A-Za-z0-9_]*'),

    # Espacios y tabs que se ignoran
    ('ESPACIOS', r'\s+'),

    # Cualquier otro carácter no esperado
    ('SIMBOLO_DESCONOCIDO', r'.'),
]

# 3) Compilar patrón maestro (en diferente orden, distinto método)
patron_general = re.compile(
    '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones_tokens),
    re.UNICODE
)

def procesar_codigo(codigo):
    tokens_encontrados = False
    for coincidencia in patron_general.finditer(codigo):
        tipo_token = coincidencia.lastgroup
        valor_token = coincidencia.group()

        # Ignorar espacios y comentarios
        if tipo_token in ('ESPACIOS', 'COMENTARIO_LINEA'):
            continue

        tokens_encontrados = True
        if tipo_token == 'SIMBOLO_DESCONOCIDO':
            print(f"[ERROR] Símbolo inesperado: {valor_token!r}")
        else:
            print(f"[OK] {tipo_token:<18} --> {valor_token!r}")
    if not tokens_encontrados:
        print("[DEBUG] No se encontraron tokens en el código.")

def analizar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, encoding='utf-8') as f:
            contenido = f.read()
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no fue encontrado.")
        return

    print(f"Analizando archivo: '{ruta_archivo}'\n")
    procesar_codigo(contenido)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python analizador_lexico.py <archivo_de_codigo.txt>")
    else:
        analizar_archivo(sys.argv[1])



