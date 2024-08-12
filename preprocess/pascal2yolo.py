import os
import random
import xml.etree.ElementTree as ET
from shutil import copy2

# Paths
base_dir = '/content/drive/MyDrive/small-weak-UVA-object-dataset'  # Replace with your dataset path
annotations_dir = os.path.join(base_dir, 'Annotations')
images_dir = os.path.join(base_dir, 'JPEGImages')
output_base_dir = '/content/drive/MyDrive/uavod10'  # Replace with your desired output path

# Create directories for YOLO dataset
yolo_dir = os.path.join(output_base_dir, 'YOLO')
train_dir = os.path.join(yolo_dir, 'train')
val_dir = os.path.join(yolo_dir, 'val')
test_dir = os.path.join(yolo_dir, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Create subdirectories for images and labels
for subdir in ['images', 'labels']:
    os.makedirs(os.path.join(train_dir, subdir), exist_ok=True)
    os.makedirs(os.path.join(val_dir, subdir), exist_ok=True)
    os.makedirs(os.path.join(test_dir, subdir), exist_ok=True)

# Conversion function
def convert_bbox(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# Parse XML and convert
def convert_annotation(image_id, split):
    annotation_file = os.path.join(annotations_dir, f'{image_id}.xml')
    out_file = os.path.join(yolo_dir, split, 'labels', f'{image_id}.txt')
    
    # Skip files that do not exist or are not XML files
    if not os.path.isfile(annotation_file) or not annotation_file.endswith('.xml'):
        return

    tree = ET.parse(annotation_file)
    root = tree.getroot()
    
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    
    with open(out_file, 'w') as f:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls == "building":
                cls_id = 0
            elif cls == "prefabricated-house":
                cls_id = 1
            else:
                continue
            
            difficult = obj.find('difficult').text
            if int(difficult) == 1:
                continue
            
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('xmax').text),
                 int(xmlbox.find('ymin').text), int(xmlbox.find('ymax').text))
            bb = convert_bbox((w, h), b)
            f.write(f"{cls_id} " + " ".join([f"{a:.6f}" for a in bb]) + '\n')

# Split the dataset
def split_dataset():
    # Only consider files with .xml extension
    image_ids = [os.path.splitext(f)[0] for f in os.listdir(images_dir) if f.endswith('.jpg')]
    random.shuffle(image_ids)
    
    train_split = int(0.7 * len(image_ids))
    val_split = int(0.9 * len(image_ids))
    
    train_ids = image_ids[:train_split]
    val_ids = image_ids[train_split:val_split]
    test_ids = image_ids[val_split:]
    
    for image_id in train_ids:
        convert_annotation(image_id, 'train')
        copy2(os.path.join(images_dir, f'{image_id}.jpg'), os.path.join(train_dir, 'images'))
        
    for image_id in val_ids:
        convert_annotation(image_id, 'val')
        copy2(os.path.join(images_dir, f'{image_id}.jpg'), os.path.join(val_dir, 'images'))
        
    for image_id in test_ids:
        convert_annotation(image_id, 'test')
        copy2(os.path.join(images_dir, f'{image_id}.jpg'), os.path.join(test_dir, 'images'))

# Run the script
if __name__ == '__main__':
    split_dataset()
    print("Conversion and splitting completed successfully.")