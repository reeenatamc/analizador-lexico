# Proyecto Bimestral – Teoría de Autómatas y Compiladores

Este repositorio contiene el proyecto bimestral para la asignatura **Teoría de Autómatas y Compiladores**. El proyecto consiste en la implementación de un autómata finito determinista (AFD) que reconoce construcciones básicas de un lenguaje de programación, como declaraciones de variables, asignaciones, estructuras de control (`if`, `while`), impresión de datos y comentarios.

---

## 📌 Características del AFD

Este autómata está diseñado para aceptar expresiones básicas del lenguaje, tales como:

* Declaración de variables: `var x: int;`
* Asignación de valores: `x = 5;`, `mensaje = "Hola";`
* Sentencias condicionales: `if(x==5)`
* Bucles: `while(x>0)`
* Impresión: `print(x)`
* Comentarios: `# esto es un comentario`

---

## 📄 Tabla de transición

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

---

## 🖼 Imagen del AFD (JFLAP)

![image](https://github.com/user-attachments/assets/360089c6-9519-49f3-b3ce-8338523ded68)


---

## 🛠 Tecnologías utilizadas

* JFLAP (para el diseño del autómata)
* XML (estructura del autómata)
* Git & GitHub (control de versiones)

---

## ✅ Estado del proyecto

✔ Proyecto completado y probado correctamente en JFLAP.

---
