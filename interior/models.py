from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=300)


class Author(models.Model):
    name = models.CharField(max_length=300)




class Course(models.Model):
    title = models.CharField(max_length=300)
    shorttitle = models.CharField(max_length=300)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)

    locationcity = models.CharField()
    loactionplace = models.CharField()
    locationpic = models.CharField()
    
    shortdesc = models.CharField(max_length=300)
    longdesc = models.CharField(max_length=300)

    startdate = models.CharField(max_length=300)
    enddate = models.CharField(max_length=300)

    price = models.IntegerField()



