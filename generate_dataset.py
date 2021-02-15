from pathlib import Path
import csv

current_dir = Path(__file__).parent.absolute()
input_dir = current_dir / 'preprocessing/stacked/'
crop_dir = current_dir / 'preprocessing/crops/'
output_dir = current_dir / 'preprocessing/stacked_cropped'


# Return a list of regular files only, not directories
cropfiles_list = [f for f in crop_dir.glob('**/*') if f.is_file()]



for cropfile in cropfiles_list:
    with open(cropfile) as cf:
        reader = csv.reader(cf, delimiter=',')
