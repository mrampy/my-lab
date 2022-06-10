from PIL import Image
import sys, os


#grab the first and second argument

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]
current_dir = os.getcwd()



#check if new folder exists and if not,  create it

if  not os.path.exists(png_folder):
    os.mkdir(png_folder)

#loop through entire folder and convert it to png
for image_file in os.listdir(jpg_folder):
    image_file_name = os.path.splitext(image_file)[0]
    img = Image.open(f"{jpg_folder}\{image_file}")
    img.save(f"{png_folder}\{image_file_name}.png")
    
    






