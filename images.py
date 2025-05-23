import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"D:\Documents\salamehBlog\content\posts"
attachments_dir = r"C:\Users\3adas\OneDrive\Notes\files"
static_images_dir = r"D:\Documents\salamehBlog\static\images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format ![[image.extension]]
        images = re.findall(r'\[\[([^]]+\.(png|jpg|jpeg|gif|bmp|webp|svg))\]\]', content, re.IGNORECASE)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image, _ in images:  # `_` is unused, it contains the extension from the regex group
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"![[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
