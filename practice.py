# help(str)
# help(list)

# 打印房间号
# for i in range(1, 6):
#     # if i == 4:
#     #     continue # 跳过本次循环，进入下一次
#     print(f'--------{i}F--------')
#     for j in range(1, 21):
#         # if i == 4 and j == 4:
#         #     break # 结束当前循环
#         if j < 10:
#             print(f'F{i}-{i}0{j}')
#         else:
#             print(f'F{i}-{i}{j}')

# 星号三角形
# for i in range(1, 10):
#     if i < 6:
#         print('*'*i)
#     else:
#         print('*'*(10-i))

# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}×{i}={i*j}', end='    ')
#     print()
#
# import requests
# url = 'http://www.baidu.com'
#
# # 传递url参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(url, params=payload)
# print(r.url)
# # http://www.baidu.com/?key1=value1&key2=value2

# name = input('请输入名字：')
# age = input('请输入年龄：')
# print('你叫'+name+'，今年'+age+'岁了')  # 用+号串联打印的内容
# print('你叫{}，今年{}岁了'.format(name, age))  # 使用format()函数插入

# print('{:.2f}'. format(3.1415926))
#
# a = 0.5
# if a < 1:
#     print('a<1')
# else:
#     pass

# for n in range(1, 11):
#     print('书桓走的第{}天，想他'.format(n))

# a = 0
# while a < 10:
#     a += 1
#     print(a)

# 逢7就跳过
# for i in range(1, 101):
#     if i % 7 == 0:
#         continue
#     elif i//10 == 7:
#         continue
#     elif i-10*(i//10) == 7:  # i % 10 == 7
#         continue
#     else:
#         print(i)

# i = int(input('请输入：'))
# a = i-10*(i//10)
# print(a)

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件，'-o'为参数简写，代表'--output'。
parser.add_argument('--width', type=int, default=160)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

# 解析并获取参数
args = parser.parse_args()

# 输入的图片文件路径
IMG = args.file

# 输出的字符画宽度
WIDTH = args.width

# 输出的字符画高度
HEIGHT = args.height

# 输出字符画的路径
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256个灰度映射到70个字符上
def get_char(r, g, b, alpha=256):

    # 判断alpha值
    if alpha == 0:
        return ' '

    # 获取字符集的长度，这里为70
    length = len(ascii_char)

    # 将RGB值转换为灰度值gray，灰度值范围为0-255
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)

    # 灰度值范围为0-255，而字符集只有70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0+1)/length

    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)




