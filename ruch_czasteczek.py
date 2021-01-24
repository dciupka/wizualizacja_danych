from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi=100) #rozmiar w calach i dpi 100pixeli na cal rozdzielczosc
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values ,linewidth=1)


    # Pokolorowanie pierwszego i ostaniego punktu

    ax.scatter(0, 0, c='green', s=250)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=250)

    plt.show()

    keep_running = input("Utworzyć nowy wykres?> ")

    if keep_running == 'n':
        break
