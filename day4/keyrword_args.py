def foo(x, z, y=10):
    print(x, z, y)


foo(1, 2)
foo(3, z=11)
foo(x=12, z=13)
foo(z=13, x=12, y=14)
# foo(4, y=5)
# foo(x=6, y=7) # foo(6, 7)
# foo(x=8)

# boom!
# foo(y=7, 10)