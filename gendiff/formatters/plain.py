def to_str(value):
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
    lines = []

    
    sorted_diff = sorted(diff, key=lambda node: node['key'])

    for node in sorted_diff:
        key = node['key']
        t = node['type'] 
        current_path = f"{path}.{key}" if path else key

        if t == 'nested':
            lines.append(render_plain(node['children'], current_path))
        elif t == 'added':
            val = to_str(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {val}")
        elif t == 'deleted':  
            lines.append(f"Property '{current_path}' was removed")
        elif t == 'changed':
            val1 = to_str(node['old_value'])
            val2 = to_str(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. From {val1} to {val2}")

    return "\n".join(filter(None, lines))