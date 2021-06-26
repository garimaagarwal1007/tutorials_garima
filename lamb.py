class Test:
    _static_var = 'Garima'

    # magic method
    def __init__(self):
        self.instance_var1 = "Damodar"
        self.instance_var2 = "Akshay"

    def i_method(self):
        print(self.instance_var1)
        print(self.instance_var2)
        print(self._static_var)

    @classmethod
    def c_method(cls):
        print(cls)
        print(cls._static_var)
        #print(cls.instance_var2)

    @staticmethod
    def s_method(a, b):
        print(Test._static_var)
        print(a + b)


test = Test()
test.i_method()
test.c_method()
test.s_method(10, 20)

# list1 = [1, 2, 3, 4]
# __square_list = map(lambda x: x * x, list1)
# print(__square_list)
