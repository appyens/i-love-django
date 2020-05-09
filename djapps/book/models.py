from django.db import models


class Genre(models.Model):
    """
    Genre mapping for book model
    """
    genre = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Object representation
        """
        return self.genre


class Language(models.Model):
    """
    Language table definition
    """
    language = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Object representation
        """
        return self.language


class Author(models.Model):
    """
    Author table definition
    """
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256)
    dob = models.DateField(blank=True, null=True)
    death = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    wikipedia = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Object representation
        """
        return self.first_name + " " + self.last_name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book table definition
    """
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    authors = models.ManyToManyField(Author, related_name='books')
    edition = models.SmallIntegerField(default=1)
    pages = models.IntegerField(blank=True)
    year = models.IntegerField(blank=True)
    language = models.ForeignKey(
        Language, on_delete=models.DO_NOTHING, related_name='books')
    genre = models.ForeignKey(
        Genre, on_delete=models.DO_NOTHING, related_name='books')
    publisher = models.ForeignKey(
        Publisher, on_delete=models.DO_NOTHING, related_name='books')
    description = models.TextField(max_length=1000)
    isbn = models.CharField(verbose_name='ISBN', max_length=13, blank=True)
    isbn_13 = models.CharField(
        verbose_name='ISBN-13',  max_length=17, blank=True)
    store_link = models.URLField(blank=True)
    wikipedia = models.URLField(blank=True)
    front_cover = models.ImageField(upload_to='book/covers/front/', blank=True)
    back_cover = models.ImageField(upload_to='book/covers/back/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Object representation
        """
        return self.title
