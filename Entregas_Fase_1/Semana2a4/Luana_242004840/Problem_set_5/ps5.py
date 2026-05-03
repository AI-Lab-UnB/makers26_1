"""
# Problem Set 5
# Name:
# Collaborators:
"""

from PIL import Image, ImageFont, ImageDraw
import numpy


def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    if color == 'red':
        c = [[.567, .433, 0], [.558, .442, 0], [0, .242, .758]]
    elif color == 'green':
        c = [[0.625, 0.375, 0], [0.7, 0.3, 0], [0, 0.142, 0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0], [0, 0.433, 0.567], [0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0], [0, 1, 0.], [0, 0., 1]]
    return c


def matrix_multiply(m1, m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """
    produto = numpy.matmul(m1, m2)
    if type(produto) == numpy.int64:
        return float(produto)
    else:
        return list(produto)


def img_to_pix(filename):
    """
    Takes a filename and converts to a list of pixels.
    Returns the list of pixels.
    Inputs:
        filename: string representing an image file
        returns: list of pixel values
    """
    imagem = Image.open(filename)
    return list(imagem.getdata())


def pix_to_img(pixels_list, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.
    Inputs:
        pixels_list: a list of pixels
        size: a tuple of (width,height)
        mode: 'RGB' or 'L'
    returns:
        img: Image object made from list of pixels
    """
    imagem = Image.new(mode, size)
    imagem.putdata(pixels_list)
    return imagem


def filter(pixels_list, color):
    """
    pixels_list: a list of pixels in RGB form
    color: 'red', 'blue', 'green', or 'none'
    returns: list of pixels transformed by matrix multiplication
    """
    matriz = make_matrix(color)
    pixels_transformados = []
    for pixel in pixels_list:
        resultado = matrix_multiply(matriz, pixel)
        pixels_transformados.append(tuple(int(v) for v in resultado))
    return pixels_transformados


def extract_end_bits(num_end_bits, pixel):
    """
    Extracts the last num_end_bits of each value of a given pixel.
    Inputs:
        num_end_bits: the number of end bits to extract
        pixel: an integer or a tuple of RGB values
    Returns:
        The num_end_bits of pixel, as an integer (BW) or tuple (RGB).
    """
    if isinstance(pixel, tuple):
        return tuple(canal % (2 ** num_end_bits) for canal in pixel)
    else:
        return pixel % (2 ** num_end_bits)


def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image.
    Inputs:
        filename: string, input BW file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    pixels = img_to_pix(filename)
    pixels_revelados = [extract_end_bits(1, p) * 255 for p in pixels]
    imagem = Image.open(filename)
    return pix_to_img(pixels_revelados, imagem.size, 'L')


def reveal_color_image(filename):
    """
    Extracts the 3 LSBs for each pixel in the RGB input image.
    Inputs:
        filename: string, input RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    pixels = img_to_pix(filename)
    fator_escala = 255 / 7
    pixels_revelados = []
    for pixel in pixels:
        bits = extract_end_bits(3, pixel)
        pixels_revelados.append(tuple(int(canal * fator_escala) for canal in bits))
    imagem = Image.open(filename)
    return pix_to_img(pixels_revelados, imagem.size, 'RGB')


def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a
    color image) for each pixel in the input image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return reveal_bw_image(filename)
    elif im.mode == 'RGB':
        return reveal_color_image(filename)
    else:
        raise Exception("Invalid mode %s" % im.mode)


def draw_kerb(filename, kerb):
    """
    Draws the text "kerb" onto the image located at "filename".
    Inputs:
        filename: string, input BW or RGB file
        kerb: string, your kerberos
    """
    im = Image.open(filename)
    font = ImageFont.truetype("noto-sans-mono.ttf", 40)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), kerb, "white", font=font)
    idx = filename.find(".")
    new_filename = filename[:idx] + "_kerb" + filename[idx:]
    im.save(new_filename)
    return


def main():
    pass


if __name__ == '__main__':
    main()