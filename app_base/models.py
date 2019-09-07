from django.db import models

def sample_image_path(instance,filename):
    return instance.title

class sampleBot(models.Model):
    title = models.CharField(null=True,max_length = 100)
    sample_image = models.ImageField( upload_to='sample_image_path',null=True)
    description = models.TextField(null=True)
    telegram_link = models.CharField(null=True,max_length=50)

    def __str__(self):
        return str(self.title)
class otherSampleBot(models.Model):
    title = models.CharField(null=True,max_length = 100)
    sample_image = models.ImageField( upload_to='sample_image_path',null=True)
    description = models.TextField(null=True)
    telegram_link = models.CharField(null=True,max_length=50)
    def __str__(self):
        return str(self.title)