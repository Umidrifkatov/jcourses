from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=300)
    # shorttitle = models.CharField(max_length=300)

    # category = models.ForeignKey()
    # author = models.ForeignKey()

    # locationcity = models.CharField()
    # loactionplace = models.CharField()
    # locationpic = models.CharField()
    
    # shortdesc = models.CharField(max_length=300)
    # longdesc = models.CharField(max_length=300)

    # startdate = models.CharField(max_length=300)
    # enddate = models.CharField(max_length=300)


    # price = models.CharField()



