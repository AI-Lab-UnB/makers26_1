from PIL import Image

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
    img = Image.open(filename)
    return list(img.getdata())

def pix_to_img(pixels_list, size, mode):
    img = Image.new(mode, size)
    img.putdata(pixels_list)
    return img

def filter(pixels_list, color):
    matrix = make_matrix(color)
    transformed = []
    
    for pixel in pixels_list:
        res = matrix_multiply(matrix, pixel)
        transformed.append((int(res[0]), int(res[1]), int(res[2])))
        
    return transformed

def extract_end_bits(num_end_bits, pixel):
    return pixel % (2 ** num_end_bits)

def reveal_bw_image(filename):
    img = Image.open(filename)
    pixels = list(img.getdata())
    size = img.size
    
    new_pixels = []
    for p in pixels:
        val = extract_end_bits(1, p)
        new_pixels.append(val * 255)
        
    return pix_to_img(new_pixels, size, 'L')

def reveal_color_image(filename):
    img = Image.open(filename)
    pixels = list(img.getdata())
    size = img.size
    
    new_pixels = []
    for r, g, b in pixels:
        new_r = extract_end_bits(3, r)
        new_g = extract_end_bits(3, g)
        new_b = extract_end_bits(3, b)
        
        rescaled_r = int(new_r * (255 / 7))
        rescaled_g = int(new_g * (255 / 7))
        rescaled_b = int(new_b * (255 / 7))
        
        new_pixels.append((rescaled_r, rescaled_g, rescaled_b))
        
    return pix_to_img(new_pixels, size, 'RGB')

def reveal_image(filename):
    img = Image.open(filename)
    if img.mode == 'L' or img.mode == '1':
        return reveal_bw_image(filename)
    elif img.mode == 'RGB':
        return reveal_color_image(filename)