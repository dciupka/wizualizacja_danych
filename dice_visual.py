from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# utowrzenie dwóch kości o 6 sciankach

die_1 = Die()
die_2 = Die()

# wykonannie pewnej liczby rzutów i umieszczenie jej na liście

results = []

for result in range(1000):
    result = die_2.roll() + die_1.roll()
    results.append(result)

# analiza wyników

frequ = []

max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequ.append(frequency)

# wizualizacja wyników

x_values = list(range(2, max_result+ 1))
data = [Bar(x=x_values, y=frequ)]

x_axis_config = {'title': 'Wynik', 'dtick':1}  #dtick znacznik pod każdym słupkiem i odleglosc pomiedzy słupkai jak :3 co 3,9 slupkipodpisane
y_axis_config = {'title': 'Częstotliwośc'}

my_layout = Layout(title='Wyniki wyrzucania pojedynczą kością', xaxis=(x_axis_config), yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d12-page.html')

