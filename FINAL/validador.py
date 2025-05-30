import os
import sys

# Agregar el directorio padre al path para poder importar analizador_lexico
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analizador_lexico import lexer

def analizar_linea(linea, numero_linea):
    # Ignorar líneas vacías y comentarios
    if not linea.strip() or linea.strip().startswith('#'):
        return True, "Comentario o línea vacía"
    
    try:
        tokens = lexer(linea)
        return True, f"Tokens válidos: {tokens}"
    except SyntaxError as e:
        return False, f"Error de sintaxis: {str(e)}"
    except Exception as e:
        return False, f"Error inesperado: {str(e)}"

def analizar_archivo(nombre_archivo):
    print(f"\n{'='*20} Analizando {nombre_archivo} {'='*20}")
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
        
        print("\nResultados del análisis:")
        print("-" * 80)
        
        for i, linea in enumerate(lineas, 1):
            # Ignorar líneas que son solo comentarios de sección
            if linea.strip().startswith('# ==='):
                print(f"\n{linea.strip()}")
                continue
                
            # Obtener el comentario esperado si existe
            comentario = ""
            if '#' in linea:
                codigo, comentario = linea.split('#', 1)
                codigo = codigo.strip()
                comentario = comentario.strip()
            else:
                codigo = linea.strip()
            
            if codigo:  # Solo analizar si hay código (no solo comentarios)
                es_valido, mensaje = analizar_linea(codigo, i)
                estado = "✅ VÁLIDO" if es_valido else "❌ INVÁLIDO"
                print(f"\nLínea {i}: {estado}")
                print(f"Código: {codigo}")
                if comentario:
                    print(f"Comentario: {comentario}")
                print(f"Resultado: {mensaje}")
                print("-" * 80)
            
    except FileNotFoundError:
        print(f"\n❌ Error: No se encontró el archivo {nombre_archivo}")
    except Exception as e:
        print(f"\n❌ Error al leer el archivo: {str(e)}")

def main():
    # Asegurarse de que estamos en el directorio correcto
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=== Validador de Código ===")
    analizar_archivo('codigo_mixto.txt')

if __name__ == "__main__":
    main() 