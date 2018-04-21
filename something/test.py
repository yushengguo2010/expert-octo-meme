from matplotlib import pyplot as plt
from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1,1])
        distance = choice([0,1,2,3,8])
        return direction * distance
    
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_steps = self.get_step()
            y_steps = self.get_step()

            if x_steps == 0 and y_steps ==0:
                continue
                
            next_x_values = self.x_values[-1]+x_steps
            next_y_values = self.y_values[-1]+y_steps

            self.x_values.append(next_x_values)
            self.y_values.append(next_y_values)

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,6))
    # point_numbers = list(range(rw.num_points))
    # plt.plot(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=1)
    plt.plot(rw.x_values,rw.y_values)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.plot(0,0,c='green',linewidth=10)
    plt.plot(rw.x_values[-1],rw.y_values[-1],c='red')
    plt.show()
    keep_running = input('Make another walk?(y/n)): ')
    if keep_running == 'n':
        break