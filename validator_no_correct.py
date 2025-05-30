from analizador_lexico import lexer

def test_incorrect_code():
    # Casos de prueba con código incorrecto
    test_cases = [
        {
            "name": "Carácter no válido (@)",
            "code": "var x@: int;"
        },
        {
            "name": "Número inválido en identificador",
            "code": "var 123var: string;"
        },
        {
            "name": "String sin cerrar",
            "code": 'var texto: string = "Hola mundo;'
        },
        {
            "name": "Operador no válido",
            "code": "var x: int = 5 $ 3;"
        },
        {
            "name": "Comentario mal formado",
            "code": "#Este es un comentario mal formado\nvar x: int;"
        }
    ]

    print("=== Pruebas de código incorrecto ===\n")
    
    for test in test_cases:
        print(f"\nPrueba: {test['name']}")
        print(f"Código: {test['code']}")
        try:
            tokens = lexer(test['code'])
            print("Tokens encontrados:")
            for token in tokens:
                print(token)
        except SyntaxError as e:
            print(f"Error de sintaxis: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
        print("-" * 50)

if __name__ == "__main__":
    test_incorrect_code()
