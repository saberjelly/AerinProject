a = [1,2,3,4,5]
iterator_a = iter(a)
print()

def line(x):
    m = 3
    b = 1
    y = m * x + b
    return y

def simple_generator():
    while True:
        yield 1

def stop_generator_ex():
    a = [1, 2, 3, 4, 5]
    iterator_a = iter(a)
    while True:
        yield next(iterator_a)

gen = simple_generator()
stop_gen = stop_generator_ex()
print()