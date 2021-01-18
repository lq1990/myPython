# json
# json.dumps(v) 序列化后的都是 字符串类型
# json.loads() 对应dumps，反序列化

# json.dump(待序列化的, file), dump 序列化后，存储到文件里
# json.load(file), load json from a file

import json

# 对元组进行序列化
tup = (1,2,3) # 元组类型。被json dumps loads之后变成list
a = json.dumps(tup) # dumps之后的是 str类型
print(a)
print(type(a)) # <class 'str'>，

print(json.loads(a)) # loads传入的是字符串类型
print(type(json.loads(a))) # list

# 对集合进行序列化。不行。
mset = {1,2,3}
# print(json.dumps(mset))

# python中的dict和json很相似。只是json中用双引号

# 对数据 序列化 dumps
print()
print('对数组序列化')
v = [12,3,4, {'k1':'v1'}, True, 'abcd']
v1 = json.dumps(v) # 返回的是str类型
print(v1, type(v1))

# 反序列化 loads
print("反序列化数组")
v2 = '["abc", 123]'
print(type(v2))
v22 = json.loads(v2) # 返回的是list类型
print(v22, type(v22))

# dump 到文件里
print('\ndump: ')
f = open("v.txt", mode="w", encoding="utf-8")
json.dump(v, f) # 将内容序列化，并写入打开的文件中
f.close()

# load 从文件里
print("\nload")
f = open("v.txt", mode='r', encoding='utf-8')
data = json.load(f)
f.close()
print(data, type(data))

