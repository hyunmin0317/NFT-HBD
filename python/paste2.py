import random

from PIL import Image, ImageDraw, ImageFont

spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

selectedFont = ImageFont.truetype('font.ttf', 1200)  # 폰트경로과 사이즈를 설정해줍니다.
candle1 = Image.open("1.png")
candle2 = Image.open("2.png")
candle1 = candle1.resize((4086, 4086))
candle2 = candle2.resize((4086, 4086))

def save(season, list):
    i = 1
    for month in list:
        for day in range(1, days[month - 1] + 1):
            hbd = "%02d.%02d" % (month, day)
            target_image = Image.open('./src/'+ season + '/' +str(i) + '.png')  # 일단 기본배경폼 이미지를 open 합니다.

            if random.choice([True, False]):
                target_image.paste(candle1, (0, 0), candle1)
            else:
                target_image.paste(candle2, (0, 0), candle2)


            target_image.save("./nft/" + hbd + ".png")
            i += 1

save("spring", spring)