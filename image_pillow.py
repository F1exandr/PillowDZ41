from PIL import Image

def process_image(input_path, output_path):
    # Открываем изображение
    with Image.open(input_path) as img:
        # Поворачиваем изображение на 45 градусов, расширяя границы
        rotated_img = img.rotate(45, expand=True)

        # Уменьшаем размер изображения до 300x300 пикселей
        resized_img = rotated_img.resize((300, 300))

        # Обрезаем верхние 110 пикселей
        width, height = resized_img.size
        cropped_img = resized_img.crop((0, 110, width, height))

        # Сохраняем результат в новый файл
        cropped_img.save(output_path)

if __name__ == "__main__":
    # Укажите путь к вашему изображению
    input_image_path = "input_image.jpg"
    # Укажите путь для сохранения обработанного изображения
    output_image_path = "output_image.jpg"

    process_image(input_image_path, output_image_path)
    print("Изображение обработано и сохранено в", output_image_path)