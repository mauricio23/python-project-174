from gendiff.parser import parse
from gendiff.diff_builder import build_diff  # Tu generador de árbol lógico
from gendiff.formatters.stylish import format_stylish  # Revisa cómo se llama tu función stylish
from gendiff.formatters.plain import render_plain

def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    
    # Tu lógica actual que genera el árbol de diferencias
    diff_tree = build_diff(data1, data2)
    
    # Selector de formato
    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'plain':
        return render_plain(diff_tree)
    else:
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