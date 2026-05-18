def stringify(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if not isinstance(value, dict):
        return str(value)

    # Si el valor es un diccionario, debemos formatearlo con espacios
    indent = "    " * depth
    lines = ["{"]
    for key, val in value.items():
        lines.append(f"{indent}    {key}: {stringify(val, depth + 1)}")
    lines.append(f"{indent}}")
    return "\n".join(lines)

def format_stylish(diff, depth=1):
    indent = "    " * depth
    # El prefijo para los signos (+ o -) son 2 espacios menos que la indentación base
    prefix = indent[:-2]
    lines = ["{"]

    for node in diff:
        t = node['type']
        key = node['key']

        if t == 'nested':
            lines.append(f"{indent}{key}: {format_stylish(node['children'], depth + 1)}")
        elif t == 'added':
            lines.append(f"{prefix}+ {key}: {stringify(node['value'], depth + 1)}")
        elif t == 'deleted':
            lines.append(f"{prefix}- {key}: {stringify(node['value'], depth + 1)}")
        elif t == 'changed':
            lines.append(f"{prefix}- {key}: {stringify(node['old_value'], depth + 1)}")
            lines.append(f"{prefix}+ {key}: {stringify(node['new_value'], depth + 1)}")
        elif t == 'unchanged':
            lines.append(f"{indent}{key}: {stringify(node['value'], depth + 1)}")

    lines.append(f"{indent[:-4]}}}")
    return "\n".join(lines)