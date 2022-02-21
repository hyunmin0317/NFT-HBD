from PIL import Image

#이미지 파일 오픈
background = Image.open("01.01.png")
foreground = Image.open("1.png")

#배경이 투명한 이미지 파일의 사이즈 가져오기
foreground = foreground.resize((4086, 4086))

#print(foreground.size)
#print("img_h : " , img_h , "img_w : ", img_w)

#합성할 배경 이미지를 위의 파일 사이즈로 resize

#이미지 합성
background.paste(foreground, (0, 0), foreground)

#합성한 이미지 파일 보여주기
background.show()
