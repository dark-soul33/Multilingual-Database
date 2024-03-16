from django.db import models

# Create your models here

class sindhi(models.Model):
    title=models.CharField(max_length=255)
    accession_number=models.CharField(max_length=255)
    author_first_name=models.CharField(max_length=255)
    author_last_name=models.CharField(max_length=255)
    keyword=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    place=models.CharField(max_length=255)

class northeast(models.Model):
    title=models.CharField(max_length=255)
    accession_number=models.CharField(max_length=255)
    class_number=models.CharField(max_length=255)
    author_name=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    year=models.CharField(max_length=255)
    collection=models.CharField(max_length=255)
    language=models.CharField(max_length=255)

class malayalam(models.Model):
    isbn_no=models.CharField(max_length=255)
    malayalam_title=models.CharField(max_length=255)
    english_title=models.CharField(max_length=255)
    author_name=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    publisher=models.CharField(max_length=255)
    year_of_dc=models.CharField(max_length=255)
    year_pub=models.CharField(max_length=255)
    other_pub=models.CharField(max_length=255)




