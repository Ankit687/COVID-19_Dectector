# COVID-19_Predictor
## this web app will predict COVID-19 with x-ray of heart using Deep learning model

this command will give root access to user
<pre>sudo chown -R $USER:$USER .</pre>

create container and start django project
<pre>sudo docker-compose run webapp django-admin startproject Detector_COVID .</pre>

all folders is given root access to user 
<pre>sudo chown -R $USER:$USER .</pre>

run container
<pre>sudo docker-compose up</pre>

create django app
<pre>sudo docker exec webapp python manage.py startapp Detector</pre>

all folders is given root access to user 
<pre>sudo chown -R $USER:$USER .</pre>

create static folder for static files(css and javascript files & photos and videos)in running container
<pre>sudo docker exec webapp mkdir static</pre>

create templates folder for html files in running containser
<pre>sudo docker exec webapp mkdir templates</pre>

migrate command for database in running container
<pre>sudo docker exec webapp python manage.py migrate</pre>

create superuser in running container
<pre>sudo docker exec -it webapp python manage.py createsuperuser</pre>

installing Pillow library
<pre>sudo docker exec webapp pip install Pillow</pre>

create makemigration for database in running container
<pre>sudo docker exec webapp python manage.py makemigrations</pre>

