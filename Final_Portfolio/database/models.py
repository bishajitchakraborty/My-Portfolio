from django.db import models


class About(models.Model):
    about=models.TextField(null=True, blank=True)
    cv_link=models.CharField(max_length=200,null=True, blank=True)
    facebook_link=models.CharField(max_length=200,null=True, blank=True)
    linkdin_link=models.CharField(max_length=200,null=True, blank=True)
    github_link=models.CharField(max_length=200,null=True, blank=True)

class Contact(models.Model):
    phone=models.CharField(max_length=11,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)


class Profile(models.Model):
    firstname=models.CharField(max_length=25,null=True, blank=True)
    lastname=models.CharField(max_length=35,null=True, blank=True)
    about=models.OneToOneField(About,null=True, blank=True, on_delete=models.CASCADE)
    contact=models.OneToOneField(Contact,default=None, null=True, blank=True, on_delete=models.CASCADE)
 
class Skills(models.Model):
    skill=models.CharField(max_length=70,null=True, blank=True)
    images=models.ImageField(null=True, blank=True)
    about=models.ForeignKey(About,default=None, null=True, blank=True,on_delete=models.CASCADE)

class Experiernces(models.Model):
    start_date=models.DateField(null=True, blank=True)
    posision=models.CharField(max_length=200,null=True, blank=True)
    company_name=models.CharField(max_length=70,null=True, blank=True)
    company_logo=models.ImageField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    about=models.ForeignKey(About,default=None, null=True, blank=True,on_delete=models.CASCADE)

class Educations(models.Model):
    start_date=models.DateField(null=True, blank=True)
    end_date=models.DateField(null=True, blank=True)
    institution_name=models.CharField(max_length=70,null=True, blank=True)
    institution_logo=models.ImageField(null=True, blank=True)
    education=models.CharField(max_length=20,null=True, blank=True)
    CGPA=models.FloatField(null=True, blank=True)
    Out_of=models.FloatField(null=True, blank=True)
    about=models.ForeignKey(About,default=None, null=True, blank=True,on_delete=models.CASCADE)


class Testimonials(models.Model):
    Client_name=models.CharField(max_length=35,null=True, blank=True)
    company=models.CharField(max_length=50,null=True, blank=True)
    speech=models.CharField(max_length=250,null=True, blank=True)
    image=models.ImageField(null=True, blank=True)
    video=models.FileField(upload_to='videos/',null=True, blank=True)
    profile=models.ForeignKey(Profile,default=None, null=True, blank=True,on_delete=models.CASCADE)



class Services(models.Model):
    service_name=models.CharField(max_length=60,null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    icon=models.ImageField(null=True, blank=True)
    profile=models.ForeignKey(Profile,default=None, null=True, blank=True,on_delete=models.CASCADE)

class Message(models.Model):
    name=models.CharField(max_length=60,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    subject=models.CharField(max_length=22,null=True, blank=True)
    message=models.TextField(null=True, blank=True)
    profile=models.ForeignKey(Profile,default=None, null=True, blank=True,on_delete=models.CASCADE)

class Professions(models.Model):
    profession=models.CharField(max_length=60,null=True, blank=True)
    profile=models.ForeignKey(Profile,default=None, null=True, blank=True,on_delete=models.CASCADE)



class Category(models.Model):
    name=models.CharField(max_length=50,null=True, blank=True)

class Portfolio_projects(models.Model):
    title=models.CharField(max_length=60,null=True, blank=True)
    thumbnail=models.TextField(null=True, blank=True)
    category=models.ForeignKey(Category,null=True, blank=True,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,default=None, null=True, blank=True,on_delete=models.CASCADE)

class Images(models.Model):
    portfolio_projects=models.ForeignKey(Portfolio_projects,default=None, null=True, blank=True,on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True)
 



