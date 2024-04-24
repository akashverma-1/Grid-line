import os
from PIL import Image, ImageFilter

class ImageProcessor:
    def __init__(self):
        pass
    
    def resize_image(self, image, scale_factor):
        width, height = image.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        return image.resize((new_width, new_height))
    
    def crop_image(self, image, crop_values):
        return image.crop(crop_values)
    
    def blur_image(self, image):
        return image.filter(ImageFilter.BLUR)
    
    def convert_to_grayscale(self, image):
        return image.convert("L")
    
    def process_single_image(self, image_path, scale_factor=None, crop_values=None, blur=False, grayscale=False):
        image = Image.open(image_path)
        output_paths = {}
        
        if scale_factor is not None:
            resized_image = self.resize_image(image, scale_factor)
            resized_path = "resized_" + os.path.basename(image_path)
            resized_image.save(resized_path)
            output_paths["resized_image"] = resized_path
        
        if crop_values is not None:
            cropped_image = self.crop_image(image, crop_values)
            cropped_path = "cropped_" + os.path.basename(image_path)
            cropped_image.save(cropped_path)
            output_paths["cropped_image"] = cropped_path
        
        if blur:
            blurred_image = self.blur_image(image)
            blurred_path = "blurred_" + os.path.basename(image_path)
            blurred_image.save(blurred_path)
            output_paths["blurred_image"] = blurred_path
        
        if grayscale:
            grayscale_image = self.convert_to_grayscale(image)
            grayscale_path = "grayscale_" + os.path.basename(image_path)
            grayscale_image.save(grayscale_path)
            output_paths["grayscale_image"] = grayscale_path
        
        return output_paths
    
    def process_images_in_folder(self, folder_path, scale_factor=None, crop_values=None, blur=False, grayscale=False):
        output_dict = {}
        for filename in os.listdir(folder_path):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Only process image files
                image_path = os.path.join(folder_path, filename)
                processed_images = self.process_single_image(image_path, scale_factor, crop_values, blur, grayscale)
                output_dict[filename] = processed_images
        return output_dict

if __name__ == "__main__":
# Example usage:
image_processor = ImageProcessor()

# Process a single image
image_path = "input_image.jpg"
processed_images = image_processor.process_single_image(image_path, scale_factor=0.5, crop_values=(100, 100, 400, 400), blur=True, grayscale=True)
print("Processed single image:", processed_images)

# Process all images in a folder
folder_path = "/path/to/folder"
processed_images_folder = image_processor.process_images_in_folder(folder_path, scale_factor=0.5, crop_values=(100, 100, 400, 400), blur=True, grayscale=True)
print("Processed images in folder:", processed_images_folder)
