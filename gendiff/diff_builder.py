def build_diff(data1, data2):
    # Obtenemos todas las llaves de ambos archivos y las ordenamos
    keys = sorted(data1.keys() | data2.keys())
    diff = []

    for key in keys:
        if key not in data1:
            # La llave no estaba en el primero, es nueva
            diff.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif key not in data2:
            # La llave no está en el segundo, fue eliminada
            diff.append({'key': key, 'type': 'deleted', 'value': data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            # ¡RECURSIVIDAD! Si ambos son diccionarios, llamamos a build_diff otra vez
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            # El valor es idéntico
            diff.append({'key': key, 'type': 'unchanged', 'value': data1[key]})
        else:
            # El valor cambió
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
    return diff