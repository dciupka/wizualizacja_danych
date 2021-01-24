from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# utowrzenie kości
die = Die()

results = []

for roll_num in range(0, 500_000):
    result = die.roll()
    results.append(result)


# Analiza wyników

frequencieies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencieies.append(frequency)

print(frequencieies)

# wizualizacja wyników

x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencieies)]

x_axis_config = {'title': 'Wynik'}
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}

my_layout = Layout(title='Wyniki wyrzucania pojedyncza kościa', xaxis=(x_axis_config), yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6-page.html')
