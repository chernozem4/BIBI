from django.db import models

# Create your models here.
class Post(models.Model):

    LIKE_OR_DISLIKE = (
        ('👍🏻', '👍🏻'),
        ('👎🏻', '👎🏻'),

    )

    title = models.CharField(max_length=255,
                             verbose_name='enter title news')
    image = models.ImageField(upload_to='post/',
                              verbose_name='download picture')
    description = models.TextField(verbose_name='white your news')
    url_news = models.URLField(verbose_name='white your url news')
    email_news = models.EmailField(verbose_name='white  email news company')
    #Если вы после миграций забыли указать какое то поле то так же создаете его,
    # но в атрибуте нового поля, указываете null=True и заново проводите миграции (PS: даже если вы изменили название поля)
    like_or_dislike = models.CharField(max_length=100, choices=LIKE_OR_DISLIKE,
                                       null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.created_at}'



class ReviewPost(models.Model):
    post_review = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='review_post')
    text_post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.text_post} - {self.created_at}'