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


## Authors
Vladimir Poplavsky https://github.com/VladimirPoplavsky \
Shaun Suhareanu https://github.com/Botnim \
Daniel Gardashnik https://github.com/Danielgard10 \
Valeria Zagorchik https://github.com/Vale-Za \
Ilya Yaverbaum https://github.com/ilyayaver95 

