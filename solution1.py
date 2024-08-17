# Write code for algorithm 1 below

def count(i):
    # Base case
    if i == 0:
        return
    # recursive case
    else:
        print(i)
        count(i - 1)
# test
i = 8
count(i)
