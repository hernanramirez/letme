# Configuracion para conexion Mongo DB

## Hacer pull del repositorio

```shell
git pull
```

## Crear un virtualenv con Pyrhon3

### Crear un virtualenv fuera del repositorio

```shell
virtualenv -p python3 venv_letme
```
 
### Activar el Virtual Env

```shell
source venv_letme/bin/activate
```

### Instalar los paquetes

Entrar en el directorio de la aplicación Django

```shell
pip install -r requirements.txt
```

Cambiar en el setting con tu conexión a la base de datos mongo

```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propogate': False,                        
                }
            },
         },
        'NAME': 'letmepark',
        'CLIENT': {
            'host': 'mongodb+srv://students:0ndZKyjSf3FNjy6B@cluster0-ywxsp.mongodb.net/test?retryWrites=true&w=majority',
        }
    },
}
```


### Hacer las migraciones
	
```shell
./manage.py makemigrations
./manage.py migrate
```

Ejecutar

```shell
./manage.py run server
```

Deberias ver el listado en:

http://127.0.0.1:8000/p/


