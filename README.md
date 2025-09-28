# M6_AE3_ABPRO-Ejercicio grupal
Por Sofía Lagos, Daniel Arrieta, Álvaro Ortega, Cecilia Ramos

## Contexto del Proyecto

La App de Recetas es un sitio web donde los usuarios pueden ver y explorar diversas recetas de cocina. Tiene una página de inicio con una lista de recetas, una página para cada receta individual con sus detalles, y una página de contacto.

## INICIALIZACION DEL ENTORNO VIRTUAL E INSTALACIONES

```bash
python -m venv env
env\Scripts\activate
pip install django
python.exe -m pip install --upgrade pip
python -m pip install Pillow
```

## CARGAR RECETAS INICIALES Y HACER CORRER EL SERVIDOR

```bash
python manage.py shell
exec(open('recetas_app/scripts/cargar_recetas.py', encoding='utf-8').read())
exit()
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Ctrl + C
deactivate
```