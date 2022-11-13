from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=300)


class Author(models.Model):
    name = models.CharField(max_length=300)




class Course(models.Model):
    title = models.CharField(max_length=300)
    shorttitle = models.CharField(max_length=300)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    locationcity = models.CharField(max_length=300)
    loactionplace = models.CharField(max_length=300)
    locationpic = models.CharField(max_length=300)
    
    shortdesc = models.CharField(max_length=300)
    longdesc = models.CharField(max_length=300)

    startdate = models.CharField(max_length=300)
    enddate = models.CharField(max_length=300)

    price = models.IntegerField()



