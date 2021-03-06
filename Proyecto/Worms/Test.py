import os
import glob
from PIL import Image

weapon_images = os.path.join('Resources', 'Weapons', 'Missile.gif')
weapon_list = glob.glob(weapon_images)
for sprite_path in weapon_list:
    nombre_sprite = sprite_path.split('\\')[-1].split('.')
    image = Image.open(sprite_path)
    image = image.convert('RGBA')
    # image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # image = image.transpose(Image.FLIP_TOP_BOTTOM)

    for i in range(0, 360):
        new_image = nombre_sprite[0] + "_" + str(i) + "." + nombre_sprite[1]
        imRotate = image.rotate(i, resample=Image.BICUBIC, expand=0)
        rotated = Image.new('RGBA', imRotate.size, (255, 255, 255, 0))
        # rotated.paste(imRotate, (30, 30), imRotate)
        rotated = Image.composite(rotated, imRotate, rotated)

        # imRotate.show()
        rotated.save(os.path.join('Resources', 'Weapons', nombre_sprite[0], new_image), format='PNG')
