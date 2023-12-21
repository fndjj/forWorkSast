from PIL import Image
import math
# Расчеты
def math_img(img1_path,img2_path,mode):
    with Image.open(img2_path) as img:
        img = img.convert('RGB')
    print( "Информационная энтропия конечного изображения: " + str(H(img,10000)))
    print("Среднее изменение интенсивности: " + str(get_uaci(img1_path,img2_path)))
    print("Процент измененных пикселей: " + str(get_npcr(img1_path,img2_path)))
    print("Рассчитанная корреляция: " + str(get_coff_corelation(img2_path,mode)))
#Расчет информационной энтропии
def H(img, Size):
    counts = {}
    z = 0
    zz = 0
    for i in range(Size):
        c = img.getpixel((i % img.width, i // img.width))
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    for x in counts:
        z = counts[x]
        zz += z / Size * math.log(Size / counts[x], 2)
    return zz
#Расчет среднего изменения интенсивности
def get_uaci(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    result = .0
    image1 = image1.convert("P")
    image2 = image2.convert("P")
    bright_sum = .0
    for x in range(image1.width):
        for y in range(image1.height):
            bright_sum += abs(image1.getpixel((x,y)) - image2.getpixel((x,y)))/256
    result = bright_sum / (image1.height * image1.width)
    return result * 100
# Расчет процента измененных пикселей
def get_npcr(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    result = .0
    changed_pixels_count = 0
    for x in range(image1.width):
        for y in range(image1.height):
            if image1.mode == "P":
                if image1.getpixel((x,y)) != image2.getpixel((x,y)):
                    changed_pixels_count += 1
            else:
                if sum(image1.getpixel((x,y))[:2])/3 != sum(image2.getpixel((x,y))[:2])/3:
                    changed_pixels_count += 1
    result = changed_pixels_count / (image1.height * image1.width)
    return result * 100
# Расчет корреляции
def get_coff_corelation(picturePath, mode=0):
    im = Image.open(picturePath).convert("RGB")
    width = im.size[0]
    height = im.size[1]
    sum_xy = 0
    D = 0
    avg_b = get_avg_bright(picturePath)
    if mode == 0:
        endW = width - 1
        endH = height
        shamt_x = 1
        shamt_y = 0
    elif mode == 1:
        endW = width
        endH = height - 1
        shamt_x = 0
        shamt_y = 1
    else:
        endW = width - 1
        endH = height - 1
        shamt_x = 1
        shamt_y = 1
    for x in range(0, endW):
        for y in range(0, endH):
            pixels_x = im.getpixel((x, y))
            pixels_y = im.getpixel((x + shamt_x, y + shamt_y))
            pixels_x_b = get_brights(pixels_x)
            pixels_y_b = get_brights(pixels_y)
    sum_xy += (pixels_x_b - avg_b) * (pixels_y_b - avg_b)
    for x in range(0, width):
        for y in range(0, height):
            pixels_x = im.getpixel((x, y))
            pixels_x_b = get_brights(pixels_x)
            D += (pixels_x_b - avg_b) ** 2
    return sum_xy / D
def get_avg_bright(picturePath):
    im = Image.open(picturePath).convert("RGB")
    width = im.size[0]
    height = im.size[1]
    all_pixels_count = width * height
    sum_a = 0
    for x in range(0, width):
        for y in range(0, height):
            pixels = im.getpixel((x, y))
            sum_a += get_brights(pixels)
    return sum_a / all_pixels_count
def get_brights(pixels):
    return 0.299 * pixels[0] + 0.587 * pixels[1] + 0.114 * pixels[2]

