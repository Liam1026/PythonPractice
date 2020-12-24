class test(object):
    def __init__(self):
        print('Test -> __init__')

    def __new__(cls):
        print('Test -. __new__')
        return super().__new__(cls)

a =  test()

class test2(object):
    def __init__(self):
        print('Test2 -> __init__')

    def __new__(cls):
        print('Test2 -> __new__')
        return object()

b = test2()

print('a:',type(a))
print('b:',type(b))

# __init__ 作用是类实例进行初始化
"""官方的解释：__init__ 作用是类实例进行初始化，第一个参数为 self，代表对象本身，可以没有返回值。__new__ 则是返回一个新的类的实例，第一个参数是 cls 代表该类本身，必须有返回值。很明显，类先实例化才能产能对象，显然是 __new__ 先执行，然后再 __init__，实际上，只要 __new__ 返回的是类本身的实例，它会自动调用 __init__ 进行初始化。但是有例外，如果 __new__ 返回的是其他类的实例，则它不会调用当前类的 __init__。"""

