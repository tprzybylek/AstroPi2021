from pathlib import Path
import csv
import numpy
from PIL import Image


current_dir = Path(__file__).parent.absolute()
input_dir = current_dir / 'preprocessing/stacked/'
crop_dir = current_dir / 'preprocessing/crops/'
output_dir_a = current_dir / 'preprocessing/learn_a'
output_dir_m = current_dir / 'preprocessing/learn_m'

cropfiles_list = [f for f in crop_dir.glob('**/*') if f.is_file()]


def crop_image(input_array, size, x_start, y_start, filename, index):
    if len(input_array.shape) == 3:
        array_extract = input_array[y_start:y_start+size,x_start:x_start+size,:]
        output_image = Image.fromarray(array_extract.astype('uint8'), 'RGB')
        output_image.save(output_dir_a / (filename + '_' + index + '.tif'))
    else:
        array_extract = input_array[y_start:y_start+size,x_start:x_start+size]
        output_image = Image.fromarray(array_extract.astype('uint8'), 'L')
        output_image.save(output_dir_m / (filename + '_' + index + '.tif'))


for cropfile in cropfiles_list:
    im_filename = cropfile.name.split('.')[0]
    print(im_filename)

    with open(cropfile) as cf:
        reader = csv.reader(cf, delimiter=',')

        im_a = Image.open(input_dir / (im_filename + '_a.tif'))
        im_a_array = numpy.array(im_a)

        im_m = Image.open(input_dir / (im_filename + '_m.tif'))
        im_m_array = numpy.array(im_m)

        ## normalize mask array
        for ix,iy in numpy.ndindex(im_m_array.shape):
            if im_m_array[ix,iy] in [111, 112, 113, 114, 115, 116]:
                im_m_array[ix,iy] = 1
            elif im_m_array[ix,iy] in [121, 122, 123, 124, 125, 126]:
                im_m_array[ix,iy] = 2
            elif im_m_array[ix,iy] in [20, 30]:
                im_m_array[ix,iy] = 3
            elif im_m_array[ix,iy] == 60:
                im_m_array[ix,iy] = 4
            elif im_m_array[ix,iy] == 40:
                im_m_array[ix,iy] = 5
            elif im_m_array[ix,iy] == 50:
                im_m_array[ix,iy] = 6
            elif im_m_array[ix,iy] == 70:
                im_m_array[ix,iy] = 7
            elif im_m_array[ix,iy] in [90, 100]:
                im_m_array[ix,iy] = 8
            elif im_m_array[ix,iy] in [80, 200]:
                im_m_array[ix,iy] = 9
            else:
                im_m_array[ix,iy] = 0

        for row in reader:
            print(row)
            crop_image(im_a_array, int(row[1]), int(row[2]), int(row[3]), im_filename, row[0])
            crop_image(im_m_array, int(row[1]), int(row[2]), int(row[3]), im_filename, row[0])
