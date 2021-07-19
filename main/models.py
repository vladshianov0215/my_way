from django.db import models

# Create your models here.

#dont foget register this on admin panel

class Task(models.Model): #it`s table sqllite
    title = models.CharField('Name', max_length=50)   #attribute char 255 symbols
    task = models.TextField('About') #attribute string 

    def __str__(self): #show class to screen
        return self.title
    
    class Meta:
        verbose_name = 'MyTask'
        verbose_name_plural = 'MyTasks'