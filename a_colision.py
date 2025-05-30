import math


def check_collision_inters(pos1, pos2):
    # Define los vértices del objeto 1
    vertices1 = [
        (pos1[0] + 1, 0, pos1[2] + 1),  # Vértice 0
        (pos1[0] + 1, 0, pos1[2] - 1),  # Vértice 1
        (pos1[0] + 1, 0, pos1[2] + 1),  # Vértice 2
        (pos1[0] + 1, 0, pos1[2] - 1),  # Vértice 3
        (pos1[0] - 1, 0, pos1[2] + 1),  # Vértice 4
        (pos1[0] - 1, 0, pos1[2] - 1),  # Vértice 5
        (pos1[0] - 1, 0, pos1[2] + 1),  # Vértice 6
        (pos1[0] - 1, 0, pos1[2] - 1)   # Vértice 7
    ]

    # Verifica si al menos uno de los vértices del objeto 1 está dentro del objeto 2
    for vertex in vertices1:
        if (pos2[0] - 1 <= vertex[0] <= pos2[0] + 1 and
            pos2[1] - 1 <= vertex[1] <= pos2[1] + 1 and
            pos2[2] - 1 <= vertex[2] <= pos2[2] + 1):
            return True

    return False


def check_collision_diamond(pos1, pos2):
    # Calcula la distancia entre los centros de los objetos
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    distance = math.sqrt(dx**2 + dy**2 + dz**2)

    # Calcula la mitad de la suma de las longitudes de las diagonales de los objetos
    diagonal1 = math.sqrt(2) * 2  # Longitud de la diagonal de un cubo de lado 2
    diagonal2 = math.sqrt(2) * 2  # Longitud de la diagonal de un cubo de lado 2
    sum_diagonals = (diagonal1 + diagonal2) / 2

    # Comprueba si la distancia entre los centros es menor que la mitad de la suma de las longitudes de las diagonales
    return distance < sum_diagonals


def check_collision_sat(pos1, pos2):
    # Define los límites de las cajas
    min_x1, max_x1 = pos1[0] - 1, pos1[0] + 1
    min_y1, max_y1 = pos1[1] - 1, pos1[1] + 1
    min_z1, max_z1 = pos1[2] - 1, pos1[2] + 1

    min_x2, max_x2 = pos2[0] - 1, pos2[0] + 1
    min_y2, max_y2 = pos2[1] - 1, pos2[1] + 1
    min_z2, max_z2 = pos2[2] - 1, pos2[2] + 1

    # Verifica la separación en cada eje
    if max_x1 < min_x2 or min_x1 > max_x2:
        return False  # No hay colisión en el eje x
    if max_y1 < min_y2 or min_y1 > max_y2:
        return False  # No hay colisión en el eje y
    if max_z1 < min_z2 or min_z1 > max_z2:
        return False  # No hay colisión en el eje z

    return True  # Hay colisión en todos los ejes, por lo tanto, colisión total

