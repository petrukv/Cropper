from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

print("Початок розділення зображення ...")

general_image = Image.open('images.png')

image_width, image_height = general_image.size

image_size = 28

num_rows_per_clothing = 3
num_columns_per_clothing = 10
total_clothing_types = 10

x_pos, y_pos = 0, 0

clothing_names = [
    "Футболка/топ", "Брюки", "Кофта", "Сукня", "Пальто",
    "Сандалі", "Сорочка", "Кросівки", "Сумка", "Капці"
]

for clothing_index, clothing_name in enumerate(clothing_names):
    create_folder_if_not_exists(clothing_name)

    for row in range(num_rows_per_clothing):
        for col in range(num_columns_per_clothing):
            box = (x_pos, y_pos + image_size, y_pos + image_size)
            clothing_image = general_image.crop(box)

            image_filename = f"{clothing_name}/{row}_{col}.png"
            clothing_image.save(image_filename)

            print(f"Збережено: {image_filename}")

            x_pos += image_size

        x_pos = 0
        y_pos += image_size

    if (clothing_index + 1) % total_clothing_types == 0:
        x_pos = 0
        y_pos = 0

print("Розділення зображення завершено.")
