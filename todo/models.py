from django.db import models

from django.utils.text import slugify




class Category(models.Model):
    name = models.CharField(max_length = 200, unique=True, verbose_name="name")
    slug = models.SlugField(max_length = 200, unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    complet = models.BooleanField(default=False)
    color = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d', blank=True)
    archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)





class Tache(models.Model):
    category = models.ForeignKey(Category, null=True, verbose_name="category", 
                related_name='taches', on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, unique=True, verbose_name="name")
    slug = models.SlugField(max_length = 200, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complet = models.BooleanField(default=False)
    color = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)







