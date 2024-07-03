# hans_library
En este proyecto implementaremos una API para una Biblioteca Digital, la cual será desplegada en un Droplet de DigitalOcean, utilizando un servidor Nginx y PM2. Una vez en la nube, las APIs de GET serán consumidas por una aplicación web, permitiendo la visualización de la información almacenada en nuestra base de datos.

### Objetivos:
* Perfeccionar la lógica de creación de APIs con FastAPI.
* Desplegar aplicaciones en DigitalOcean.
* Consumir APIs mediante una aplicación web.

### Aplicación Web:
Nuestra página web es una aplicación CRUD que permite crear, eliminar, actualizar y visualizar registros de libros. Además, incluye la funcionalidad de crear categorías, las cuales están asociadas a los libros como atributos. Todos estos procesos se realizan a través de endpoints conectados a nuestra base de datos mediante una API. Posteriormente, la aplicación se implementa en un servidor Nginx dentro de un droplet en DigitalOcean.

Si deseas acceder a nuestra aplicación web, [haz clic aquí.][http://157.230.222.10/]

### Capturas de Pantalla:
**INICIO**
Al ingresar, nos encontramos con la siguiente página de inicio:
![Inicio](imagenes/img1)

**LIBROS DISPONIBLES**
Dentro de la sección de ‘Libros Disponibles’ hacemos uso de los endpoints GET BOOKS, puesto que nos muestra toda la información de los libros que tenemos creados en nuestra base de datos, podemos filtrar por medio de código o categoria, al igual que actualizar o eliminar los libros :
![Libros Disponibles](imagenes/img2)

**REGISTRAR LIBRO**
Dentro de la sección ‘Registrar Libro’ podremos crear un nuevo libro con ayuda de nuestro endpoint CREATE BOOK:
![Libros Disponibles](imagenes/img3)

**CREAR CATEGORÍAS**
Finalmente, en nuestra última sección ‘Crear Categoria’ podremos ver todas las categorías que tenemos creadas, filtrarlas por ID, actualizarlas o eliminarlas, todo esto con ayuda de nuestros endpoints de CATEGORIAS:
![Libros Disponibles](imagenes/img4)




