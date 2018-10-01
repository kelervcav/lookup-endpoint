from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class AbstractCategory(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'PENDING'),
        ('ACTIVATED', 'ACTIVATED'),
        ('REJECTED', 'REJECTED'),
        ('ARCHIVED', 'ARCHIVED'),
    )
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(AbstractCategory, self).save(*args, **kwargs)
        slug = slugify(self.name) + "-" + str(self.id)
        if self.slug != slug:
            self.slug = slug
            self.save()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()


class Category(AbstractCategory):

    class Meta:
        db_table = 'categories'


class SubCategory(AbstractCategory):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'sub_categories'
