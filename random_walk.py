from random import choice


class RandomWalk():
    """Klasa przeznaczona do wygenerowania błądzenia losowego"""

    def __init__(self, num_points=5000):
        """Inicjalizacja atrybutów błądzenia"""
        self.num_points = num_points

        # Punkt początkowy współrzędne(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Wygenenerowanie punktów dal błączenia losowego"""

        while len(self.x_values) < self.num_points:

            # ustalenie kierunku oraz odległości do pokonanaia w tym kierunki
            y_direction = [-1, 1]
            x_direction = [-1, 1]

            y_distance = [0, 1, 2, 3, 4]
            x_distance = [0, 1, 2, 3, 4]

            x_step = choice(x_direction) * choice(x_distance)
            y_step = choice(y_direction) * choice(y_distance)

            # wykluczenie korku do nikąd
            if x_step == 0 and y_step == 0:
                continue

            # ustalenie następnych wartości

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

