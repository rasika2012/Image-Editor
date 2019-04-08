from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def makePost(image, article, font_path = './Fonts/Mata.TTF', font_size = 60,\
             location = (0, 0),
             color = (0, 0, 0),
             tmp_out= './tmp.bmp'):
    image_object = Image.open(image)
    image_object = image_object.resize((2000,int(image_object.size[1]*2000/image_object.size[0])))
    draw_object = ImageDraw.Draw(image_object)
    font_family = ImageFont.truetype(font_path, font_size)

    #print(color)
    draw_object.text(location, article, color, font=font_family)
    image_object.save(tmp_out)

    low_w = 700
    low_h = 700
    if (image_object.size[0]>image_object.size[1]):
        low_q = image_object.resize((500,int(image_object.size[1] * 500 / image_object.size[0])))
    else:
        low_q = image_object.resize((int(image_object.size[0] * 700 / image_object.size[1]), 700))

    low_q.save('./low.bmp')


# print(image_object)

def save(path):
    image_object = Image.open('./tmp.bmp')
    image_object.save(path)


def add_tag(image='./tmp.bmp', tag_path='./Tag/tag.png', author="", font_size=10, color=(0, 0, 0),font='./Fonts/Mata.TTF'):
    image_object = Image.open(image)
    image_tag = Image.open('./Tag/tag.png')

    width, height = image_object.size
    # print(width,height)

    tag_width, tag_height = image_tag.size
    height = height * tag_width / width
    image_object = image_object.resize((tag_width, int(height)))
    image_object.paste(image_tag, (0, int(height - tag_height)))

    draw_object = ImageDraw.Draw(image_object)
    image_object.save(image)
    low_q = image_object.resize((int(image_object.size[0] * 500 / image_object.size[1]), 500))
    low_q.save('./low.bmp')
    makePost(image, author, font_size=font_size, location=(90, int(height - (tag_height*1.5))), color=color,font_path=font)
