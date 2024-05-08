import csv
import os
from PIL import Image, ImageDraw, ImageFont

# Set the paths for the required files and directories
template_image_path = "template.png"
csv_file_path = "employee.csv"
photo_dir_path = "employee_photos"
output_pdf_path = "output.pdf"

# Open the ID template image
template_image = Image.open(template_image_path)

# Create a list to store all the ID card images
id_cards = []
with open(csv_file_path, "r", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Create a copy of the template image
        id_card = template_image.copy()

        # Load the employee photo
        photo_path = os.path.join(photo_dir_path, row["photo"])
        employee_photo = Image.open(photo_path)

        # Paste the employee photo onto the ID card
        id_card.paste(employee_photo, (50, 50))  # Adjust the position as needed

        # Draw the employee name and title
        draw = ImageDraw.Draw(id_card)
        font = ImageFont.truetype("arial.ttf", 24)  # Adjust the font and size as needed
        draw.text((200, 50), row["name"], font=font, fill=(0, 0, 0))
        draw.text((200, 100), row["title"], font=font, fill=(0, 0, 0))

        # Add the ID card image to the list
        id_cards.append(id_card)

# Save the ID cards as a single PDF file
id_cards[0].save(output_pdf_path, save_all=True, append_images=id_cards[1:])
