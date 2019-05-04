#! /usr/bin/env python3

import imageio, glob, PIL, tqdm
from image2gifparser import parameter_parser
from PIL import Image, ExifTags

def find_photos(path):
    # Find all candidate images from the input path
    photos = glob.glob(args.input_path + "*.jpeg")
    photos += glob.glob(args.input_path + "*.JPG")
    photos += glob.glob(args.input_path + "*.PNG")
    photos += glob.glob(args.input_path + "*.JPEG")
    photos += glob.glob(args.input_path + "*.png")
    return sorted(photos)

def main(args):
    images = []
    photos = find_photos(args.input_path)
    if not photos:
        print("Please give an input folder with photos in it. Supported file formats are JPEG and PNG.")
        return -1
    
    baseheight = args.height

    for photo in tqdm.tqdm(photos, desc="Reading Images & Resizing"):
        try :
            # Read image
            img = Image.open(photo)
            # Preserve the orientation.
            for orientation in ExifTags.TAGS.keys() : 
                if ExifTags.TAGS[orientation]=='Orientation' : break 
            exif=dict(img._getexif().items())
            if exif[orientation] == 3 : 
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 6 : 
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 8 : 
                img = img.rotate(90, expand=True)
        except:
            traceback.print_exc()
            return -1
        
        img_height = float(img.size[1])
        
        # Resize according to parameters
        if (int(img_height) != baseheight):
            img_width  = float(img.size[0])
            hpercent = (baseheight / img_height)
            wsize = int((img_width * float(hpercent)))
            img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
        images.append(img)
    # Create gif from the images
    print("Creating gif file in", args.output_path + '.gif')
    imageio.mimsave(args.output_path + '.gif', images, duration=args.duration)
    print("Gif file is created!")

if (__name__ == "__main__"):
    args = parameter_parser()
    main(args)