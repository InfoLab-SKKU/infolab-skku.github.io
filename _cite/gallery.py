import os

def get_all_pictures(directory):
    # Supported image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    images = []

    for filename in os.listdir(directory):
        _, ext = os.path.splitext(filename)
        if ext.lower() in image_extensions:
            images.append(filename)

    return images

def generate_gallery(images, image_folder="images/gallery"):
    header = """---
title: Team photos
---
{% include breadcrumbs.html %}

# {% include icon.html icon="fa-solid fa-users" %}Team photos

MORE COMING SOON! Until then, check out some older photos on [our old lab website](https://infolab.skku.edu/gallery/).

{% include section.html %}

{% capture content %}
"""

    figures = ""
    for img in images:
        figure = f"""\n{{%
  include figure.html
  image="{image_folder}/{img}"
  link="{image_folder}/{img}"
  caption="{os.path.splitext(img)[0].replace('_', ' ').title()}"
  width="300px"
%}}\n"""
        figures += figure

    footer = """
{% endcapture %}

{% include grid.html style="square" content=content %}
"""

    return header + figures + footer

if __name__ == "__main__":
    directory = input("Enter the directory (default: images/gallery/2025): ").strip() or "images/gallery/2025"
    output_file = input("Enter the output file name (default: 2025.md): ").strip() or "2025.md"

    pictures = get_all_pictures(directory)
    gallery_content = generate_gallery(pictures)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(gallery_content)

    print(f"Gallery file '{output_file}' has been generated with {len(pictures)} images.")