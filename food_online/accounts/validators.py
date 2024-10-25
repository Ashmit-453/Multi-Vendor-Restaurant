from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    # Get the file extension using value.name and [1] for extension
    ext = os.path.splitext(value.name)[1]  # Changed value to value.name and [0] to [1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions: ' + str(valid_extensions))