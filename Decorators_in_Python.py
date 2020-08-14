#Decorators in Python
"""
def function1():
    print('Subscribe now')

func2 = function1

#del function1
func2()    
"""

# def functret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = functret(1) 
# print(a)           

# def execuotor(func):
#     func('This is Himesh')

# execuotor(print)
def dec1(func1):
    def nowexc():
        print('Executing now')
        func1()
        print('Executed')
    return nowexc    
@dec1
def who_is_harry():
    print('Harry is a good boy')

#who_is_harry = dec1(who_is_harry)
who_is_harry()
