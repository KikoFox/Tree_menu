from django.db import models
from django.urls import reverse


class Menu(models.Model):

    """
    Модель для Menu. Имеет поля title и slug.
    """

    is_visible = models.BooleanField(default=True, verbose_name='Видимость поля')
    order = models.IntegerField(default=10, verbose_name='Порядок отображения')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=20, verbose_name='Заголовок меню')
    slug = models.SlugField(max_length=255, verbose_name='Slug', null=True,
                            help_text='Используйте его templatetag для отображения меню')
    named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
                                 help_text='Именованный URL-адрес из вашего файла urls.py')
    objects = models.Manager()

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return self.title

    def get_full_path(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = '/{}/'.format(self.slug)
        return url


class MenuItem(models.Model):

    """
    Модель для MenuItem. Имеет поля menu, parent, title, поля URL.
    Поле menu требуется только для элементов верхнего уровня.
    Вы можете указать любой элемент в родительском поле, и он станет относительным для этого элемента.
    Если вы будете использовать поле «именованный URL-адрес», метод get_url будет использовать
    его в первую очередь для генерации URL-адреса.
    И только потом поле 'url'.
    """

    is_visible = models.BooleanField(default=True, verbose_name='Visibility')
    order = models.IntegerField(default=10, verbose_name='Order')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    menu = models.ForeignKey(Menu, related_name='items',
                             verbose_name='menu', blank=True, null=True,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='items',
                               verbose_name='parent menu item',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Item title')
    url = models.CharField(max_length=255, verbose_name='Link', blank=True)
    named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
                                 help_text='Named url from your urls.py file')
    objects = models.Manager()

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
        ordering = ('order', )

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        elif self.url:
            url = self.url
        else:
            url = '/'

        return url

    def __str__(self):
        return self.title
