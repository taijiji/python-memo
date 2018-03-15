class Sample(object):
    def func_0(self):
        return '0'

    def func_1(self, arg1):
        return arg1

    def func_2(self, arg1, arg2):
        return arg1 + arg2


s = Sample()

result = s.func_0()
print(result)

result = s.func_1('test1')
print(result)

result = s.func_2('test1', 'test2')
print(result)

func = getattr(s, 'func_0')
result = func()
print(result)

func = getattr(s, 'func_1')
result = func('test1')
print(result)

func = getattr(s, 'func_2')
result = func('test1', 'test2')
print(result)