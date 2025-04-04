from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from userdata.models import user_data
from datetime import date
import ast  # used for making models returning string into list by removing literals
import base64

def homepage(request):
    return render(request,'index.html')

def user_login(request):
    if request.method == 'POST':
        html_username = request.POST['html_username']
        html_password = request.POST['html_password']
        if (html_username == '' or html_password == ''):
            return render(request,'login.html',{ 'output' : 'Wrong UserName or Password' })
        else:
            # Check if the user exists with the exact username (case-sensitive)
            try:
                user = User.objects.get(username=html_username)
            except User.DoesNotExist:
                user = None

            # If user exists, authenticate with the password
            if user is not None and user.check_password(html_password):
                login(request, user)
                request.session['pass'] = html_password
                return redirect('/resumebuild/')
            else:
                return render(request,'login.html',{ 'output' : "Don't have an account"})
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        html_username = request.POST['html_username']
        html_password = request.POST['html_password']
        conf_password = request.POST['html_confpassword']
        if (html_password != conf_password) or (html_username == '' or html_password == '' or conf_password == ''):
            return render(request,'signup.html',{ 'output':'Wrong UserName or Password' })
        else:
            isuser = authenticate(request,username = html_username, password = html_password)
            if isuser is not None:
                return render(request,'signup.html',{ 'output':'You have already an account' })
            else:
                user = User.objects.create_user(username=html_username,password=html_password)
                user.save()
                return render(request,'signup.html',{ 'output' : 'Account created Now Go to LogIn page'})
    return render(request,'signup.html')

