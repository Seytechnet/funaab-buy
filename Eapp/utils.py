import requests
from PIL import Image
import io

def upload_image_to_imgbb(image_file):
    url = "https://api.imgbb.com/1/upload"
    api_key = "2d57b31a66582a2c75234109512f3967"

    try:
        # Open the image and convert it to WebP
        image = Image.open(image_file)
        image = image.convert('RGB')  # Ensure compatibility with WebP format

        # Save the image as WebP in memory
        webp_image_io = io.BytesIO()
        image.save(webp_image_io, format='WEBP')
        webp_image_io.seek(0)  # Reset pointer to the start

        # Prepare payload and files
        payload = {'key': api_key}
        files = {
            'image': ('image.webp', webp_image_io, 'image/webp')
        }

        # Make API request
        response = requests.post(url, data=payload, files=files)

        # Handle response
        if response.status_code == 200:
            data = response.json()
            image_url = data.get('data', {}).get('url')
            if image_url:
                return image_url
            else:
                print(f"Error: No URL returned. Response: {response.json()}")
                return None
        else:
            print(f"ImgBB API Error: {response.status_code}, {response.text}")
            return None

    except Exception as e:
        print(f"Error in upload_image_to_imgbb: {e}")
        return None
