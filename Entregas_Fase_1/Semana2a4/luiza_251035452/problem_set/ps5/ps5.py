from PIL import Image, ImageDraw
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def make_matrix(color):
    if color == 'red':
        return [[0.567, 0.433, 0],
                [0.558, 0.442, 0],
                [0,     0.242, 0.758]]
    elif color == 'green':
        return [[0.625, 0.375, 0],
                [0.700, 0.300, 0],
                [0,     0.142, 0.858]]
    elif color == 'blue':
        return [[0.950, 0.050, 0],
                [0,     0.433, 0.567],
                [0,     0.475, 0.525]]
    elif color == 'none':
        return [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]

def matrix_multiply(matrix, vector):
    result = []
    for row in matrix:
        total = 0
        for i in range(len(row)):
            total += row[i] * vector[i]
        result.append(total)
    return result

def draw_kerb(filename, kerb):
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), kerb, fill="white")
    output = filename.replace('.', '_kerb.')
    img.save(output)
    print(f"Imagem com kerb salva como {output}")



def img_to_pix(filename):
    img = Image.open(filename)
    return list(img.getdata())


def pix_to_img(pixels_list, size, mode):
    img = Image.new(mode, size)
    img.putdata(pixels_list)
    return img


def filter(pixels_list, color):
    matrix = make_matrix(color)
    resultado = []
    for pixel in pixels_list:
        novo_pixel = matrix_multiply(matrix, pixel)
        resultado.append(tuple(int(v) for v in novo_pixel))
    return resultado


def extract_end_bits(num_end_bits, pixel):
    return pixel % (2 ** num_end_bits)

def reveal_bw_image(filename):
    pixels = img_to_pix(filename)
    tamanho = Image.open(filename).size
    novos_pixels = []
    for pixel in pixels:
        lsb = extract_end_bits(1, pixel)
        novos_pixels.append(lsb * 255)
    return pix_to_img(novos_pixels, tamanho, 'L')


def reveal_color_image(filename):
    pixels = img_to_pix(filename)
    tamanho = Image.open(filename).size
    novos_pixels = []
    for pixel in pixels:
        r = round(extract_end_bits(3, pixel[0]) * 255 / 7)
        g = round(extract_end_bits(3, pixel[1]) * 255 / 7)
        b = round(extract_end_bits(3, pixel[2]) * 255 / 7)
        novos_pixels.append((r, g, b))
    return pix_to_img(novos_pixels, tamanho, 'RGB')


def reveal_image(filename):
    img = Image.open(filename)
    if img.mode == 'L':
        return reveal_bw_image(filename)
    else:
        return reveal_color_image(filename)


# Testes

if __name__ == "__main__":
    # parte 1: filtro de daltonismo
    nome_arquivo = os.path.join(BASE_DIR, 'image_15.png')
    pixels = img_to_pix(nome_arquivo)
    tamanho = Image.open(nome_arquivo).size
    pixels_transformados = filter(pixels, 'red')
    img_nova = pix_to_img(pixels_transformados, tamanho, 'RGB')
    img_nova.save(os.path.join(BASE_DIR, 'image_15_transformada.png'))
    print("Imagem transformada salva como image_15_transformada.png")

    # parte 2: testa extract_end_bits
    print(extract_end_bits(1, 13))  # 1
    print(extract_end_bits(2, 13))  # 1
    print(extract_end_bits(3, 13))  # 5

    # parte 2: revela imagens escondidas
    reveal_image(os.path.join(BASE_DIR, 'hidden1.bmp')).save(os.path.join(BASE_DIR, 'hidden1_revelada.bmp'))
    print("Imagem BW revelada salva como hidden1_revelada.bmp")

    reveal_image(os.path.join(BASE_DIR, 'hidden2.bmp')).save(os.path.join(BASE_DIR, 'hidden2_revelada.bmp'))
    print("Imagem colorida revelada salva como hidden2_revelada.bmp")

   