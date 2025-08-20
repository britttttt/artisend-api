from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from .post import Post

def get_media_upload_path(instance, filename):
    """
    Generate upload path based on media type.
    This function is outside the class because it needs to be 
    accessible to the upload_to parameter.
    """
    media_type = instance.media_type
    if media_type == 'image':
        return f'post_media/images/{filename}'
    elif media_type == 'video':
        return f'post_media/videos/{filename}'
    elif media_type == 'audio':
        return f'post_media/audio/{filename}'
    else:
        return f'post_media/other/{filename}'

class PostMedia(models.Model):
    """
    Represents media attachments for posts.
    Notice how everything that belongs to this class is indented
    one level in from the class declaration.
    """
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    
    # You can use your custom upload path function here
    file = models.FileField(
        upload_to=get_media_upload_path,  # Using your custom function
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp4', 'mp3', 'wav']
            )
        ]
    )  
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        ordering = ['order', 'created_at']  
        verbose_name = "Post Media"
        verbose_name_plural = "Post Media"
    
    def clean(self):
        """
        Validate file size based on media type.
        This method MUST be indented to be part of the PostMedia class.
        """
        if self.file:
            file_size = self.file.size
            

            size_limits = {
                'image': 10 * 1024 * 1024,  # 10MB
                'video': 50 * 1024 * 1024,  # 50MB
                'audio': 20 * 1024 * 1024,  # 20MB
            }
            
            limit = size_limits.get(self.media_type)
            if limit and file_size > limit:
                # Make the error message user-friendly
                limit_mb = limit / (1024 * 1024)
                size_mb = file_size / (1024 * 1024)
                raise ValidationError(
                    f"{self.get_media_type_display()} files must be under {limit_mb}MB. "
                    f"Your file is {size_mb:.1f}MB."
                )
    
    def save(self, *args, **kwargs):
        """
        Auto-detect media type from file extension if not set.
        This method MUST be indented to be part of the PostMedia class.
        """
        if self.file and not self.media_type:
            extension = self.file.name.split('.')[-1].lower()
            
            # Define our extension mappings
            extension_map = {
                'image': ['jpg', 'jpeg', 'png', 'gif'],
                'video': ['mp4', 'avi', 'mov'],
                'audio': ['mp3', 'wav', 'ogg']
            }
            
            # Find the media type for this extension
            for media_type, extensions in extension_map.items():
                if extension in extensions:
                    self.media_type = media_type
                    break
            else:
                # This runs if we didn't find a match (Python's for-else construct)
                raise ValidationError(f"Unsupported file type: {extension}")
        
        self.full_clean()  # Run validation before saving
        super().save(*args, **kwargs)
    
    def __str__(self):
        """
        String representation for admin interface and debugging.
        This makes it easier to identify media items.
        """
        return f"{self.get_media_type_display()} for post '{self.post.title}' (order: {self.order})"