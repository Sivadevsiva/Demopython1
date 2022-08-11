from django.db import models

# Create your models here.
class Agri(models.Model):
    name=models.CharField(max_length=250)
    use=models.TextField()
    About=models.TextField()
    img=models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.name


