from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):  # defines the our model (called Post), which is an object
    # class name should always start with an uppercase letter
    # models.Model indicates that it is a django model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey links to another model
    title = models.CharField(max_length=200)  # defines text that will hold a limited number of characters
    text = models.TextField()  # for long texts without any character limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# self represents an instance of our class.
# By using it ware able to access the class methods and attributes
