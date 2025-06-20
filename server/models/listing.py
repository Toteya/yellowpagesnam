"""
Directory listing implementation
"""
from mongoengine import DictField, EmailField, IntField, ListField, PointField, StringField
from server.models.base import BaseModel
import os
import shutil


class Listing(BaseModel):
    """
    Directory listing model.
    """
    meta = {
        'collection': 'listings',
        'indexes': [
            'name',
            'category',
            'email',
            'website',
            'location',
            'phone_numbers',
            'likes',
            'reviews'
        ]
    }

    name = StringField(max_length=255, required=True)
    category = StringField(max_length=255, required=True)
    email = EmailField(max_length=255, required=False)
    website = StringField(max_length=255, required=False)
    location = PointField(required=False)  # GeoJSON point for location
    phone_numbers = ListField(StringField(max_length=60), required=False)
    photos = ListField(StringField(max_length=255), required=False)
    likes = IntField(default=0, required=False)
    reviews = ListField(DictField(), default=list, required=False)

    def add_media(self, filename):
        """ Adds a photo to the listing
        """
        accepted_video_formats = ['.mp4', '.mov', '.webm', '.ogg']
        accepted_image_formats = ['.jpg', '.jpeg', '.png', '.gif']

        # check if file format is acceptable
        if not filename.lower().endswith(tuple(accepted_video_formats + accepted_image_formats)):
            raise ValueError("Invalid file format. Only images and videos are allowed.")

        media_dirpath = os.environ.get('DIRECTORY_MEDIA_DIRPATH')
        if not media_dirpath:
            raise EnvironmentError("DIRECTORY_MEDIA_DIRPATH environment variable is not set.")
        if not os.path.exists(media_dirpath):
            print(f"Directory {media_dirpath} does not exist.")
            raise FileNotFoundError(f"The directory {media_dirpath} does not exist.")

        # check if file exists in the general media folder
        scr_filepath = f'{media_dirpath}/all/{filename}'
        if not os.path.exists(scr_filepath):
            raise FileNotFoundError(f"The file {filename} does not exist in the media folder.")

        # copy file to the dedicated folder
        if filename.lower().endswith(tuple(accepted_image_formats)):
            type = 'photos'
        else:
            type = 'videos'
 
        # create a subfolder for the listing if it doesn't already exist
        dst_subfolder = f'{self.id}/{type}'

        try:
            os.makedirs(f'{media_dirpath}/{dst_subfolder}', exist_ok=True)
        except Exception as e:
            print(f"Error creating directory {media_dirpath}/{dst_subfolder}: {e}")
            raise
        
        dst_filepath = f'{dst_subfolder}/{filename}'
        shutil.copy(scr_filepath, f'{media_dirpath}/{dst_filepath}')

        self.photos.append(dst_filepath)
