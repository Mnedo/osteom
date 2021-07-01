from django.db import models
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


def validate_max_four_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 3 and
            obj.id not in list(map(lambda x: x.id, model.objects.all()))):
        raise ValidationError("Can only create 4 %s instance" % model.__name__)


class Posts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    image = models.ImageField(upload_to='osteom_views/static/images', verbose_name='Картинка', blank=True)
    content = models.TextField(verbose_name='Текст поста')
    file = models.FileField(upload_to='osteom_views/static/files', verbose_name='Файл', blank=True)
    is_urgent = models.BooleanField(default=True, verbose_name='Отображать')
    tags = models.ManyToManyField("Tag", verbose_name='Теги')
    date_created = models.DateTimeField(auto_now_add='True')

    def get_tags(self):
        tags_list = self.tags.all()
        res = []
        for tag in tags_list:
            res.append(tag.title)
        return ', '.join(res)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')
    date_created = models.DateTimeField(auto_now_add='True')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Feedback(models.Model):
    name = models.CharField(max_length=15, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    content = models.TextField(max_length=800, verbose_name='Содержание отзыва')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_visible = models.BooleanField(default=False, verbose_name='Отображение на главной странице(максимум 5)')

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' - ' + str(self.time.strftime("%A %d %B %Y"))

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Certificate(models.Model):
    title = models.CharField(max_length=75, verbose_name='Название сертификата')
    image = models.ImageField(upload_to='osteom_views/static/images', verbose_name='Фотография')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Bio(models.Model):
    name = models.CharField(verbose_name='Представить как', max_length=70, default='')
    content = models.TextField(max_length=1000, verbose_name='Описание')
    mail = models.CharField(verbose_name='Почта для связи', max_length=50, default='test_mail@mail.com')
    image = models.ImageField(upload_to='osteom_views/static/images', verbose_name='Фотография')

    def __str__(self):
        return 'Визитка'

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name = 'Визитки'
        verbose_name_plural = 'Визитки'


class BlogAbout(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50, default='Из самых последних')
    bio = models.CharField(verbose_name='Описание', max_length=500)
    img = models.ImageField(verbose_name='Картинка', upload_to='osteom_views/static/images')

    def __str__(self):
        return self.title

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name = 'Био'
        verbose_name_plural = 'Био'


class Jobs(models.Model):
    address = models.CharField(max_length=65, verbose_name='Адрес работы')
    work_time = models.CharField(max_length=50, verbose_name='Время работы')
    phones = models.CharField(max_length=100,
                              verbose_name='Номера телеонов \n (если телефонов >1 делить  ";" без пробелов)')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    location = models.ImageField(verbose_name='Фото местности (не обязательно)', blank=True,
                                 upload_to='osteom_views/static/images')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Место работы'
        verbose_name_plural = 'Места работы'


class ServicePrices(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название услуги')
    price = models.IntegerField(verbose_name='Стоимость')
    free = models.BooleanField(verbose_name='Бесплатно', default=False)

    def __str__(self):
        return self.title

    def clean(self):
        validate_max_four_instance(self)

    class Meta:
        verbose_name = 'Цена услуги'
        verbose_name_plural = 'Цены услуг'
