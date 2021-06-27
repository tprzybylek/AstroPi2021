# TODO: add imports and path variables
# generates pairs of images and masks for further processing using TensorFlow CNNs

folders = ['train_frames', 'train_masks', 'val_frames', 'val_masks', 'test_frames', 'test_masks']

for folder in folders:
  # os.makedirs(current_dir / 'preprocessing/learn' / folder)
  pass

# Get all frames and masks, sort them, shuffle them to generate data sets.
all_frames = os.listdir(output_dir_a)
all_masks = os.listdir(output_dir_m)

all_frames.sort(key=lambda var:[int(x) if x.isdigit() else x 
                                for x in re.findall(r'[^0-9]|[0-9]+', var)])
all_masks.sort(key=lambda var:[int(x) if x.isdigit() else x 
                               for x in re.findall(r'[^0-9]|[0-9]+', var)])

random.seed(230)
random.shuffle(all_frames)

# Generate train, val, and test sets for frames
train_split = int(0.7*len(all_frames))
val_split = int(0.9 * len(all_frames))

train_frames = all_frames[:train_split]
val_frames = all_frames[train_split:val_split]
test_frames = all_frames[val_split:]

# Generate corresponding mask lists for masks
train_masks = [f for f in all_masks if f in train_frames]
val_masks = [f for f in all_masks if f in val_frames]
test_masks = [f for f in all_masks if f in test_frames]

#Add train, val, test frames and masks to relevant folders
def add_frames(dir_name, image):
  
  img = Image.open(output_dir_a / image)
  img.save(str(current_dir / 'preprocessing/learn') + ('/{}'.format(dir_name)+'/'+image))
  
def add_masks(dir_name, image):
  
  img = Image.open(output_dir_m / image)
  img.save(str(current_dir / 'preprocessing/learn') + ('/{}'.format(dir_name)+'/'+image))

frame_folders = [(train_frames, 'train_frames'), (val_frames, 'val_frames'), 
                 (test_frames, 'test_frames')]

mask_folders = [(train_masks, 'train_masks'), (val_masks, 'val_masks'), 
                (test_masks, 'test_masks')]

# Add frames
for folder in frame_folders:
  
  array = folder[0]
  name = [folder[1]] * len(array)

  list(map(add_frames, name, array))
         
# Add masks
for folder in mask_folders:
  
  array = folder[0]
  name = [folder[1]] * len(array)
  
  list(map(add_masks, name, array))
        
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
        
val_datagen = ImageDataGenerator(rescale=1./255)

train_image_generator = train_datagen.flow_from_directory(
    current_dir / 'preprocessing/learn' / 'train_frames',
    batch_size = 4
)

train_mask_generator = train_datagen.flow_from_directory(
    current_dir / 'preprocessing/learn' / 'train_masks',
    batch_size = 4
)

val_image_generator = val_datagen.flow_from_directory(
    current_dir / 'preprocessing/learn' / 'val_frames',
    batch_size = 4
)

val_mask_generator = val_datagen.flow_from_directory(
    current_dir / 'preprocessing/learn' / 'val_masks',
    batch_size = 4
)

train_generator = zip(train_image_generator, train_mask_generator)
val_generator = zip(val_image_generator, val_mask_generator)
