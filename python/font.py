from PIL import Image, ImageDraw, ImageFont

target_image = Image.open('src.png')  # 일단 기본배경폼 이미지를 open 합니다.
selectedFont = ImageFont.truetype('font.ttf', 1200)  # 폰트경로과 사이즈를 설정해줍니다.
draw = ImageDraw.Draw(target_image)
keyword = "03.17"
draw.text((1430, 2750), keyword, fill = "white", font = selectedFont, align = 'center')  # fill= 속성은 무슨 색으로 채울지 설정,font=는 자신이 설정한 폰트 설정
target_image.save("save.png")  # 편집된 이미지를 저장합니다.