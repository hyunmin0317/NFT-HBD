from PIL import Image, ImageDraw, ImageFont

spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
selectedFont = ImageFont.truetype('font.ttf', 1200)  # 폰트경로과 사이즈를 설정해줍니다.

# i = 1
# for month in spring:
#     for day in range(1, days[month-1]+1):
#         hbd = "%02d.%02d"%(month, day)
#         target_image = Image.open('./nft/spring/' + str(i) + '.png')  # 일단 기본배경폼 이미지를 open 합니다.
#         draw = ImageDraw.Draw(target_image)
#         draw.text((1430, 2750), hbd, fill="white", font=selectedFont, align='center')  # fill= 속성은 무슨 색으로 채울지 설정,font=는 자신이 설정한 폰트 설정
#         target_image.save("./save/spring/" + str(i) + ".png")
#         i+=1
#
# i = 1
# for month in summer:
#     for day in range(1, days[month-1]+1):
#         hbd = "%02d.%02d"%(month, day)
#         target_image = Image.open('./nft/summer/' + str(i) + '.png')  # 일단 기본배경폼 이미지를 open 합니다.
#         draw = ImageDraw.Draw(target_image)
#         draw.text((1430, 2750), hbd, fill="white", font=selectedFont, align='center')  # fill= 속성은 무슨 색으로 채울지 설정,font=는 자신이 설정한 폰트 설정
#         target_image.save("./save/summer/" + str(i) + ".png")
#         i+=1
#
# i = 1
# for month in autumn:
#     for day in range(1, days[month-1]+1):
#         hbd = "%02d.%02d"%(month, day)
#         target_image = Image.open('./nft/autumn/' + str(i) + '.png')  # 일단 기본배경폼 이미지를 open 합니다.
#         draw = ImageDraw.Draw(target_image)
#         draw.text((1430, 2750), hbd, fill="white", font=selectedFont, align='center')  # fill= 속성은 무슨 색으로 채울지 설정,font=는 자신이 설정한 폰트 설정
#         target_image.save("./save/autumn/" + str(i) + ".png")
#         i+=1

i = 1
for month in winter:
    for day in range(1, days[month-1]+1):
        hbd = "%02d.%02d"%(month, day)
        target_image = Image.open('./nft/winter/' + str(i) + '.png')  # 일단 기본배경폼 이미지를 open 합니다.
        draw = ImageDraw.Draw(target_image)
        draw.text((1430, 2750), hbd, fill="white", font=selectedFont, align='center')  # fill= 속성은 무슨 색으로 채울지 설정,font=는 자신이 설정한 폰트 설정
        target_image.save("./save/winter/" + str(i) + ".png")
        i+=1