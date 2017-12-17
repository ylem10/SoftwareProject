# -*- coding: utf-8 -*-
from __init__ import app
import random, math, datetime
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

from flask import Flask, make_response, render_template, request, session


class ImageChar():
    def __init__(self, fontColor=(0, 0, 0),
                 size=(100, 40),
                 fontPath='STZHONGS.TTF',
                 bgColor=(255, 255, 255, 255),
                 fontSize=20):
        self.size = size
        self.fontPath = fontPath
        self.bgColor = bgColor
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = ImageFont.truetype(self.fontPath, self.fontSize)
        self.image = Image.new('RGBA', size, bgColor)

    def rotate(self):
        img1 = self.image.rotate(random.randint(-5, 5), expand=0)  # 默认为0，表示剪裁掉伸到画板外面的部分
        img = Image.new('RGBA', img1.size, (255,) * 4)
        self.image = Image.composite(img1, img, img1)

    def drawText(self, pos, txt, fill):
        draw = ImageDraw.Draw(self.image)
        draw.text(pos, txt, font=self.font, fill=fill)
        del draw

    def randRGB(self):
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def randPoint(self):
        (width, height) = self.size
        return (random.randint(0, width), random.randint(0, height))

    def randLine(self, num):
        draw = ImageDraw.Draw(self.image)
        for i in range(0, num):
            draw.line([self.randPoint(), self.randPoint()], self.randRGB())
        del draw

    def randChinese(self, num):
        gap = 0
        start = 0
        strRes = ''
        code = ""
        for i in range(0, num):
            num = random.randint(0, 9)
            code = str(code) + str(num)
            x = start + self.fontSize * i + random.randint(0, gap) + gap * i
            self.drawText((x, random.randint(-5, 5)), str(num), (0, 0, 0))
            self.rotate()
        print(strRes)
        self.randLine(8)
        print(code)
        session["validCode"] = code
        return strRes, self.image


@app.route('/VerifyCode')
def get_code():
    # 把strs发给前端,或者在后台使用session保存
    ic = ImageChar(fontColor=(100, 211, 90))
    strs, code_img = ic.randChinese(5)
    buf = BytesIO()
    code_img.save(buf, 'PNG', quality=70)
    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/png'
    return response


