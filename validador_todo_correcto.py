from analizador_lexico import lexer

def main():
    try:
        # Leer el archivo base.txt
        with open('base.txt', 'r', encoding='utf-8') as file:
            codigo = file.read()
        
        # Analizar el código
        tokens = lexer(codigo)
        
        # Imprimir los tokens
        print("Tokens encontrados:")
        for token in tokens:
            print(token)
            
    except FileNotFoundError:
        print("Error: No se encontró el archivo base.txt")
    except Exception as e:
        print(f"Error durante el análisis: {str(e)}")

if __name__ == "__main__":
    main()
