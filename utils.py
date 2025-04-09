from imgurpython import ImgurClient
from env import *

imgClient = ImgurClient(clientID, clientSecret)


def get_image_url(image_path: str) -> str:
    try:
        imageUrl = imgClient.upload_from_path(image_path, anon=True)
        return imageUrl['link']
    except Exception as e:
        print(f"Error uploading image: {e}")
        return None


