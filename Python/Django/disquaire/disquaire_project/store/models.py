from django.db import models
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "artiste"

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "prospect"

    def __str__(self):
        return self.name


class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.ImageField(blank=True, null = True)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)
    img = models.BinaryField(null = True)

    class Meta:
        verbose_name = "disque"

    def __str__(self):
        return self.title


class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "réservation"

    def __str__(self):
        return self.contact.name
