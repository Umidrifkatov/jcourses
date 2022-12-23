from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название категории')
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Author(models.Model):
    name = models.CharField(max_length=300, verbose_name='Имя')
    img = models.ImageField(upload_to='authorsimage/', height_field=None, width_field=None, max_length=100)
    description = models.TextField(max_length=500, verbose_name='Описание спикера', null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'




class Course(models.Model):
    shorttitle = models.CharField(max_length=300, verbose_name='Краткое название')
    title = models.TextField(max_length=500, verbose_name='Название')
    
    shortdesc = models.CharField(max_length=300, verbose_name='Краткое описание')
    longdesc = models.TextField(max_length=1000, verbose_name='Полное описание')
    
    


    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Спикер')


    locationcity = models.CharField(max_length=300, verbose_name='Страна Город')
    loactionplace = models.CharField(max_length=300, verbose_name='Место')

    locationpic = models.CharField(max_length=300, verbose_name='Фото локации (места проведения)', help_text='введите ID картинки с гугл диска')
    
    startdate = models.DateField( verbose_name='Дата начала')
    enddate = models.DateField( verbose_name='Дата конца')
    regdate = models.DateField( verbose_name='Дата ранней регистрации (До)')

    price1 = models.IntegerField( verbose_name='Цена ранней рег')
    price2 = models.IntegerField( verbose_name='Цена поздней рег')

    recomended = models.BooleanField(verbose_name='Рекомендовать', default=False)

    ended = models.BooleanField(default=False, verbose_name='Окончен')

    def __str__(self):
        return f'{self.shorttitle}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'




class CourseImage(models.Model):
    belongs_to = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='images',
                                            verbose_name='Принадлежит курсу')
    image_file = models.ImageField(upload_to='cases/',verbose_name='изображение')

    def __str__(self):
        return f'{self.belongs_to.shorttitle}'

    class Meta:
        verbose_name = 'Клинический кейс'
        verbose_name_plural = 'Клинические кейсы'

class PostCourseImage(models.Model):
    belongs_to = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='pimages',
                                            verbose_name='Принадлежит курсу')
    image_file = models.ImageField(upload_to='photoarchive/',verbose_name='изображение')
    

    def __str__(self):
        return f'{self.belongs_to.shorttitle}'

    class Meta:
        verbose_name = 'Фотоотчет'
        verbose_name_plural = 'Фотоотчет'