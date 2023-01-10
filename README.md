# communication_ltd_2

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


- create superuser for admin login: \
(env) $ python manage.py createsuperuser 


## Running 
- to run server: \
$ python manage.py createsuperuser  

- to run over HTTPS: \
$ python manage.py runsslserver --certificate cert.pem --key key.pem 


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

