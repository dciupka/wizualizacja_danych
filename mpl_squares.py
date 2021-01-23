import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]



plt.style.use('fivethirtyeight') # in consol: import matplotlib.pyplot as plt ;  plt.style.available ---wyświeltenie stylow
fig, ax =plt.subplots()
ax.plot(input_values,squares, linewidth=3)


#zdefiniowanie tytułu wykresu i etykiety osi
ax.set_title('Kwadraty liczb', fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadrat wartości", fontsize=14)


#zdefiniowanie wielkości etykiet (liczb na osi x i y)
ax.tick_params(axis='both', labelsize=10)


plt.show()