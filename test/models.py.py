from django.db import models


class BlogModel(models.Model):
    id = models.IntegerField(primary_key=True)
    '''
    If you don’t specify primary_key=True for any fields in your model, Django will automatically add an IntegerField to hold the primary key,
    so you don’t need to set primary_key=True on any of your fields [https://docs.djangoproject.com/en/3.1/topics/db/models/]
    '''
    blog_title = models.CharField(max_length=25)
    blog = models.TextField()

    def __str__(self):
        # return f"Blog: {self.blog_title}"
        return 'Blog:', self.blog_title


class CommentModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = first_name + ' ' + last_name
    nic_name = models.CharField(max_length=25)
    comment_text = models.TextField()
    blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE)

    def __str__(self):
        # return f"Comment by Name: {self.nic_name}"
        return 'Comment by Name:', self.nic_name
