import os
import shutil

# Folder containing original .txt files (training0)
source_folder = r'path\ComfyUI\custom_nodes\comfyui-inspire-pack\prompts\[promptfolder]'

# Parent directory (prompts)
parent_folder = os.path.dirname(source_folder)

# Number of folders to create
num_folders = 25

# Create destination folders in parent directory
folders = []
for i in range(1, num_folders + 1):
    folder_path = os.path.join(parent_folder, f'folder_{i:02d}')
    os.makedirs(folder_path, exist_ok=True)
    folders.append(folder_path)

# Get .txt files from source folder
txt_files = [file for file in os.listdir(source_folder) if file.endswith('.txt')]

# Distribute and modify files evenly among folders
for idx, file_name in enumerate(txt_files):
    # Determine destination folder
    dest_folder = folders[idx % num_folders]

    # Paths
    src_file_path = os.path.join(source_folder, file_name)
    dest_file_path = os.path.join(dest_folder, file_name)

    # Move the file
    shutil.move(src_file_path, dest_file_path)

    # Modify file by adding negative line
    with open(dest_file_path, 'a', encoding='utf-8') as file:
        file.write('\nnegative:blurry_woman, nose_ring, nostril_ring, nose_piercing, watermark, text, owl, tattoos, cartoon, drawing, animation, 2d, small_breasts, small_butt, small_hips, big_waist, nude, naked, nipples, fat, obese, overweight, dark_skin, big_smile, ugly\n')

# Rename files sequentially in each folder
for folder_path in folders:
    txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')])

    for idx, old_file_name in enumerate(txt_files, start=1):
        old_file_path = os.path.join(folder_path, old_file_name)
        new_file_path = os.path.join(folder_path, f'prompt{idx}.txt')

        os.rename(old_file_path, new_file_path)

print("Distribution, modification, and renaming completed successfully.")
