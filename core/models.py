from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _


# Post model
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('Заголовок'))
    body = models.TextField(null=False, blank=False, verbose_name=_('Тест поста'))
    created_at = models.DateTimeField(null=False, blank=False, verbose_name=_('Создано в'), auto_now_add=True)
    url_slug = models.CharField(max_length=150, null=False, blank=False, verbose_name=_('URL'), unique=True)
    is_published = models.BooleanField(default=False, verbose_name=_('Опубликовано?'))

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    class Meta:
        db_table = 'posts'
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')
        ordering = ('-published_at',)
