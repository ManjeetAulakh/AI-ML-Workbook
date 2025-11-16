import os
import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# --- Define Base Directories ---
base_dir = './images_dataSAT'
dir_non_agri = os.path.join(base_dir, 'class_0_non_agri')
dir_agri = os.path.join(base_dir, 'class_1_agri')

## Task 1: Determine the shape (dimensions) of a single image stored in the image_data variable.

# This task typically assumes you have loaded the first image's data into 'image_data'.
# We will simulate this by loading one image from the non-agricultural directory.

# 1. Get a list of all non-agri image paths
non_agri_files = glob.glob(os.path.join(dir_non_agri, '*.png'))

# Check if the list is not empty
if not non_agri_files:
    print("Error: No images found in the non-agricultural directory.")
else:
    # 2. Load the first image using PIL (Pillow)
    first_image_path = non_agri_files[0]
    img = Image.open(first_image_path)
    
    # 3. Convert to a numpy array (as is common for 'image_data')
    image_data = np.array(img)
    
    print(f"--- Task 1 Output ---")
    print(f"Shape (dimensions) of the image_data variable: {image_data.shape}")
    print("-----------------------")


## Task 2: Display the first four images in the './images_dataSAT/class_0_non_agri/' directory.

# 1. Get the first four image paths (assuming glob's result is consistent or just taking the first few)
display_non_agri_paths = non_agri_files[:4]

print(f"\n--- Task 2 Output: Displaying first 4 non-agri images ---")
if len(display_non_agri_paths) == 0:
    print("Not enough images to display 4 non-agri samples.")
else:
    plt.figure(figsize=(10, 3))
    for i, img_path in enumerate(display_non_agri_paths):
        # Load the image
        img = Image.open(img_path)
        
        # Plot the image
        plt.subplot(1, 4, i + 1)
        plt.imshow(img)
        plt.title(f"Non-Agri {i+1}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()
print("-----------------------")


## Task 3: Create a list named agri_images_paths that contains the full file paths of all images
## located in the dir_agri directory. Sort the list before saving it.

# 1. Use glob to find all image files in the agricultural directory
# Note: '*.png' is assumed based on common satellite image formats and the task's context.
agri_images_paths = glob.glob(os.path.join(dir_agri, '*.png'))

# 2. Sort the list
agri_images_paths.sort()

print(f"\n--- Task 3 Output ---")
print(f"Total number of agricultural image paths found: {len(agri_images_paths)}")
print(f"First 5 sorted paths:")
for path in agri_images_paths[:5]:
    print(f"  {path}")
print("-----------------------")


## Task 4: Determine the number of images of agricultural land that exist in the 
## './images_dataSAT/class_1_agri/' directory.

# The count is simply the length of the list created in Task 3
num_agri_images = len(agri_images_paths)

print(f"\n--- Task 4 Output ---")
print(f"Number of agricultural images: {num_agri_images}")
print("-----------------------")


## Task 5: Display the first four images of the agricultural land.

# 1. Get the first four image paths from the sorted list
display_agri_paths = agri_images_paths[:4]

print(f"\n--- Task 5 Output: Displaying first 4 agri images ---")
if len(display_agri_paths) < 4:
    print("Not enough agricultural images to display 4 samples.")
else:
    plt.figure(figsize=(10, 3))
    for i, img_path in enumerate(display_agri_paths):
        # Load the image
        img = Image.open(img_path)
        
        # Plot the image
        plt.subplot(1, 4, i + 1)
        plt.imshow(img)
        plt.title(f"Agri {i+1}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()
print("-----------------------")