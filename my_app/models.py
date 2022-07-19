from django.db import models



class Post(models.Model):
    sarlavha = models.CharField(max_length = 250)
    text = models.TextField()

    def __str__(self):
        return self.sarlavha


class Category(models.Model):
    name = models.CharField(max_length=100, null = False, blank = False)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length = 250)
    image = models.ImageField(upload_to='images/', blank = True)
    text = models.TextField()
    category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
