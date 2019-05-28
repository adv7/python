'''
LEGB
Local, Enclosing, Global, Built-in
'''

# import builtins

# print(dir(builtins))


# def my_min():
#     pass


# x = 'global x'
# m = min([5, 1, 4, 3, 2])
# print(m)


# def test(z):
#     # global x
#     x = 'local x'
#     # print(x)
#     print(x)
#     print(z)


# test('local z')
# print(x)

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
