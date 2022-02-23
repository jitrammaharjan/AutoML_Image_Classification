import os
from os import walk


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TRAINING_IMAGES_PATH = 'XXXXXXXXXX'  # your local path
STORAGE_PATH = 'XXXXXXXXXX' # your cloud storage bucket path


def get_image_paths(images_root):
    f = []
    for (dirpath, dirnames, filenames) in walk(images_root):
        for filename in filenames:
            if filename.endswith('.jpg') or filename.endswith('.png'):
                full_path = os.path.join(dirpath, filename)
                f.append(full_path)
    return f

def build_tag_name(file_path):
    dir = os.path.dirname(file_path)                          
    tag = os.path.basename(dir)                               
    return tag
                
if __name__ == '__main__':
    tag_overlay_file = os.path.join(PROJECT_ROOT, 'tags.csv')

    with open(tag_overlay_file, 'w') as f:
        image_paths = get_image_paths(TRAINING_IMAGES_PATH)

        for image_path in image_paths:
            tag = build_tag_name(image_path)                                                                     
            image_name = os.path.basename(image_path)
            storage_blob_path = os.path.join(STORAGE_PATH, tag, image_name)      
            print(f'{image_path},{tag}')
            print(f'{storage_blob_path},{tag}')
            f.write(f'{storage_blob_path},{tag}\n')
            print('')
