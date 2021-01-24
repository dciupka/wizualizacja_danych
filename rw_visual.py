from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues)

    # Pokolorowanie pierwszego i ostaniego punktu

    ax.scatter(0, 0, c='green', s=250)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=250)

    plt.show()

    keep_running = input("Utworzyć nowy wykres?> ")

    if keep_running == 'n':
        break
