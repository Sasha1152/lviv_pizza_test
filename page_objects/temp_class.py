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

var = A.__name__.lower()
print(var)
exec(f'{var} = 100')
print(a)

classname_obj = eval('A')
print(classname_obj)
a = classname_obj(2)

# print(vars())
# exec(f'a = {}')
# x= globals()[classname]
print(a)
print(a.var1)
print(a.var2)
