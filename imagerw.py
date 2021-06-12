from PIL import Image


def convert_image_into_array(image_file):
    image = Image.open(image_file)
    gray = image.convert('L')
    bw = gray.point(lambda x: 0 if x > 128 else 1, '1')
    data = list(bw.getdata())
    return data



