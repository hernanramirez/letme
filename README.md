README

Hacer pull del repositorio

Crear un virtual env con Pyrhon3

Activar el Virtual Env

Instalar los paquetes

Cambiar en el setting

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



Hacer

makemigrations
migrate

Ejecutar

./ma runsrver



