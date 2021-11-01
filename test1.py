import argparse
# help(argparse)
pa = argparse.ArgumentParser()
pa.add_argument('square', type=int)
args = pa.parse_args()
print(args.square**2)

import sys
import os
import _io
from collections import namedtuple
from PIL import Image

class Nude:
    Skin = namedtuple ("Skin", "id skin region x y")

def __init__(self, path_or_image):
    # 若path_or_image为Image.Image类型的实例，直接赋值
    if isinstance(path_or_image, Image.Image):
        self.image = path_or_image

    # 若path_or_image为str类型的实例，打开图片
    elif isinstance(path_or_image, str):
        self.image = Image.open(path_or_image)

    # 获得图片所有颜色通道
    bands = self.image.getbands()

    # 判断是否为单通道图片（也即灰度图），是则将灰度图转换为RGB图
    if len(bands) == 1:

        # 新建相同大小的RGB图像
        new_img = Image.new("RGB", self.image.size)

        # 拷贝灰度图self.image到RGB图new_img.paste（PIL自动进行颜色通道转换）
        new_img.paste(self.image)
        f = self.image.filename
        # 替换self.image
        self.image = new_img
        self.image.filename = f

    # 存储对应图像所有像素的全部Skin对象
    self.skin_map = []
    # 检测到的皮肤区域，元素的索引即为皮肤区域号，元素都是包含一些Skin对象的列表
    self.detected_regions = []
    # 元素都是包含一些int对象（区域号）的列表
    # 这些元素中的区域号代表的区域都是待合并的区域
    self.merge_regions = []

    # 整合后的皮肤区域，元素的索引即为皮肤区域号，元素都是包含一些Skin对象的列表
    self.skin_regions = []

    # 最近合并的两个皮肤区域的区域号，初始化为-1
    self.last_from, self.last_to = -1, -1
    # 色情图像判断结果
    self.result = None
    # 处理得到的信息
    self.message = None
    # 图像宽高
    self.width, self.height = self.image.size
    # 图像总像素
    self.total_pixels = self.width * self.height


def resize(self, maxwidth=1000, maxheight=1000):
    ret = 0
    if maxwidth:
        if self.width > maxwidth:
            wpercent = (maxwidth/self.width)
            hsize = int((self.height * wpercent))
            fname = self.image.filename

            self.image = self.image.resize((maxwidth,hsize), Image.LANCZOS)
            self.image.filename = fname
            self.width, self.height = self.image.size
            self.total_pixels = self.width * self.height
            ret += 1
    if maxheight:
        if self.height > maxheight:
            hpercent = (maxheight/float(self.height))
            wsize = int((float(self.width) * float(hpercent)))
            fname = self.image.filename
            self.image = self.image.resize((wsize, maxheight), Image.LANCZOS)
            self.image.filename = fname
            self.width, self.height = self.image.size
            self.total_pixels = self.width * self.height
            ret += 2
    return ret

def parse(self):
    if self.result is not None:
        return self

    pixels = self.image.load()

    for y in range(self.height):
        for x in range(self.width)

        r = pixels[x, y][0]

        g = pixels[x, y][1]

        b = pixels[x, y][2]

        if self._classify_skin(r,g,b):
            isSkin = True
        else:
            False


        -id = x + y * self.width + 1

        self.skin_map.append(self.Skin(_id, isSkin, None, x, y))

        if not isSkin:
            continue
