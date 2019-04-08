class A:
    var1 = 1

    def __init__(self, var2):
        self.var2 = var2

class B(A):
    pass

class C(A):
    pass

"""
classes = {}
for obj in A.__subclasses__():
    inst_name = obj.__name__.lower()
    temp_inst = obj(2)
    classes[inst_name] = temp_inst

print(classes)
print(classes['c'].var2)
"""

# print(globals()[A.__name__])

# print(getattr(A, '__name__'))

# classname = str(A.__name__.lower())
# print(classname)
# instance = A(2)
# x= globals()[classname]
# a = x(2)
# exec(f'{classname} = {instance}')

# print(classname)
print(issubclass(B, A))

# print(a.var1)
# print(a.var2)
