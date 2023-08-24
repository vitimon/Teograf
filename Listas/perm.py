from time import time

def recursive_permutations(list_p,lefty = []):
    for i in list_p:
        if len(list_p) > 1:
            remaining =  [] + list_p
            remaining.remove(i)
            recursive_permutations(remaining,lefty + [i])
        else:
            print(lefty + list_p)

def genterate_pemutations(n):
    initial_range = range(1,n+1)
    initial_list = list(initial_range)
    recursive_permutations(initial_list)

def measure(measurements = {},until = 1):
    t0 = time()
    genterate_pemutations(until)
    tf = time()
    elapsed = tf - t0
    measurements[str(until)] = elapsed
    print(measurements)
    x = input()
    measure(measurements,until + 1)

measure()


    