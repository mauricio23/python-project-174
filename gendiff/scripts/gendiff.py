import argparse
from gendiff.parser import parse
from gendiff.diff_builder import build_diff
from gendiff.formatters.stylish import format_stylish

def generate_diff(file_path1, file_path2, format_name='stylish'):
    # 1. Tu parser lee los archivos (JSON/YAML) y los vuelve diccionarios
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    
    # 2. Tu diff_builder analiza la profundidad de forma recursiva
    diff_tree = build_diff(data1, data2)
    
    # 3. Tu stylish aplica el formato con los espacios y signos correctos
    if format_name == 'stylish':
        return format_stylish(diff_tree)
    
    raise ValueError(f"Formato no soportado: {format_name}")

def main():
    parser = argparse.ArgumentParser(
        description="Compara dos archivos de configuración y muestra una diferencia."
    )
    parser.add_argument("file1")
    parser.add_argument("file2")
    # Agregamos el argumento opcional de formato, con 'stylish' por defecto
    parser.add_argument(
        "-f", "--format", 
        default="stylish", 
        help="set format of output (default: 'stylish')"
    )

    args = parser.parse_args()

    # Ejecutamos pasando los archivos y el formato elegido
    diff = generate_diff(args.file1, args.file2, args.format)

    print(diff)

if __name__ == "__main__":
    main()