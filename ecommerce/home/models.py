from django.db import models

class Home(models.Model):
    Name = models.CharField(max_length=100)
    Field = models.CharField(max_length=100)
    Quality = models.CharField(max_length=100)
    Item_ID = models.IntegerField()
    Image = models.CharField(max_length=200, default='data:image/png;base64,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')

    def __str__(self):
        return f"{self.Name}"



class Education(models.Model):
    Qualification = models.CharField(max_length=100)
    Skills = models.CharField(max_length=100)
    Certification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Qualification}"
    

class NavBar(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Name}"
    

class DjangoForm(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Name}"
    

class FileFields(models.Model):
    Image = models.ImageField(upload_to='images', default='default.jpg')
    Audio = models.FileField(upload_to='music', default='music.mp3')

    def __str__(self):
        return f"{self.Image}"