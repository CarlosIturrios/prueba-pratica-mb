# Prueba Practica MB

## Descripción
Prueba práctica en django

## Requisitos
- Python (versión 3.+)
- Django (versión 5.0.1)

### Instalación
1. Clona este repositorio.
    ```
    git clone https://github.com/CarlosIturrios/prueba-pratica-mb.git
    ```
2. Accede al directorio de la aplicación.
    ```
    cd prueba-pratica-mb
    ```
    Antes de instalar las dependencias crea un entorno virtual (Opcional)
    ```
    python3 -m venv .env

    source .env/bin/activate
    ```
    En la terminal aparecera el prefijo (.env):
    ```
    (.env) ➜  prueba-pratica-mb git:(main)
    ```
3. Instala las dependencias.
    ```
    pip install -r requirements.txt
    ```

## Uso
1. Ejecuta las migraciones de la base de datos.
    ```
    python manage.py migrate
    ```
2. Inicia el servidor de desarrollo.
    ```
    python manage.py runserver
    ```
3. Abre tu navegador y accede a `http://localhost:8000` para ver la aplicación en funcionamiento.

4. Accede a la uri `usuarios` para visualizar la lista de usuarios y el formulario para crear uno nuevo ej: `http://localhost:8000/usuarios/`.

    4.1. Utiliza el parametro `edad` y un numero entero para filtrar los usuarios con dicha edad en la base de datos ej: `http://localhost:8000/usuarios/?edad=25`. 

    4.2. Utiliza el parametro `ordenar_por_edad` y cualquier caracter para filtrar los usuarios por edad de menor a mayor ej: `http://localhost:8000/usuarios/?ordenar_por_edad=true`.

    4.3. Utiliza el parametro `ordenar_por_apellido_paterno` y cualquier caracter para filtrar los usuarios en orden alfabetico segun su apellido paterno ej: `http://localhost:8000/usuarios/?ordenar_por_apellido_paterno=true`.

5. Accede a un usuario en particular con su `id` en la uri despues de usuarios/ para actulizar sus datos o eliminar con el metodo delete ej: `http://localhost:8000/usuarios/1`.

6. Accede a la uri `usuarios/pdf` para obtener la lista de usuarios en formato PDF ej: `http://localhost:8000/usuarios/pdf`.

    6.1. Utiliza el parametro `edad` y un numero entero para filtrar los usuarios con dicha edad en la base de datos ej: `http://localhost:8000/usuarios/pdf/?edad=29`. 

    6.2. Utiliza el parametro `ordenar_por_edad` y cualquier caracter para filtrar los usuarios por edad de menor a mayor ej: `http://localhost:8000/usuarios/pdf/?ordenar_por_edad=true`.

    6.3. Utiliza el parametro `ordenar_por_apellido_paterno` y cualquier caracter para filtrar los usuarios en orden alfabetico segun su apellido paterno ej: `http://localhost:8000/usuarios/pdf/?ordenar_por_apellido_paterno=true`.

## Estructura del Proyecto
El proyecto sigue una estructura de directorios comúnmente utilizada en aplicaciones Django:

- **pruebaPracticaMB/**: Directorio principal del proyecto pruebaPracticaMB en Django.
  - **settings.py**: Archivo de configuración principal de Django que contiene la configuración del proyecto, como la conexión a la base de datos, las aplicaciones instaladas y las claves secretas.
  - **urls.py**: Archivo de configuración de las URL de la aplicación.
  - **wsgi.py**: Archivo de configuración para el servidor WSGI (Web Server Gateway Interface).
  - **asgi.py**: Archivo de configuración para el servidor ASGI (Asynchronous Server Gateway Interface).
  - **__init__.py**: Archivo que indica a Python que este directorio debe ser tratado como un paquete.
- **usuarios/**: Directorio de la aplicación usuarios en el proyecto pruebaPracticaMB.
  - **models.py**: Archivo que contiene las definiciones de los modelos de la base de datos.
  - **views.py**: Archivo que contiene las vistas (controladores) de la aplicación.
  - **urls.py**: Archivo de configuración de las URL específicas de la aplicación.
  - **tests.py**: Archivo de configuración para realizar pruebas unitarias en las vistas.
- **usuarios/migrations/**: Directorio que contiene archivos de migración de la base de datos generados automáticamente por Django.
- **manage.py**: Script de administración de Django utilizado para realizar varias tareas, como ejecutar el servidor de desarrollo, aplicar migraciones y ejecutar pruebas.