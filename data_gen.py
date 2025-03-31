import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import random
import os
from PIL import Image
import io
import pandas as pd

def create_directory(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def draw_circle(ax, x, y, size, color):
    """Draw a circle"""
    circle = plt.Circle((x, y), size/2, color=color)
    ax.add_patch(circle)

def draw_square(ax, x, y, size, color):
    """Draw a square"""
    square = plt.Rectangle((x-size/2, y-size/2), size, size, color=color)
    ax.add_patch(square)

def draw_triangle(ax, x, y, size, color):
    """Draw a triangle"""
    points = [
        (x, y + size/2),
        (x - size/2, y - size/2),
        (x + size/2, y - size/2)
    ]
    triangle = plt.Polygon(points, color=color)
    ax.add_patch(triangle)

def draw_pentagon(ax, x, y, size, color):
    """Draw a pentagon"""
    points = []
    for i in range(5):
        angle = 2 * np.pi * i / 5 - np.pi / 2
        points.append((x + size/2 * np.cos(angle), y + size/2 * np.sin(angle)))
    pentagon = plt.Polygon(points, color=color)
    ax.add_patch(pentagon)

def draw_hexagon(ax, x, y, size, color):
    """Draw a hexagon"""
    points = []
    for i in range(6):
        angle = 2 * np.pi * i / 6
        points.append((x + size/2 * np.cos(angle), y + size/2 * np.sin(angle)))
    hexagon = plt.Polygon(points, color=color)
    ax.add_patch(hexagon)

def generate_image(num_shapes, image_size=300, output_dir="generated_images", index=0):
    """Generate an image with specified number of unique shapes and colors"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Available shapes and their drawing functions
    shape_functions = {
        'circle': draw_circle,
        'square': draw_square,
        'triangle': draw_triangle,
        'pentagon': draw_pentagon,
        'hexagon': draw_hexagon
    }
    
    # Predefined colors
    predefined_colors = {
        'red': 'red',
        'green': 'green',
        'blue': 'blue',
        'yellow': 'yellow',
        'pink': 'pink',
        'black': 'black',
    }
    
    # Predefined positions (middle, top left, top right, bottom left, bottom right)
    positions = {
        "M": (0.5, 0.5),  # middle
        "TL": (0.25, 0.75),  # top left
        "TR": (0.75, 0.75),  # top right
        "BL": (0.25, 0.25),  # bottom left
        "BR": (0.75, 0.25)   # bottom right
    }
    
    # Select random shapes for this image
    shapes = random.sample(list(shape_functions.keys()), num_shapes)
    
    # Select random colors for this image
    color_names = random.sample(list(predefined_colors.keys()), num_shapes)
    colors = [predefined_colors[name] for name in color_names]
    
    selected_positions_keys = random.sample(list(positions.keys()), num_shapes)

    data = {
        "num_shapes": num_shapes,
        **{f"shape_{i}": shapes[i] for i in range(num_shapes)},
        **{f"color_{i}": color_names[i] for i in range(num_shapes)},
        **{f"position_{i}": selected_positions_keys[i] for i in range(num_shapes)}
    }
    
    # Draw each shape
    for i in range(num_shapes):
        # Fixed size for all shapes
        size = 0.2
        
        # Get position
        x, y = positions[selected_positions_keys[i]]
        
        # Draw the shape
        shape_functions[shapes[i]](ax, x, y, size, colors[i])
    
    # Save the image
    filename = f"{output_dir}/image_{num_shapes}_shapes_{index}.png"
    data['filename'] = filename
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=image_size/10)
    plt.close(fig)
    
    return filename, data

def generate_dataset(num_images_per_category=10, output_dir="generated_images"):
    """Generate a dataset of images with varying numbers of shapes"""
    create_directory(output_dir)
    
    generated_files = []

    dict_data = []
    
    # Generate images with 1 to 5 shapes
    for num_shapes in range(1, 6):
        for i in range(num_images_per_category):
            filename, data = generate_image(num_shapes, output_dir=output_dir, index=i)
            dict_data.append(data)
            generated_files.append(filename)
            print(f"Generated: {filename}")

    df = pd.DataFrame(dict_data)
    df.to_csv(f"{output_dir}/data.csv", index=False)
    
    return generated_files, df

# Generate the dataset
if __name__ == "__main__":
    files, df = generate_dataset(num_images_per_category=100)
    print(f"Generated {len(files)} images")
    print(df)
