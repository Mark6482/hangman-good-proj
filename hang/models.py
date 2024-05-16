from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self) -> str:
        return str(self.name)


class Word(models.Model):
    text = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.text)
