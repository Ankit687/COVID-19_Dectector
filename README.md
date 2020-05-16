# COVID-19_Dectector
this web app will detect COVID-19 with x-ray of heart using Deep learning

<pre>sudo chown -R $USER:$USER .</pre>

<pre>sudo docker-compose run webapp django-admin startproject Detector_COVID .</pre>

<pre>sudo chown -R $USER:$USER .</pre>

<pre>sudo docker-compose up</pre>

<pre>sudo docker exec ***running_container_name*** python manage.py startapp Detector</pre>

<pre>sudo chown -R $USER:$USER .</pre>

<pre>sudo docker exec ***running_container_name*** mkdir static</pre>

<pre>sudo docker exec ***running_container_name*** mkdir templates</pre>

<pre>sudo docker exec ***running_container_name*** python manage.py migrate</pre>

<pre>sudo docker exec -it ***running_container_name*** python manage.py createsuperuser</pre>

<pre>sudo docker exec ***running_container_name*** pip install Pillow</pre>

<pre>sudo docker exec ***running_container_name*** python manage.py makemigrations</pre>

