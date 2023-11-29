#This program allows you to calculate the probability of getting the specified (points) number of points in total. 
#When (count_dice) dice with (verge) sides are thrown.
#The percentage is printed, rounded to one decimal place.
import numpy as np

count_dice, verge, points = int(input()), int(input()), int(input())
x = np.random.choice(np.arange(1, verge + 1), size=(100000, count_dice))
res = np.sum(np.sum(x, axis=1) == points)
probability = (res / 100000) * 100
rounded_probability = round(probability, 1)

print(f"{rounded_probability}%")
