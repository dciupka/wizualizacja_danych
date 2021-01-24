from random_walk import RandomWalk
import matplotlib.pyplot as plt


while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)

    plt.show()

    keep_running = input("Utworzyć nowy wykres?> ")

    if keep_running == 'n':
        break