def resume(request):        
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = user_data.objects.filter(username=str(request.user)+str(request.session.get('pass',''))).first()
            if not obj:
                data = user_data(
                    username = str(request.user)+str(request.session.get('pass','')),

                    intro_firstname = request.POST.get('firstname',''),
                    intro_middlename = request.POST.get('middlename',''),
                    intro_lastname = request.POST.get('lastname',''),
                    intro_image = base64.b64encode(request.FILES.get('image').read()).decode('utf-8'), # converting images into Base64-encoded string, which is text, not binary
                    intro_designation = request.POST.get('designation',''),
                    intro_address = request.POST.get('address',''),
                    intro_email = request.POST.get('email',''),
                    intro_phone = request.POST.get('phoneno',''),
                    intro_summary = request.POST.get('summary',''),

                    achi_title = request.POST.getlist('achieve_title',''),
                    achi_description = request.POST.getlist('achieve_description',''),

                    exp_title = request.POST.getlist('exp_title',''),
                    exp_company = request.POST.getlist('exp_organization',''),
                    exp_location = request.POST.getlist('exp_location',''),
                    exp_start_date = request.POST.getlist('exp_start_date', ''),
                    exp_end_date = request.POST.getlist('exp_end_date', ''),
                    exp_description = request.POST.getlist('exp_description',''),

                    edu_school = request.POST.getlist('edu_school',''),
                    edu_degree = request.POST.getlist('edu_degree',''),
                    edu_city = request.POST.getlist('edu_city',''),
                    edu_start_date = request.POST.getlist('edu_start_date',''),
                    edu_end_date = request.POST.getlist('edu_graduation_date',''),
                    edu_description = request.POST.getlist('edu_description',''),

                    proj_name = request.POST.getlist('proj_title',''),
                    proj_link = request.POST.getlist('proj_link',''),
                    proj_description = request.POST.getlist('proj_description',''),

                    skills = request.POST.getlist('skill','')
                )
                data.save()
            else:
                # If a record exists, update it
                if request.POST.get('firstname'):
                    obj.intro_firstname = request.POST.get('firstname', '')
                if request.POST.get('middlename'):
                    obj.intro_middlename = request.POST.get('middlename', '')
                if request.POST.get('lastname'):
                    obj.intro_lastname = request.POST.get('lastname', '')
                if request.POST.get('image'):
                    # obj.intro_image = request.FILES.get('image')
                    obj.intro_image = base64.b64encode(request.FILES.get('image').read()).decode('utf-8')
                if request.POST.get('designation'):
                    obj.intro_designation = request.POST.get('designation', '')
                if request.POST.get('address'):
                    obj.intro_address = request.POST.get('address', '')
                if request.POST.get('email'):
                    obj.intro_email = request.POST.get('email', '')
                if request.POST.get('phoneno'):
                    obj.intro_phone = request.POST.get('phoneno', '')
                if request.POST.get('summary'):
                    obj.intro_summary = request.POST.get('summary', '')

                if request.POST.getlist('achieve_title'):
                    obj.achi_title = request.POST.getlist('achieve_title', '')
                if request.POST.getlist('achieve_description'):
                    obj.achi_description = request.POST.getlist('achieve_description', '')

                if request.POST.getlist('exp_title'):
                    obj.exp_title = request.POST.getlist('exp_title', '')
                if request.POST.getlist('exp_organization'):
                    obj.exp_company = request.POST.getlist('exp_organization', '')
                if request.POST.getlist('exp_location'):
                    obj.exp_location = request.POST.getlist('exp_location', '')
                if request.POST.getlist('exp_start_date'):
                    obj.exp_start_date = request.POST.getlist('exp_start_date', date.today())
                if request.POST.getlist('exp_end_date'):
                    obj.exp_end_date = request.POST.getlist('exp_end_date', date.today())
                if request.POST.getlist('exp_description'):
                    obj.exp_description = request.POST.getlist('exp_description', '')

                if request.POST.getlist('edu_school'):
                    obj.edu_school = request.POST.getlist('edu_school', '')
                if request.POST.getlist('edu_degree'):
                    obj.edu_degree = request.POST.getlist('edu_degree', '')
                if request.POST.getlist('edu_city'):
                    obj.edu_city = request.POST.getlist('edu_city', '')
                if request.POST.getlist('edu_start_date'):
                    obj.edu_start_date = request.POST.getlist('edu_start_date', date.today())
                if request.POST.getlist('edu_graduation_date'):
                    obj.edu_end_date = request.POST.getlist('edu_graduation_date', date.today())
                if request.POST.getlist('edu_description'):
                    obj.edu_description = request.POST.getlist('edu_description', '')

                if request.POST.getlist('proj_title'):
                    obj.proj_name = request.POST.getlist('proj_title', '')
                if request.POST.getlist('proj_link'):
                    obj.proj_link = request.POST.getlist('proj_link', '')
                if request.POST.getlist('proj_description'):
                    obj.proj_description = request.POST.getlist('proj_description', '')
                    
                if request.POST.getlist('skill'):
                    obj.skills = request.POST.getlist('skill', '')
                obj.save()
            # return render(request,'resume.html')
        obj = user_data.objects.filter(username=str(request.user)+str(request.session.get('pass',''))).first()
        if obj:
            obj.achi_title = eval(obj.achi_title)
            obj.achi_description = eval(obj.achi_description)

            obj.exp_title = eval(obj.exp_title)
            obj.exp_company = eval(obj.exp_company)
            obj.exp_location = eval(obj.exp_location)
            obj.exp_start_date = obj.exp_start_date
            obj.exp_end_date = obj.exp_end_date
            obj.exp_description = eval(obj.exp_description)

            obj.edu_school = eval(obj.edu_school)
            obj.edu_degree = eval(obj.edu_degree)
            obj.edu_city = eval(obj.edu_city)
            obj.edu_start_date = obj.edu_start_date
            obj.edu_end_date = obj.edu_end_date
            obj.edu_description = eval(obj.edu_description)

            obj.proj_name = eval(obj.proj_name)
            obj.proj_link = eval(obj.proj_link)
            obj.proj_description = eval(obj.proj_description)

            obj.skills = eval(obj.skills)
            print(user_data.intro_image)
            return render(request,'resume.html',
            {'output': obj,
            'achievements':zip(obj.achi_title, obj.achi_description),
            'experiences':zip(obj.exp_title,obj.exp_company,obj.exp_location,obj.exp_start_date,obj.exp_end_date,obj.exp_description),
            'educations':zip(obj.edu_school,obj.edu_degree,obj.edu_city,obj.edu_start_date,obj.edu_end_date,obj.edu_description),
            'projects':zip(obj.proj_name,obj.proj_link,obj.proj_description),
            'skills':obj.skills
            })
        return render(request,'resume.html')
    else:
        return redirect('/signup/')
    
def signout(request):
    logout(request)
    return redirect('/login/')
