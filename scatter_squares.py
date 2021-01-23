import matplotlib.pyplot as plt

x_values=range(0,1001)
y_values=[x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

#ax.scatter(x_values,y_values, s=10, c='green')  # s=wielkosc plamki punktu; c='red' or c=(0,0.8,0) RGB

ax.scatter(x_values,y_values, s=10, c=y_values, cmap=plt.cm.cool)  #https://matplotlib.org/gallery/color/colormap_reference.html

#zdefiniowanie tytułu wykresu i etykiety osi
ax.set_title('Kwadraty liczb', fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadrat wartości", fontsize=14)

#zdefiniowanie wielkości etykiet (liczb na osi x i y)
ax.tick_params(axis='both', labelsize=16)

#zdefiniowanie wyświetlania zakresu dla każdej osi

ax.axis([0,1100,0,1100000])

#plt.savefig('squares_plot.png')
plt.show()