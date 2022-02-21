from PIL import Image, ImageDraw, ImageFont

spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def save(season, list):
    i = 1
    for month in list:
        for day in range(1, days[month - 1] + 1):
            hbd = "%02d.%02d" % (month, day)
            path = './'+season+'/images/' + str(i) + '.png'
            save = './images/' + hbd + '.png'
            target_image = Image.open(path)
            target_image.save(save)
            i += 1

save("spring", spring)
save("summer", summer)
save("autumn", autumn)
save("winter", winter)