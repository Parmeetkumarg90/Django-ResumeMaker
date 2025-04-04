from django.db import models
# Create your models here.
class user_data(models.Model):
    username = models.CharField(max_length=15,verbose_name="UserName",default = '')

    intro_firstname = models.CharField(max_length=50,verbose_name="FirstName",default = '')
    intro_middlename = models.CharField(max_length=50,verbose_name="MiddleName",default = '')
    intro_lastname = models.CharField(max_length=50,verbose_name="LastName",default = '')
    # intro_image = models.FileField(upload_to='',verbose_name="User Image",null = True,default=None,max_length=250)
    intro_image = models.TextField(default="")
    intro_designation = models.TextField(verbose_name="Designation",default = '')
    intro_address = models.TextField(verbose_name="User Address",default = '')
    intro_email = models.EmailField(verbose_name="User Email",default = '')
    intro_phone = models.CharField(max_length=50,verbose_name="User Mobile Number",default = '')
    intro_summary = models.TextField(verbose_name="User Summary",default = '')

    achi_title = models.CharField(max_length=50,verbose_name="Achievement Title",default = list)
    achi_description = models.TextField(verbose_name="Achievement Description",default = list)

    exp_title = models.CharField(max_length=50,verbose_name="Experience Title",default = list)
    exp_company = models.CharField(max_length=50,verbose_name="Experience Company",default = list)
    exp_location = models.CharField(max_length=50,verbose_name="Experience Location",default = list)
    exp_start_date = models.JSONField(verbose_name="Experience Start Date",null=True,blank=True)
    exp_end_date = models.JSONField(verbose_name="Experience End Date",null=True,blank=True)
    exp_description = models.TextField(verbose_name="Experience Description",default = list)

    edu_school = models.CharField(max_length=50,verbose_name="Education School",default = list)
    edu_degree = models.CharField(max_length=50,verbose_name="Education Degree",default = list)
    edu_city = models.CharField(max_length=50,verbose_name="Education City",default = list)
    edu_start_date = models.JSONField(verbose_name="Education Start Date",null=True,blank=True)
    edu_end_date = models.JSONField(verbose_name="Education End Date",null=True,blank=True)
    edu_description = models.TextField(verbose_name="Education Description",default = list)

    proj_name = models.CharField(max_length=50,verbose_name="Project Name",default = list)
    proj_link = models.CharField(max_length=50,verbose_name="Project Link",default = list)
    proj_description = models.TextField(verbose_name="Project Description",default = list)

    skills = models.TextField(verbose_name="your Skills",default = list)
