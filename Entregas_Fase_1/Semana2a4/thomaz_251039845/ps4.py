# Problem Set - Colorblindness Filters
# Name: [Thomaz]
# Collaborators: 
# Time spent: 

from PIL import Image
import numpy as np


def get_color_matrix(color):
    if color == 'red': 
        return np.array([
            [0.567, 0.433, 0.000],
            [0.558, 0.442, 0.000],
            [0.000, 0.242, 0.758]
        ])
    elif color == 'green':  
        return np.array([
            [0.625, 0.375, 0.000],
            [0.700, 0.300, 0.000],
            [0.000, 0.300, 0.700]
        ])
    elif color == 'blue': 
        return np.array([
            [0.950, 0.050, 0.000],
            [0.000, 0.433, 0.567],
            [0.000, 0.475, 0.525]
        ])
    else:  
        return np.array([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ])


def img_to_pixels(filename):
    img = Image.open(filename)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())
    return pixels, (width, height), img.mode

def pixels_to_img(pixels_list, size, mode='RGB'):
    img = Image.new(mode, size)
    img.putdata(pixels_list)
    
    return img

def apply_filter(pixels_list, color):
    transform_matrix = get_color_matrix(color)
    
    transformed_pixels = []
    
    for pixel in pixels_list:
        pixel_array = np.array(pixel, dtype=np.float32)
        transformed = np.dot(transform_matrix, pixel_array)
        transformed = np.clip(transformed, 0, 255)
        transformed_pixel = tuple(int(round(x)) for x in transformed)
        transformed_pixels.append(transformed_pixel)
    
    return transformed_pixels

def process_image(filename, color, output_filename=None):
    pixels, size, mode = img_to_pixels(filename)
    transformed_pixels = apply_filter(pixels, color)
    new_img = pixels_to_img(transformed_pixels, size, mode)
    
    if output_filename:
        new_img.save(output_filename)
        print(f"Imagem salva como: {output_filename}")
    
    return new_img

if __name__ == "__main__":
    test_image = "skimage_15.png"
    for color_type in ['red', 'green', 'blue', 'none']:
        output_name = f"output_{color_type}.png"
        try:
            process_image(test_image, color_type, output_name)
            print(f"Processado: {color_type} -> {output_name}")
        except FileNotFoundError:
            print(f"Arquivo {test_image} não encontrado. Pulei o teste.")
            break