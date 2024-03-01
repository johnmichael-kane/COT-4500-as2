import Problem2 as p

target_x=7.3

#this is the function to approximate it using all the values we obtained in Problem2
approximation = p.c[0] + \
    (target_x - p.x[0]) * p.d1 + \
    (target_x - p.x[0]) * (target_x - p.x[1]) * p.d2 + \
    (target_x - p.x[0]) * (target_x - p.x[1]) * (target_x - p.x[2]) * p.d3


print(approximation)
