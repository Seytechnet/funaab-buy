import requests
from PIL import Image
import io

def upload_image_to_imgbb(image_file):
    url = "https://api.imgbb.com/1/upload"
    api_key = "2d57b31a66582a2c75234109512f3967"  # Your ImgBB API key

    # Open the image using Pillow to convert it to WebP
    try:
        image = Image.open(image_file)
        image = image.convert('RGB')  # Convert to RGB to ensure compatibility with WebP format

        # Create a BytesIO object to save the image as WebP
        webp_image_io = io.BytesIO()
        image.save(webp_image_io, format='WEBP')
        webp_image_io.seek(0)  # Move the pointer to the start of the BytesIO object

        # Prepare the payload with the API key
        payload = {
            'key': api_key,
        }

        # Prepare the files to be uploaded
        files = {
            'image': ('image.webp', webp_image_io, 'image/webp')
        }

        # Send the POST request to ImgBB
        response = requests.post(url, data=payload, files=files)

        # Check if the upload was successful
        if response.status_code == 200:
            data = response.json()
            image_url = data['data']['url']  # The URL of the uploaded image on ImgBB
            return image_url
        else:
            print(f"Error uploading image: {response.text}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
