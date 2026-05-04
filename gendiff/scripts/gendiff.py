import argparse 
import json
import os
import yaml

def cargar_datos(ruta1, ruta2):

    def cargar_archivo(ruta):
        _, ext = os.path.splitext(ruta)
        ext = ext.lower()

        with open(ruta, 'r', encoding='utf-8') as f:
            if ext == '.json':
                return json.load(f)
            elif ext in ['.yml', '.yaml']:
                return yaml.safe_load(f)
            else:
                raise ValueError(f"Extensión no soportada: {ext}")

    data1 = cargar_archivo(ruta1)
    data2 = cargar_archivo(ruta2)

    return data1, data2

def stringify(value):
    
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)

def generate_diff(file_path1, file_path2):
    # 1. Cargar los datos (puedes usar la función cargar_datos que ya tienes)
    data1, data2 = cargar_datos(file_path1, file_path2)
    
    # 2. Obtener todas las llaves y ordenarlas
    keys = sorted(data1.keys() | data2.keys())
    
    # 3. Construir el resultado (aquí va la magia)
    lines = ['{']
    for key in keys:
       
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                # El valor es igual en ambos
                lines.append(f"    {key}: {data1[key]}")
            else:
                # El valor cambió (Caso especial del timeout)
                lines.append(f"  - {key}: {data1[key]}")
                lines.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            # Estaba en el 1 pero ya no en el 2 (Eliminado)
            lines.append(f"  - {key}: {data1[key]}")
        else:
            # No estaba en el 1 pero apareció en el 2 (Agregado)
            lines.append(f"  + {key}: {data2[key]}")
        pass

    lines.append('}')
    return "\n".join(lines)


def main():
    
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("file1")
    parser.add_argument("file2")

    args = parser.parse_args()

    diff = generate_diff(args.file1, args.file2)

    print(diff)
if __name__ == "__main__":
    main()