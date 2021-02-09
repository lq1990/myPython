'''
file, folder
'''

import os

# os.rename('abc.txt','abc1.txt')
# os.remove('abc.txt.bk')

# create dir
if not os.path.isdir('tmp1'):  # isdir: if exists the dir
    os.mkdir('tmp1')

# get current working dir
print(os.getcwd())

# delete dir
if os.path.isdir('tmp1'):
    os.rmdir('tmp1')

'''
change cwd
'''

if not os.path.isdir('tmp'):
    os.mkdir('tmp')

os.chdir('tmp')
with open('t1.txt', 'a') as f:
    f.write('some words')


os.chdir('../')
print(os.listdir(os.getcwd()))

print(os.path.join(os.getcwd(), 'kkk')) # F:\Users\lq\code\myPython\review\file_ops\kkk





