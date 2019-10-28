from django.db import models

# Create your models here.

class Productowner(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    def __str__(self):
        return name

class Productbacklog(models.Model):
    pass

class Project(models.Model):
    name=models.CharField(max_length=50)
    owner=models.ForeignKey(Productowner,on_delete=models.CASCADE)
    pb=models.ForeignKey(Productbacklog, on_delete=models.CASCADE)
    create_time=models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return name


class  TeamMember(models.Model): 
    name=models.CharField(max_length=20)
    email=models.EmailField()
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return name



class Pbi(models.Model):
    card=models.TextField()
    conversation=models.CharField(max_length=100)
    storypoints=models.IntegerField()
    sprintNo=models.IntegerField()
    #define the choices
    inprogress='INP'
    completed='CP'
    notstart='NO'
    stat=[(inprogress,'in progress'),(completed,'compeleted'),(notstart,'not start')]
    status=models.CharField(choices=stat, max_length=20,default=notstart)
    

class Confirmation(models.Model):
    content=models.CharField(max_length=100)
    done=models.BooleanField()
    pbi=models.ForeignKey(Pbi, on_delete=models.CASCADE)


