# TuPrimeraPagina - Ferrante

Web creada en Django para el curso de Python de Coderhouse.

## Descripción

Aplicación de inventario de componentes de hardware. Permite registrar, visualizar, editar y eliminar componentes, organizados por marca y categoría. Cuenta con un sistema de cuentas de usuario con perfil editable.

## Uso

### Página de inicio

Al ingresar a la web se muestra una navbar con las secciones "Inventario", "Marcas", "Categorías" y opciones de cuenta. También hay dos botones: "Nuevo Componente" y "Ver Catálogo".

---

### Componentes

- **Ver el catálogo:** Accesible desde la navbar en "Inventario" o desde el botón "Ver Catálogo" en el inicio. No requiere estar registrado. Se listan todos los componentes con su imagen, modelo y precio.
- **Buscar un componente:** En la página del catálogo hay un campo de búsqueda. Al ingresar un nombre de modelo, la lista se filtra automáticamente.
- **Ver el detalle de un componente:** Al hacer click sobre un componente del catálogo se accede a su página con toda la información: imagen, modelo, SKU, precio, descripción, marca, categoría y fecha de ingreso.
- **Crear un componente:** Disponible desde el botón "Nuevo Componente" o la navbar. Solo accesible para admins. No es posible crear un componente si no existe al menos una marca y una categoría previamente cargadas, ya que son campos obligatorios.
- **Editar un componente:** Desde la página de detalle del componente se puede acceder al botón "Editar". Solo accesible para admins.
- **Eliminar un componente:** Desde la página de detalle del componente se puede acceder al botón "Eliminar". Se muestra una pantalla de confirmación antes de borrar. Solo accesible para admins.

---

### Marcas

- **Crear una marca:** Accesible desde la navbar en "Marcas". Solo accesible para admins. Es necesario tener al menos una marca creada antes de poder registrar un componente.

---

### Categorías

- **Crear una categoría:** Accesible desde la navbar en "Categorías". Solo accesible para admins. Es necesario tener al menos una categoría creada antes de poder registrar un componente.

---

### Cuentas de usuario

- **Registrarse:** Desde la navbar en "Registrarse" se completa el formulario con usuario, email y contraseña. Al finalizar, el usuario queda logueado automáticamente y es redirigido a su perfil.
- **Iniciar sesión:** Desde la navbar en "Login" se ingresan las credenciales.
- **Cerrar sesión:** Disponible desde la navbar en "Logout".
- **Ver perfil:** Una vez logueado, desde la navbar se puede acceder a la página de perfil con todos los datos del usuario.
- **Editar perfil:** Desde la página de perfil, con el botón "Editar perfil", se pueden modificar nombre, apellido, email, DNI, teléfono, dirección, país y foto de avatar. No es accesible sin estar logueado.
- **Cambiar contraseña:** Desde la página de perfil con el botón "Cambiar contraseña". No es accesible sin estar logueado.

---

## Tecnologías

- Python / Django
- HTML / Bootstrap
