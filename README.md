# Recetas Deliciosas - Aplicación Web Django

**Desarrollado por:** Sofía Lagos, Daniel Arrieta, Álvaro Ortega, Cecilia Ramos  
**Proyecto:** M6_AE3_ABPRO - Ejercicio Grupal  
**Framework:** Django 5.2.6  
**Lenguaje:** Python  

## Descripción del Proyecto

Recetas Deliciosas es una aplicación web desarrollada en Django que permite a los usuarios explorar y visualizar una colección de recetas de cocina. La aplicación cuenta con una interfaz moderna y responsiva construida con Bootstrap 5, ofreciendo una experiencia de usuario intuitiva y atractiva.

## Características Principales

### Funcionalidades Implementadas
- **Página de Inicio**: Muestra las últimas 6 recetas agregadas al sistema
- **Lista de Recetas**: Vista completa de todas las recetas disponibles
- **Detalle de Receta**: Información completa de cada receta incluyendo ingredientes, instrucciones e imagen
- **Formulario de Contacto**: Sistema de contacto con validación y procesamiento mejorado
- **Panel de Administración**: Gestión completa de recetas desde Django Admin
- **Diseño Responsivo**: Compatible con dispositivos móviles y desktop

### Tecnologías Utilizadas
- **Backend**: Django 5.2.6
- **Base de Datos**: SQLite3 (desarrollo)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.3
- **Procesamiento de Imágenes**: Pillow
- **Gestión de Archivos**: Django Static/Media files

## Estructura del Proyecto

```
M6_AE3_Grupal/
├── recetas_proyecto/                 # Proyecto Django principal
│   ├── manage.py                     # Utilidad de línea de comandos de Django
│   ├── db.sqlite3                    # Base de datos SQLite
│   ├── media/                        # Archivos multimedia subidos por usuarios
│   │   ├── carbonara.jpg
│   │   ├── ensalada.jpg
│   │   └── risotto.jpg
│   ├── recetas_app/                  # Aplicación principal
│   │   ├── models.py                 # Modelos de datos
│   │   ├── views.py                  # Vistas de la aplicación
│   │   ├── urls.py                   # URLs de la aplicación
│   │   ├── forms.py                  # Formularios Django
│   │   ├── admin.py                  # Configuración del panel de administración
│   │   ├── templates/                # Plantillas HTML
│   │   │   ├── base.html
│   │   │   ├── inicio.html
│   │   │   ├── lista_recetas.html
│   │   │   ├── detalle_receta.html
│   │   │   ├── contacto.html
│   │   │   └── confirmacion_contacto.html
│   │   ├── static/                   # Archivos estáticos
│   │   │   └── images/
│   │   │       └── fondo.jpg
│   │   ├── scripts/                  # Scripts de utilidad
│   │   │   └── cargar_recetas.py
│   │   └── migrations/               # Migraciones de base de datos
│   └── recetas_proyecto/             # Configuración del proyecto
│       ├── settings.py               # Configuración principal
│       ├── urls.py                   # URLs principales
│       ├── wsgi.py                   # Configuración WSGI
│       └── asgi.py                   # Configuración ASGI
├── requirements.txt                  # Dependencias del proyecto
├── README.md                         # Documentación del proyecto
└── paso-a-paso.txt                   # Instrucciones originales
```

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/OrtegaHamel/M6_AE3_Grupal.git
   cd M6_AE3_Grupal
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```
   
   **Nota importante:** Asegúrate de usar la bandera `-r` para leer el archivo de requerimientos. 
   El comando `pip install requirements.txt` (sin `-r`) NO funcionará.

4. **Configurar la base de datos**
   ```bash
   cd recetas_proyecto
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Cargar datos de ejemplo**
   ```bash
   python manage.py shell
   exec(open('recetas_app/scripts/cargar_recetas.py', encoding='utf-8').read())
   exit()
   ```

6. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - Aplicación principal: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Uso de la Aplicación

### Para Usuarios Finales
1. **Navegación**: Utiliza el menú de navegación para acceder a las diferentes secciones
2. **Explorar Recetas**: Visualiza las recetas desde la página de inicio o la lista completa
3. **Ver Detalles**: Haz clic en "Ver Receta" para acceder a los detalles completos
4. **Contacto**: Utiliza el formulario de contacto para enviar mensajes

