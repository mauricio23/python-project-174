def to_str(value):
    """Formatea los valores individuales según las reglas de Hexlet."""
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def render_plain(diff, path=""):
    """Recorre el AST recursivamente generando las líneas de texto plano."""
    lines = []

    for key, node in sorted(diff.items()):
        # Construimos la ruta completa (ej: 'common.setting6.ops')
        current_path = f"{path}.{key}" if path else key
        status = node.get('status')

        if status == 'nested':
            # Si es anidado, bajamos recursivamente pasando la ruta actual
            lines.append(render_plain(node['children'], current_path))
        elif status == 'added':
            val = to_str(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {val}")
        elif status == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif status == 'changed':
            val1 = to_str(node['old_value'])
            val2 = to_str(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. From {val1} to {val2}")
        # El status 'unchanged' se ignora por completo en formato plain

    # Filtramos líneas vacías y unimos con saltos de línea
    return "\n".join(filter(None, lines))