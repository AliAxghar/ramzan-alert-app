from django.db import models


class Ayat(models.Model):
    reference = models.CharField(max_length=255)
    arabic_text = models.TextField()
    urdu_text = models.TextField()
    english_text = models.TextField()


    def __str__(self):
        return self.reference

class Hadees(models.Model):
    reference = models.CharField(max_length=255)
    arabic_text = models.TextField()
    urdu_text = models.TextField()
    english_text = models.TextField()


    def __str__(self):
        return self.reference

class Dua(models.Model):
    title = models.CharField(max_length=255)
    arabic_text = models.TextField()  
    urdu_text = models.TextField()
    english_text = models.TextField()


    def __str__(self):
        return self.title

class Quran(models.Model):
    arabic = models.FileField(upload_to='files/')
    urdu_arabic = models.FileField()


    def __str__(self):
        return self.arabic

class Eid(models.Model):
    reference = models.CharField(max_length=255)
    arabic_hadees = models.TextField()
    urdu_hadees = models.TextField()
    english_hadees = models.TextField()

    def __str__(self):
        return self.reference

class RamzanHadees(models.Model):
    reference = models.CharField(max_length=255)
    arabic_text = models.TextField(default="")  
    urdu_text = models.TextField(default="")
    english_text = models.TextField(default="")

    def __str__(self):
        return self.reference

class SehrHadees(models.Model):
    reference = models.CharField(max_length=255)
    arabic_text = models.TextField(default="")  
    urdu_text = models.TextField(default="")
    english_text = models.TextField(default="")

    def __str__(self):
        return self.reference

class IftarHadees(models.Model):
    reference = models.CharField(max_length=255)
    arabic_text = models.TextField(default="")  
    urdu_text = models.TextField(default="")
    english_text = models.TextField(default="")

    def __str__(self):
        return self.reference

class LailaTulQadarHadees(models.Model):
    reference = models.CharField(max_length=255)
    arabic_text = models.TextField(default="")  
    urdu_text = models.TextField(default="")
    english_text = models.TextField(default="")

    def __str__(self):
        return self.reference

