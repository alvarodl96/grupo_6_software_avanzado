1- Descargar el servidor de Apache y MySQL, para ello se usa el entorno XAMPP:
https://www.apachefriends.org/es/index.html

2- Una vez descargado, al instalar seleccionar los componentes: 
Apache, MySQL, PHP, phpMyAdmin

3- Iniciar los servidores de Apache y MySQL, se pueden iniciar ejecutando xampp-control.exe dentro de la carpeta de instalacion de XAMMP

4- Para importar la base de datos acceder a http://localhost/phpmyadmin/ . En la pestaña importar seleccionar el archivo
universidad.sql.zip que se encuentra en la carpeta base_de_datos

5- Instalar conector para poder acceder a la base de datos desde Python.
pip install mysql-connector-python-rf

Es posible que también se necesite actualizar:
pip install -U setuptools
pip install -U wheel

6- Arrancar el servidor del API Rest para ello ir a la carpeta python-flask-server y ejecutar el comando:
python -m swagger_server
Se puede acceder al API Rest desde la página: http://localhost:8080/profesores/ui/


