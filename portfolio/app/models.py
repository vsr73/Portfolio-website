from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=200,null=False)
    role=models.CharField(max_length=200,null=False)
    number=models.IntegerField(null=False)
    email=models.EmailField(null=False)
    bio=models.TextField(null=False,blank=False)
    experience=models.IntegerField(blank=False)
    no_of_awards=models.IntegerField(blank=False)
    no_of_works_completed=models.IntegerField(null=False,blank=False)
    clients_dealed=models.IntegerField(null=False,blank=False)
    address=models.CharField(max_length=500)
    dp=models.ImageField(null=False,default='avatar.svg')
    hero_bg=models.ImageField(null=False,default='hero-bg.jpg')
    def __str__(self):
        return self.name
class skills(models.Model):
    host=models.ForeignKey(user,on_delete=models.CASCADE)
    skill=models.CharField(max_length=150)
    def __str__(self):
        return self.skill

class coding_languages(models.Model):
    host=models.ForeignKey(user,on_delete=models.CASCADE)
    language=models.CharField(max_length=150)
    percentage_contributed=models.IntegerField(null=False,blank=False)
    def __str__(self):
        return self.language

class support(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    subject=models.CharField(max_length=150)
    message=models.CharField(max_length=500)
    def __str__(self):
        return self.subject

class ideas(models.Model):
    idea=models.CharField(max_length=150,null=False)
    display=models.ImageField(null=False,default='post-3.jpg')
    description=models.TextField(null=False)

class servicestyle(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class services(models.Model):
    host=models.ForeignKey(user,on_delete=models.CASCADE)

    service=models.CharField(max_length=100)
    description=models.TextField(blank=True)

    
    service1=models.CharField(max_length=100,blank=True)
    description1=models.TextField(blank=True)


    service2=models.CharField(max_length=100,blank=True)
    description2=models.TextField(blank=True)


    service3=models.CharField(max_length=100,blank=True)
    description3=models.TextField(blank=True)

    
    service4=models.CharField(max_length=100,blank=True)
    description4=models.TextField(blank=True)

    service5=models.CharField(max_length=100,blank=True)
    description5=models.TextField(blank=True)

    def __str__(self):
        return 'services offeredy by'+self.host.name

class blog(models.Model):
    host=models.ForeignKey(user,on_delete = models.CASCADE)
    category=models.CharField(max_length=200)
    subject=models.CharField(max_length=300,null=False)
    description=models.TextField(blank=False)
    pic=models.ImageField(null=False,blank=False)
    def __str__(self):
        return self.subject

class comment(models.Model):
    blog=models.ForeignKey(blog,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=150)
    mail=models.EmailField(null=False)
    comment=models.CharField(max_length=150)
    dp=models.ImageField(default='avatar.svg')
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment

class reply(models.Model):
    reply_name=models.CharField(max_length=100)
    commentor=models.ForeignKey(comment,on_delete=models.CASCADE)
    reply=models.CharField(max_length=300,default='my reply')
    reply_created=models.DateTimeField(auto_now_add=True)
    dpic=models.ImageField(default='emoji1.png')
    def __str__(self):
        return self.reply+'  reply given to commment  '+self.commentor.comment

class projects(models.Model):
    host=models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    client=models.CharField(max_length=50)
    date=models.DateTimeField(blank=False)
    url=models.URLField(max_length=150)
    details=models.TextField(max_length=200)
    bg=models.ImageField(null=False,default='work-3.jpg')
    img1=models.ImageField(null=True,default='work-3.jpg')
    img2=models.ImageField(null=True,blank=True)
    img3=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.title