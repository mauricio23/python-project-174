def stringify(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if not isinstance(value, dict):
        return str(value)

    # Reajuste de la indentación para diccionarios puros dentro de stringify
    current_indent = "    " * depth
    closing_indent = "    " * (depth - 1)
    lines = ["{"]
    
    for key, val in value.items():
        lines.append(f"{current_indent}{key}: {stringify(val, depth + 1)}")
        
    lines.append(f"{closing_indent}}}")
    return "\n".join(lines)


def format_stylish(diff, depth=1):
    indent = "    " * depth
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

    # El cierre de la llave principal del nivel actual debe alinearse con el nivel anterior
    lines.append(f"{'    ' * (depth - 1)}}}")
    return "\n".join(lines)