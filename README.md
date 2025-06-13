# Analizador Léxico

Este proyecto corresponde al trabajo bimestral de la asignatura "Teoría de Autómatas y Compiladores". Consiste en un analizador léxico implementado en Python, capaz de identificar y clasificar los diferentes tokens presentes en un archivo de código fuente sencillo. El analizador reconoce palabras clave, identificadores, operadores, literales, comentarios y otros símbolos, mostrando el resultado por consola.

## Descripción del funcionamiento

- El archivo principal es `analizador_lexico.py`.
- Utiliza expresiones regulares para definir los patrones de los tokens.
- El conjunto de palabras clave reconocidas es:
  - `main`, `number`, `string`, `Boolean`, `True`, `False`, `for`, `while`, `if`, `else`, `echo`, `input`, `and`, `or`, `not`
- Los tipos de tokens reconocidos son:
  - **PALABRA_CLAVE**: Palabras reservadas del lenguaje.
  - **IDENTIFICADOR**: Nombres de variables o funciones (letra o guion bajo inicial, seguido de letras, dígitos o guion bajo).
  - **NUM_ENTERO** y **NUM_FLOTANTE**: Números enteros y flotantes.
  - **LITERAL_CADENA**: Cadenas entre comillas dobles.
  - **OPERADOR_DUP**: Operadores dobles como `++`, `--`, `==`, `!=`, `<=`, `>=`, `&&`, `||`.
  - **OPERADOR**: Operadores simples como `=`, `<`, `>`, `+`, `-`, `*`, `/`, `!`.
  - **LLAVE_ABRE**, **LLAVE_CIERRA**, **PAR_IZQ**, **PAR_DER**, **COMA**, **PUNTO_Y_COMA**: Símbolos de agrupación y puntuación.
  - **COMENTARIO_LINEA**: Comentarios de una línea que empiezan con `//`.
  - **ESPACIOS**: Espacios y saltos de línea (ignorados).
  - **SIMBOLO_DESCONOCIDO**: Cualquier otro carácter no esperado (marca error).
- El archivo de entrada de ejemplo es `base.txt`, que contiene código de prueba con todos los elementos anteriores.

## Instrucciones de uso

1. Asegúrate de tener Python instalado.
2. Coloca el archivo `analizador_lexico.py` y el archivo de código fuente a analizar (por ejemplo, `base.txt`) en el mismo directorio.
3. Ejecuta el analizador desde la terminal:

   ```sh
   python analizador_lexico.py base.txt
   ```

   Cambia `base.txt` por el nombre de tu archivo si es necesario.

4. El programa imprimirá una lista de tokens reconocidos, por ejemplo:

   ```
   Analizando archivo: 'base.txt'

   [OK] PALABRA_CLAVE      --> 'main'
   [OK] LLAVE_ABRE         --> '{'
   [OK] PALABRA_CLAVE      --> 'number'
   [OK] IDENTIFICADOR      --> 'contador'
   ...
   [ERROR] Símbolo inesperado: '@'
   ```

## Espacio para imagen



## Tabla de transición (basada en automata_final.jff)

| Estado Origen | Entrada      | Estado Destino | Descripción                       |
|-------------- |------------- |---------------|-----------------------------------|
| q0            | L            | q1            | Letra inicial de identificador    |
| q1            | L/N          | q1            | Letras o números en identificador |
| q0            | main symbols | q2/q3/q4/q5...| Agrupadores y operadores          |
| q0            | //           | q16           | Comentario de línea               |
| q16           | #n           | q16           | Comentario hasta salto de línea   |
| q0            | >, <, =, !   | q7            | Operadores relacionales           |
| q7            | =            | q8            | Operador doble (>=, <=, ==, !=)   |
| q0            | (            | q2            | Paréntesis de apertura            |
| q0            | )            | q2            | Paréntesis de cierre              |
| q0            | {            | q2            | Llave de apertura                 |
| q0            | }            | q2            | Llave de cierre                   |
| q0            | +, -         | q10           | Operadores aritméticos            |
| q0            | &            | q12           | Operador lógico AND               |
| q12           | &            | q13           | Operador lógico AND (&&)          |
| q0            | |            | q14           | Operador lógico OR                |
| q14           | |            | q15           | Operador lógico OR (||)           |
| q0            | números      | q3/q5         | Números enteros o flotantes       |
| q3            | .            | q6            | Punto decimal para flotante       |
| q6            | números      | q5            | Parte decimal de flotante         |
| q0            | "            | q4            | Inicio de literal de cadena       |
| q4            | cualquier    | q4            | Caracteres dentro de la cadena    |
| q4            | "            | q5            | Fin de literal de cadena          |
| ...           | ...          | ...           | ...                               |

> Nota: Esta tabla es un resumen interpretativo de las transiciones principales del autómata en automata_final.jff, adaptada a los tokens y símbolos que reconoce el analizador léxico.
