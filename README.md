# Tasks

## Instalación
Descargar el repositorio con:

```
git clone git@github.com:fedemarkco/yuhu.git
```
El proyecto se encuentra en un contenedor Docker, para poder levantarlo, se tiene que ejecutar:

```
cd yuhu
docker-compose up --build
```
He puesto que cree un superusuario con los siguientes datos (para la autenticación):
<br>Username: Marco
<br>Password: 1234

La paginación es de 10 y para chequear la documentación de la api se puede ingresar a:

```
http://localhost:8000/swagger/

```

Se agregó un archivo .env_example que se deberá tomar como ejemplo para crear el archivo .env en donde se encontrarán las variables de entorno.
