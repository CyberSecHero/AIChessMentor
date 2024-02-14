import os
import cairosvg

# Directory containing SVG files
svg_directory = "pieces/svg"

# Directory to save PNG files
png_directory = "pieces/png"

# Create the PNG directory if it doesn't exist
os.makedirs(png_directory, exist_ok=True)

# Loop through SVG files in the directory
for filename in os.listdir(svg_directory):
    if filename.endswith(".svg"):
        # Construct the full path to the SVG file
        svg_path = os.path.join(svg_directory, filename)
        
        # Construct the full path to save the PNG file
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(png_directory, png_filename)
        
        # Convert SVG to PNG
        cairosvg.svg2png(url=svg_path, write_to=png_path)
        
        print(f"Converted {filename} to {png_filename}")
