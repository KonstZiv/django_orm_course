from django.db import models


class LiteraryFormat(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(LiteraryFormat, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} (price: {self.price}), format: {self.format.name}"
