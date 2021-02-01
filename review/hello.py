import numpy as np

# 复习
'''
多行注释
'''

print("hello world!")
a = 33
print(id(a))
a = 332
print(id(a))

list = [11, 12, 13]
print(list)
print(id(list))
list.append(14)
print(id(list))

tu1 = (11, 22, 33)
print(tu1)

set1 = {11, 2, 2, 3}
print(set1)

dict1 = {'k1': 11, 'k2': 12, 'k1': 111}
print(dict1)

'''
for
'''
for i in range(0, 5):
    print(i, end='')  # default end is \n

print()

for item in 'hello':
    print(item)

for item in list:
    print('item:', item)

'''
operator
'''
print(10 // 3)
print(10 / 3)
print(10 % 3)
print(10 ** 3)
print('ab' * 2)
# print(10++) # error, no ++


'''
String
'''
print("\nString:")
str1 = 'abcdefg'
print(str1[0:3])  # note: left close,right open
print(str1[::-2])  # geca
print(str1[1:4:-2])  # empty
print(str1[-1:-4:-2])  # ge,  note: pos of -1 is g
print("abc" + "aaa")

print('nihaonihao'.count('ni'))
print('nihaonihao'.startswith('ni'))
print('nihaonihao'.endswith('ni'))
print("nihaonihao".replace('ni', 'ni2'))
print('nihao1'.isalpha())
print('nihao1'.isalnum())
print('nihao'.isalpha())

'''
不可变：Number, String, Tuple
可变：list, set, dict
'''

'''list'''
print("list")
list1 = [11, 222, 33, 33, 44, 1, 2]
print(list1)
list1.remove(11)  # remove an item
print(list1)
list1.pop(0)  # delete an value of idx=0
print(list1)

list1.sort(reverse=True)
print(list1)

'''
tuple, CRUD, 常用方法
元组是不可变的，一旦定义了变量，不可修改
'''
print("tup:")
tup = (11, 22, 'a')
print(tup)

# del tup


'''
dict:
可变的，即可增删改元素
'''
print("dict:")
d1 = {"name": "zhangsan", "age": 18, "class": 302}
print(d1)
print(d1.get("name"))
print(d1["name"])
print(d1.keys())  # return list

print("===\nkey: ")
for key in d1:
    print(key)

print("===\nkey, val:")
for key, val in d1.items():
    print(key, val, sep=':')

d1['name'] = "lisi"
print(d1)

d1.update({'name': 'ana', 'addr': 'sh'})  # only update/add name
print(d1)

# del d1
del d1['addr']
print(d1)

'''
set
可变
'''
print('set: ')
s1 = {11, 22, 33}
s1.remove(11)
s1.add(111)
print('s1: ', s1)
print('list1: ', list1)
s2 = set(list1)
print('s2: ', s2)

s_jiao = s1 & s2;
print(s_jiao)
s_bing = s1 | s2;
print(s_bing)
s_cha = s1 - s2;
print(s_cha)

'''
fn
传参注意：
    对于不可变类型（Number, String, Tuple），传递的是值
    对于 可变类型（list，set，dict）传递的是地址，因此函数内部修改后对外部有影响
'''
print("===\nfn, lambda:")


def fn1():
    return


def add(a, b):
    return a + b


print(add(4, 5))


def push_back(arr):
    arr.append(5)


list2 = [1, 2, 3, 4]
push_back(list2)
print(list2)

# 不定长参数
print('不定长参数')


def my_print(*args):
    for item in args:
        print(item)


my_print(11, 22, 33, [1, 12])

'''
lambda expr
'''
print("lambda: ")
my_lam = lambda a1, b: a1 + b

print(my_lam(11, 2))

'''
class
'''
print("class review: ")


class Father():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Son(Father):
    def __init__(self, name, age, email):
        super().__init__(name, age)
        self.email = email

    def print(self):
        print(self.name, self.age, self.email, sep=', ')


son = Son('zhangsan', 18, 'abc@123.com')
son.print()

'''
file
'''
print('===\nfile review:\n===')
obj = open("./test.csv", 'r+', encoding='utf-8')  # r+ 可以读和写

print(obj.read())

obj.close()




