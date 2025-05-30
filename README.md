# Analizador Léxico

Este proyecto implementa un analizador léxico para un lenguaje de programación simple, capaz de identificar y clasificar tokens en el código fuente.

## Características

- Reconocimiento de tokens básicos de programación
- Manejo de comentarios
- Detección de errores léxicos
- Soporte para tipos de datos básicos (int, string, bool)
- Validación de sintaxis

## Estructura del Proyecto

- `analizador_lexico.py`: Implementación principal del analizador léxico
- `validador_todo_correcto.py`: Validador para código sintácticamente correcto
- `validador_no_correcto.py`: Validador para casos de prueba con código incorrecto
- `base.txt`: Archivo de ejemplo con código para analizar
- `FINAL/`: Carpeta con la versión final del proyecto
  - `validador.py`: Validador mejorado que analiza línea por línea
  - `codigo_mixto.txt`: Archivo de prueba con ejemplos de código correcto e incorrecto

## Tabla de Transición

| Estado Origen | Entrada                     | Estado Destino | Descripción                       |
| ------------- | --------------------------- | -------------- | --------------------------------- |
| q0            | `var`                       | q1             | Inicio de declaración de variable |
| q1            | `letter`                    | q2             | Nombre de variable                |
| q2            | `letter`                    | q2             | Letras adicionales                |
| q2            | `digit`                     | q2             | Dígitos del identificador         |
| q2            | `:`                         | q3             | Separador de tipo                 |
| q3            | `int`                       | q4             | Tipo de dato: entero              |
| q3            | `string`                    | q4             | Tipo de dato: cadena              |
| q3            | `bool`                      | q4             | Tipo de dato: booleano            |
| q4            | `;`                         | q5             | Fin de declaración                |
| q0            | `letter`                    | q6             | Inicio de asignación              |
| q6            | `letter`                    | q6             | Letras del identificador          |
| q6            | `digit`                     | q6             | Dígitos del identificador         |
| q6            | `=`                         | q7             | Asignación                        |
| q7            | `digit`                     | q8             | Valor numérico                    |
| q7            | `letter`                    | q8             | Identificador como valor          |
| q7            | `"`                         | q8             | Inicio de cadena                  |
| q8            | `letter`                    | q8             | Letras dentro de valor            |
| q8            | `digit`                     | q8             | Dígitos dentro de valor           |
| q8            | `;`                         | q5             | Fin de asignación                 |
| q0            | `if`                        | q9             | Inicio de condición               |
| q0            | `while`                     | q9             | Inicio de bucle                   |
| q0            | `print`                     | q9             | Inicio de impresión               |
| q0            | `#`                         | q9             | Inicio de comentario              |
| q9            | `(`                         | q10            | Inicio de condición               |
| q10           | `letter`                    | q10            | Variables en condición            |
| q10           | `digit`                     | q10            | Constantes en condición           |
| q10           | `==` `!=` `<` `>` `<=` `>=` | q10            | Operadores relacionales           |
| q10           | `)`                         | q5             | Fin de condición                  |
| q9            | `letter`                    | q9             | Comentario: letras                |
| q9            | `digit`                     | q9             | Comentario: dígitos               |
| q9            | `space`                     | q9             | Comentario: espacio               |
| q9            | `newline`                   | q5             | Fin de comentario                 |
| q8            | `+ - * /`                   | q8             | Operadores aritméticos            |

## Tokens Soportados

El analizador reconoce los siguientes tipos de tokens:

- Palabras clave: `var`, `int`, `string`, `bool`, `if`, `while`, `print`, `true`, `false`
- Identificadores: Nombres de variables
- Números: Valores enteros
- Strings: Texto entre comillas dobles
- Operadores: `+`, `-`, `*`, `/`
- Comparadores: `==`, `!=`, `<=`, `>=`, `<`, `>`
- Símbolos especiales: `=`, `;`, `:`, `(`, `)`, `{`, `}`
- Comentarios: Líneas que comienzan con `#`

## Uso

1. Para analizar código correcto:
```bash
python validador_todo_correcto.py
```

2. Para probar casos de código incorrecto:
```bash
python validador_no_correcto.py
```

3. Para usar el validador final (versión mejorada):
```bash
cd FINAL
python validador.py
```

## Ejemplo de Código Válido

```python
# Declaración de variables
var x: int;
var texto: string;
var activo: bool;

# Asignaciones
x = 42;
texto = "Hola mundo";
activo = true;

# Estructuras de control
if (x > 10) {
    print(true);
}
```

## Ejemplos de Código Incorrecto

El archivo `FINAL/codigo_mixto.txt` contiene ejemplos de código correcto e incorrecto:

```python
# Código correcto
var edad: int;              # ✅ Válido: declaración correcta
var nombre: string;         # ✅ Válido: declaración correcta
edad = 25;                  # ✅ Válido: asignación correcta

# Código incorrecto
var 123edad: int;           # ❌ Inválido: identificador comienza con número
var nombre@: string;        # ❌ Inválido: carácter no válido
edad = "25";                # ❌ Inválido: tipo incorrecto
```

## Manejo de Errores

El analizador detecta y reporta los siguientes tipos de errores:
- Caracteres no válidos
- Identificadores mal formados
- Strings sin cerrar
- Operadores no válidos
- Comentarios mal formados

## Requisitos

- Python
- No se requieren dependencias externas

---
