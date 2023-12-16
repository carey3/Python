#!/c/Users/carey/AppData/Local/Microsoft/WindowsApps/python
import django
import os

projectname = 'HelloDjango'
print('projectname is ',projectname)
inputName = input("enter a different project name or hit cr to keep the default name:")
if(inputName != ""):
    projectname = inputName
print('OK projectname is ',projectname)

pname = 0
# This is here, Just to remember how to do this
import platform
OS_Name = platform.system()
print('Running on ',OS_Name)

cwd = os.getcwd()
file_list = os.listdir(cwd)
for item in file_list:
    #print(item)
    if item == projectname:
        print(projectname,' Already Exists')
        pname = 1

i = 0
while i <= 1:
    i+=1
    print('step ',i,' started') # step 1
    try:
        djVersion = django.get_version()
        print('django version:',djVersion)
        break
    except ValueError as err:
        i+=1
        print('Value error', err)
    except OSError as err:
        i+=1
        print("OS error:", err)
    except Exception as err:
        i+=1
        print(f"Unexpected {err=}, {type(err)=}")
        raise
#print('django version:',djVersion)
#print('django version:',django.get_version())

print("step ",i," complete")  # 1
if pname > 0:
    print('Project name ',projectname,' exists, skipping this step ')
    i = 2
    pname = 1
while i <= 2 and pname == 0:
    i+=1
    print('step',i,' started') # step 2
    project = 'django-admin.py startproject '+projectname
    print('project Name: ',project)
    try:
        os.system(project)
        break
    except ValueError as err:
        i+=1
        print('Value error', err)
    except CommandError as err:
        i+=1
        print('Value error', err)
    except OSError as err:
        i+=1
        print("OS error:", err)
    except Exception as err:
        i+=1
        print(f"Unexpected {err=}, {type(err)=}")
        raise

print('python -m django startproject ',projectname)

t = 'python -m django startproject '+ projectname 
print(t)

print("step ",i," complete")  # 2

if pname > 0:
    print('Project name ',projectname,' exists, skipping this step ')
    i = 4

while i <= 3 and pname == 0:
    i+=1
    print('step ',i,' started')
    try:
        #os.system('python -m django startproject ',projectname);# Pysite')
        os.system(t);# Pysite')
        break
    except NameError:
        i+=1
        print('NameError:')
    except RuntimeError as err:
        i+=1
        print('RuntimeError:', err)
    except SyntaxError as err:
        i+=1
        print('SyntaxError:', err)
    except ImportError as err:
        i+=1
        print('ImportError:', err)
    except IndexError as err:
        i+=1
        print('IndexError:', err)
    except ValueError as err:
        i+=1
        print('Value error', err)
    except OSERROR as err:
        i+=1
        print("OS error:", err)
    except Exception as err:
        i+=1
        print(f"Unexpected {err=}, {type(err)=}")
        raise
print("step ",i)," complete"  # 3

#i = 0
list = ''
import subprocess
if OS_Name == 'Windows':
    list = 'dir'
    #os.system('dir')
    #subprocess.run(["dir"]) 
elif 'Linux':
    list = 'ls -alFtr'
    #os.system('ls -alFtr')
    #subprocess.run(["ls", "-l"]) 

#os.system('ls -alFtr')
#os.system('django-admin startproject mysite')

while i <= 4:
    i+=1
    print('step ',i,' started')
    try:
        os.system(list) # just to prove it works
        break
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

print("step ",i," complete")

file_list = os.listdir(cwd)
for item in file_list:
    #print(item)
    if item == projectname:
        print(projectname,' Exists')
        
print('http://localhost:8080/')
#os.system('cd ',projectname) #Pysite')
"""
"""
#os.systme('python ',projectname,'/manage.py runserver 8080')
#os.system('python Pysite/manage.py runserver 8080')

