from django.db import models 
class profile(models.Model): 
    name = models.CharField(max_lenght = 50) 
    picture = models.ImageField(upload_to ='pictures') 
    class Meta: 
        db_table = "profile" 
