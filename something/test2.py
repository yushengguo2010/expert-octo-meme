from random import randint
import pygal

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)

die=Die()
results =[]

for roll_num in range(1000):
    result=die.roll()
    results.append(result)

fres = []
for each in range(1,die.num_sides+1):
    fre = results.count(each)
    fres.append(fre)

hist = pygal.Bar()

hist._title = 'Results of rolling one D6 1000 times'
hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = 'Result'
hist._y_title = 'Fre of result'

hist.add('D6',fres)
hist.render_to_file('die_visual.svg')