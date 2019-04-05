class A:
    var1 = 1

    def __init__(self, var2):
        self.var2 = var2

class B(A):
    pass

class C(A):
    pass


classes = {}
for obj in A.__subclasses__():
    inst_name = obj.__name__.lower()
    temp_inst = obj(2)
    classes[inst_name] = temp_inst

print(classes)
print(classes['c'].var2)


# print(globals()[A.__name__])

# print(get_instance_name(A))

# print(getattr(A, '__name__'))

# print(a.var1)
# print(a.var2)

class GeneralPage:
    def __init__(self, var):
        self.var = var

    @classmethod
    def create_instanses_for_all(cls, var):
        classes = {}
        for obj in cls.__subclasses__():
            inst_name = obj.__name__.lower()
            class_obj = obj(var)
            classes[inst_name] = class_obj
        return classes

class GooglePage(GeneralPage):
    pass

class PizzaLvivPage(GeneralPage):
    pass

print(GeneralPage.create_instanses_for_all(5))
print(GeneralPage.create_instanses_for_all(5)['googlepage'])
