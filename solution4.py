# Write code for algorithm 4 below

def to_the_power(n, y):
    if y == 1:
        return n
    else:
        return n * to_the_power(n, y-1)

print(to_the_power(5, 3))