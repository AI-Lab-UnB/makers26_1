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
    # You do not need to understand exactly how this function works.
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

    product = numpy.matmul(m1, m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def img_to_pix(filename):
    image = Image.open(filename)
    return list(image.getdata())


def pix_to_img(pixels_list, size, mode):
    image = Image.new(mode, size)
    image.putdata(pixels_list)
    return image


def filter(pixels_list, color):
    matrix = make_matrix(color)
    filtered_pixels = []
    
    for pixel in pixels_list:
        transformed = matrix_multiply(matrix, pixel)
        
        pixel_tuple = tuple(int(x) for x in transformed)
        filtered_pixels.append(pixel_tuple)
    
    return filtered_pixels


def extract_end_bits(num_end_bits, pixel):
    divider = 2**num_end_bits
    
    if isinstance(pixel, tuple):
        return tuple(p % divider for p in pixel)
    else:
        return pixel % divider 


def reveal_bw_image(filename):
    pixels = img_to_pix(filename)
    image = Image.open(filename)
    
    revealed_pixels = []
    for p in pixels:
        revealed_pixels.append(extract_end_bits(1, p) * 255)
    
    return pix_to_img(revealed_pixels, image.size, 'L')

def reveal_color_image(filename):
    pixels = img_to_pix(filename)
    image = Image.open(filename)
    
    revealed_pixels = []
    for p in pixels:
        extracted = extract_end_bits(3, p)
        
        rescaled = tuple(val * 36 for val in extracted)
        revealed_pixels.append(rescaled)
    
    return pix_to_img(revealed_pixels, image.size, 'RGB')


def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a 
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    im = Image.open(filename)
    if im.mode == '1' or im.mode == 'L':
        return(reveal_bw_image(filename))
    elif im.mode == 'RGB':
        return(reveal_color_image(filename))
    else:
        raise Exception("Invalid mode %s" % im.mode)


def draw_kerb(filename, kerb):
    """
    Draws the text "kerb" onto the image located at "filename" and returns a PDF.
    Inputs:
        filename: string, input BW or RGB file
        kerb: string, your kerberos
    Output:
        Saves output image to "filename_kerb.xxx"
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
    im = Image.open('Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_5/image_15.png')
    width, height = im.size
    pixels = img_to_pix('Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_5/image_15.png')

    non_filtered_pixels = filter(pixels,'none')
    im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')
    im.show()

    red_filtered_pixels = filter(pixels,'red')
    im2 = pix_to_img(red_filtered_pixels,(width,height), 'RGB')
    im2.show()

    im = reveal_image('Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_5/hidden1.bmp')
    im.show()

    im2 = reveal_image('Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_5/hidden2.bmp')
    im2.show()
    

if __name__ == '__main__':
    main()
