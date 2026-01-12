import os
from PIL import Image
import pillow_heif
import concurrent.futures

input_dir = "heic_converter_png/heic_files"  # From parent dir
output_dir = "heic_converter_png/converted_png"

# Create output folder
os.makedirs(output_dir, exist_ok=True)

# Find all .heic files
heic_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.heic')]



def convert_function(heic_file):
    print(f"Converting {heic_file}...")
    
    # Read HEIC
    # heif_file = pillow_heif.read_heif(heic_file)
    heif_file = pillow_heif.read_heif(os.path.join(input_dir, heic_file))  # Full path

    
    # Convert to PIL Image
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    
    # Save as PNG
    png_file = os.path.splitext(heic_file)[0] + '.png'
    image.save(os.path.join(output_dir, png_file))
    
    print(f"Saved: {png_file}")
    
with concurrent.futures.ThreadPoolExecutor() as executer:
    time_taken=[executer.submit(convert_function, heic_file) for heic_file in heic_files]    

print("All done!")
