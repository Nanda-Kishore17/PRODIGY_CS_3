from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    """Encrypts an image using XOR pixel manipulation."""
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint8)
    
    encrypted_array = img_array ^ key  # Apply XOR operation with the key
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    """Decrypts an image by reversing the XOR operation."""
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint8)
    
    decrypted_array = img_array ^ key  # XOR twice with the same key restores original image
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    key = 42  # Simple key for XOR operation
    encrypt_image("input.png", key, "encrypted.png")
    decrypt_image("encrypted.png", key, "decrypted.png")
