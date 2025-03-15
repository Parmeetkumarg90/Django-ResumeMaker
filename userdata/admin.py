from django.contrib import admin
from .models import user_data
# Register your models here.
class show_data(admin.ModelAdmin):
    list_display = ('username','intro_firstname','intro_middlename','intro_lastname','intro_image','intro_designation','intro_address','intro_email','intro_phone','intro_summary','achi_title','achi_description','exp_title','exp_company','exp_location','exp_start_date','exp_end_date','exp_description','edu_school','edu_degree','edu_city','edu_start_date','edu_end_date','edu_description','proj_name','proj_link','proj_description','skills')

admin.site.register(user_data,show_data)