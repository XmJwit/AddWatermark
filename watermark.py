# coding:utf-8
# 请预先导入：
# pip install pillow

from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image, text):
 font = ImageFont.truetype('‪C:\Windows\Fonts\msyh.ttc', 36)

 # 添加背景
 new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
 new_img.paste(image, image.size)

 # 添加水印
 font_len = len(text)
 rgba_image = new_img.convert('RGBA')
 text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
 image_draw = ImageDraw.Draw(text_overlay)

 for i in range(0, rgba_image.size[0], font_len*40+100):
  for j in range(0, rgba_image.size[1], 200):
   image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 50))
 text_overlay = text_overlay.rotate(-45)
 image_with_text = Image.alpha_composite(rgba_image, text_overlay)

 # 裁切图片
 image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
 return image_with_text


if __name__ == '__main__':
 img = Image.open("test.jpg")   # 当前目录下的test.jpg
 im_after = add_text_to_image(img, u'该图片仅用于U-file实名认证') # 水印
 im_after.save(u'test_success.png') # 保存后的图片文件，后缀必须为.png
 
 imgnew = im_after.convert('RGB')
 imgnew.save('test_jpg.jpg')   # 后缀非.png ，可为.jpg等等
