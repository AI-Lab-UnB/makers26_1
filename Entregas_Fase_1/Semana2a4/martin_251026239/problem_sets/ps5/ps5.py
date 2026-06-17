from PIL import Image, ImageFont, ImageDraw
import numpy

def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
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
    """
    product = numpy.matmul(m1, m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result

def img_to_pix(filename):
    """
    Takes a filename and converts to a list of representing pixels.
    """
    img = Image.open(filename)
    pixels = list(img.getdata())
    return pixels

def pix_to_img(pixels_list, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.
    """
    img = Image.new(mode, size)
    img.putdata(pixels_list)
    return img

def filter(pixels_list, color):
    """
    Transforms pixels by matrix multiplication to simulate color blindness.
    """
    matrix = make_matrix(color)
    filtered_pixels = []
    
    for pixel in pixels_list:
        new_pixel = matrix_multiply(matrix, pixel)
        filtered_pixels.append(tuple(int(p) for p in new_pixel))
        
    return filtered_pixels

def extract_end_bits(num_end_bits, pixel):
    """
    Extracts the last num_end_bits of each value of a given pixel.
    """
    divisor = 2 ** num_end_bits
    
    if isinstance(pixel, int):
        return pixel % divisor
    else:
        return tuple(p % divisor for p in pixel)

def reveal_bw_image(filename):
    """
    Extracts the single LSB for each pixel in the BW input image. 
    """
    img = Image.open(filename)
    pixels = list(img.getdata())
    
    revealed_pixels = []
    for p in pixels:
        extracted = extract_end_bits(1, p)
        scaled = extracted * 255
        revealed_pixels.append(scaled)
        
    return pix_to_img(revealed_pixels, img.size, img.mode)

def reveal_color_image(filename):
    """
    Extracts the 3 LSBs for each pixel in the RGB input image. 
    """
    img = Image.open(filename)
    pixels = list(img.getdata())
    
    revealed_pixels = []
    for p in pixels:
        extracted = extract_end_bits(3, p)
        scaled = tuple((val * 255) // 7 for val in extracted)
        revealed_pixels.append(scaled)
        
    return pix_to_img(revealed_pixels, img.size, img.mode)

def reveal_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 3 LSBs (for a color image).
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
    Draws the text "kerb" onto the image located at "filename".
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
    im = Image.open('image_15.png')
    width, height = im.size
    pixels = img_to_pix('image_15.png')

    non_filtered_pixels = filter(pixels,'none')
    im = pix_to_img(non_filtered_pixels, (width, height), 'RGB')

    red_filtered_pixels = filter(pixels,'red')
    im2 = pix_to_img(red_filtered_pixels,(width,height), 'RGB')

    im = reveal_image('hidden1.bmp')

    im2 = reveal_image('hidden2.bmp')
    
if __name__ == '__main__':
    main()