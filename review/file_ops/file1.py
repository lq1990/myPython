
# 打开。用a模式时指针在文件尾，所有a模式下直接read的话是空的内容
f = open('F:/Users/lq/code/myPython/review/file_ops/abc1.txt', mode='rb+')
f.seek(-3, 2) # 若不加这个seek0，就直接read的话 那么由于指针在EOF，所以read为空。
# 若想从后往前改的话，需要加 b模式
f.write(b'E') # 从当前光标向后写

# print(f.read()) # read all
# print(f.readline()) # read only one line,  like a iterator
# print(f.readlines()) # save in list

# write
f.write(b'Q')  # rb+, seed(-1,2)

f.close()

print()

exit(0)

# no need to close() if we use below:
with open('abc.txt') as f:
    print(f.read())

'''
backup file
'''

name = 'abc.txt'
index = name.rfind('.')
new_name = name[:index] + name[index:] + '.bk'

f0 = open(name, 'rb')
f1 = open(new_name, 'wb')
while True:
    con = f0.read(1024)
    if len(con) == 0:
        break

    f1.write(con)

f1.close()
f0.close()