### Para Administradores
1. **Acceder al Panel**: Visita /admin/ e inicia sesión con credenciales de superusuario
2. **Gestionar Recetas**: Crear, editar, eliminar y organizar recetas
3. **Filtros y Búsqueda**: Utiliza las herramientas de filtrado y búsqueda en el panel
4. **Gestión de Medios**: Administra las imágenes y archivos multimedia

## Modelo de Datos

### Modelo Receta
```python
class Receta(models.Model):
    nombre = CharField(max_length=100)           # Nombre de la receta
    ingredientes = TextField()                   # Lista de ingredientes
    instrucciones = TextField()                  # Pasos de preparación
    imagen = ImageField(upload_to='recetas/')    # Imagen de la receta
    fecha_creacion = DateTimeField(auto_now_add=True)      # Fecha de creación
    fecha_actualizacion = DateTimeField(auto_now=True)     # Fecha de actualización
```

## URLs y Vistas

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | inicio | Página principal con últimas recetas |
| `/recetas/` | ListaRecetas | Lista completa de recetas |
| `/receta/<id>/` | detalle_receta | Detalle específico de una receta |
| `/contacto/` | contacto | Formulario de contacto |
| `/confirmacion-contacto/` | confirmacion_contacto | Confirmación de envío |

## Configuración de Desarrollo

### Variables de Configuración Importantes
- `DEBUG = True` (solo para desarrollo)
- `LANGUAGE_CODE = 'es'` (idioma español)
- `TIME_ZONE = 'America/Santiago'` (zona horaria)
- `MEDIA_URL` y `MEDIA_ROOT` configurados para manejo de archivos

### Archivos Estáticos y Media
- **Static Files**: `/static/` - CSS, JS, imágenes del sitio
- **Media Files**: `/media/` - Imágenes subidas por usuarios

### Configuración del Entorno Virtual
El proyecto utiliza un entorno virtual para aislar las dependencias. Información del entorno:
- **Tipo**: VirtualEnvironment
- **Python**: 3.13.7
- **Activación Windows**: `venv\Scripts\activate`
- **Activación macOS/Linux**: `source venv/bin/activate`

### Gestión de Archivos con .gitignore
El proyecto incluye un `.gitignore` completo que excluye:
- Archivos de compilación Python (`*.pyc`, `__pycache__/`)
- Entornos virtuales (`venv/`, `env/`, etc.)
- Base de datos SQLite (`*.sqlite3`, `db.sqlite3`)
- Archivos de IDEs (`.vscode/`, `.idea/`)
- Archivos del sistema operativo (`.DS_Store`, `Thumbs.db`)
- Archivos sensibles (`.env`, `*.key`)

## Solución de Problemas Comunes

### Error: "Import django.db could not be resolved"
**Causa**: Django no está instalado o el entorno virtual no está activado.
**Solución**:
```bash
# Activar entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Instalar dependencias
pip install -r requirements.txt
```

### Error: "pip install requirements.txt" no funciona
**Causa**: Comando incorrecto para instalar desde archivo de requerimientos.
**Solución**: Usar la bandera `-r`:
```bash
pip install -r requirements.txt
```

### Error: Migraciones pendientes
**Causa**: Cambios en modelos no aplicados a la base de datos.
**Solución**:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Error: Pillow no instalado para ImageField
**Causa**: Pillow es requerido para el campo de imagen en el modelo Receta.
**Solución**: Instalar desde requirements.txt (incluye Pillow 10.4.0)

## Testing

Para ejecutar las pruebas del proyecto:
```bash
python manage.py test
```

## Despliegue en Producción

### Configuraciones Necesarias
1. Cambiar `DEBUG = False`
2. Configurar `ALLOWED_HOSTS`
3. Configurar base de datos de producción
4. Configurar servidor web (Apache/Nginx)
5. Configurar manejo de archivos estáticos

### Variables de Entorno Recomendadas
```bash
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=False
DATABASE_URL=tu_url_de_base_de_datos
```

## Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto es parte de un ejercicio académico del bootcamp de programación.

## Soporte

Para soporte técnico o consultas sobre el proyecto, utiliza el formulario de contacto de la aplicación o contacta directamente a los desarrolladores.

## Historial de Versiones

- **v1.1** - Mejoras implementadas (ver CHANGELOG.md)
- **v1.0** - Versión inicial del proyecto