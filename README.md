# team-10-backend

proyecto-6


# api base

# requerimientos:

python 3.8 o superior

# instalacion

# windows:

python -m venv venv <br />
./venv/Scripts/activate <br />
pip install -r requirements.txt <br />
cd plataforma <br />
importante pegar el archivo .env en la carpeta crudCyE  <br />
python manage.py makemigrations <br />
python manage.py migrate <br />
python manage.py runserver <br />

# linux:

virtualenv -p python3 . <br />
source ./bin/activate <br />
pip install -r requirements.txt <br />
cd plataforma <br />
importante pegar el archivo .env en la carpeta crudCyE  <br />
python3 manage.py makemigrations <br />
python3 manage.py migrate <br />
python3 manage.py runserver <br />



# endpoints

# cursos:

crear curso
soporta peticiones GET, POST, PUT y DELETE
http://127.0.0.1:8000/api/curso/
 
eliminar o editar curso
para peticiones PUT y DELETE se pone el numero de id al final
http://127.0.0.1:8000/api/cursos/1/

listar todos los cursos disponibles
http://127.0.0.1:8000/api/cursos/

crear categorias
http://127.0.0.1:8000/api/categorias/

crear y listar roles
http://127.0.0.1:8000/api/groups/

para editar o eliminar un rol se agrega el id al final
http://127.0.0.1:8000/api/groups/1/

listar profesores
http://127.0.0.1:8000/api/users/profesores/

listar estudiantes
http://127.0.0.1:8000/api/users/estudiantes/

obtener informacion de el usuario que esta logueado
http://127.0.0.1:8000/api/user_info/


# categorias:

crear categoria
soporta peticiones GET, POST, PUT y DELETE
http://127.0.0.1:8000/api/categorias/

eliminar o editar categoria
para peticiones PUT y DELETE se pone el numero de id al final
http://127.0.0.1:8000/api/categorias/1/


# autenticacion:

registro de usuario
http://127.0.0.1:8000/api/auth/signup/

inicio de sesion
http://127.0.0.1:8000/api/auth/login/

cerrar cesion
http://127.0.0.1:8000/api/auth/logout/

recuperar contraseña olvidada
http://127.0.0.1:8000/api/auth/reset/

