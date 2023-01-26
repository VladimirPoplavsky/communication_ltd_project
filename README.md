# communication_ltd

This site is a project created as a part of the course "Computer Security"  of HIT (Holon Institute of Technology)
This is the web system, developed for an imaginary communication company called Communication_LTD,  sells Internet packages.
The site is used by employees of the company, to manage customers and databases (add and remove customers, to associate Internet plan to specific customers)


### Installing
- If You do not have python, You can go to https://www.python.org/downloads/ to download th latest version

- create virtual environment: \
$ pip install --upgrade virtualenv \
$ virtualenv env 


- Install requirements: \
(env) $ pip install -r requirements.txt

- Make migrations:\
(env) $ python manage.py makemigrations \
(env) $ python manage.py migrate 


- create superuser: \
Before using site it's necessary to create superuser for admin login:\
(env) $ python manage.py createsuperuser\
proceed according to instruction


## Running 
- to run server: \
$ python manage.py createsuperuser  

- to run over HTTPS: \
$ python manage.py runsslserver --certificate cert.pem --key key.pem 


## Using

Login with superuser credentials that was created before\
If You forgot the password, it can be restored by email\
![image](https://user-images.githubusercontent.com/34675746/214836681-26305c80-2a58-42d0-8673-b1ed41cf1337.png)

On the top of page You can add new employees account, or change password\
![image](https://user-images.githubusercontent.com/34675746/214838138-f29af8e5-c6ca-44af-a897-8856395294e5.png)

Here You can add new internet plan\
![image](https://user-images.githubusercontent.com/34675746/214838888-459f3804-12ab-48ad-b885-ad8429f66b95.png)

![image](https://user-images.githubusercontent.com/34675746/214838970-d1703509-21f5-4d15-ada4-bea1380fa94f.png)

Also can to add new customer and to assign him internet plan\
![image](https://user-images.githubusercontent.com/34675746/214839114-a1f20395-4063-4c55-8250-fc10628ecc68.png)
![image](https://user-images.githubusercontent.com/34675746/214840346-aed89f7b-c2a8-4df4-8ea1-8018ebb57570.png)





# Architecture:


![image](https://user-images.githubusercontent.com/104764998/211631610-91102180-fd50-4eff-9faa-6b9bd1265c70.png)

# Threat modeling:

![image](https://user-images.githubusercontent.com/104764998/211631647-27d2defa-a1d0-4cb4-b590-3094c08058c4.png)


## Authors
Vladimir Poplavsky https://github.com/VladimirPoplavsky \
Shaun Suhareanu https://github.com/Botnim \
Daniel Gardashnik https://github.com/Danielgard10 \
Valeria Zagorchik https://github.com/Vale-Za \
Ilya Yaverbaum https://github.com/ilyayaver95 

