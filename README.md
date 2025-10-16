# Sportify API ⚽

API REST desarrollada con Django y Django REST Framework para la gestión completa de equipos deportivos y sus jugadores.

## 📋 Descripción

Sportify API es una aplicación backend que permite administrar equipos deportivos y sus jugadores de manera eficiente. La aplicación proporciona endpoints RESTful para realizar operaciones CRUD completas, búsquedas avanzadas y visualización de relaciones entre entidades.

### Características Principales

- ✅ Gestión completa de equipos deportivos (CRUD)
- ✅ Gestión completa de jugadores (CRUD)
- ✅ Búsqueda de equipos por nombre o categoría
- ✅ Visualización de relaciones equipo-jugadores en JSON
- ✅ API RESTful completamente funcional
- ✅ Interfaz web navegable con Django REST Framework

## 🛠️ Tecnologías

- **Python** 3.13.3
- **Django** 5.2.7
- **Django REST Framework** 3.16.1
- **SQLite** (Base de datos)

## 🚀 Instalación

### Prerrequisitos

- Python 3.13 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/Josue-Zapata-v/project-sportify.git
cd project-sportify/src
```

2. **Crear y activar entorno virtual**

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Mac/Linux
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Iniciar servidor de desarrollo**

```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`

## 📚 Documentación de la API

### Base URL

```
http://127.0.0.1:8000/api/
```

### Endpoints - Equipos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/equipos/` | Listar todos los equipos |
| `POST` | `/equipos/` | Crear un nuevo equipo |
| `GET` | `/equipos/{id}/` | Obtener un equipo específico |
| `PUT` | `/equipos/{id}/` | Actualizar un equipo completo |
| `PATCH` | `/equipos/{id}/` | Actualizar campos específicos |
| `DELETE` | `/equipos/{id}/` | Eliminar un equipo |
| `GET` | `/equipos/?search={texto}` | Buscar por nombre o categoría |

#### Ejemplo de Petición - Crear Equipo

```json
POST /api/equipos/

{
  "nombre": "Barcelona FC",
  "ciudad": "Barcelona",
  "categoria": "Profesional"
}
```

#### Ejemplo de Respuesta

```json
{
  "id": 1,
  "nombre": "Barcelona FC",
  "ciudad": "Barcelona",
  "categoria": "Profesional",
  "jugadores": []
}
```

### Endpoints - Jugadores

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/jugadores/` | Listar todos los jugadores |
| `POST` | `/jugadores/` | Crear un nuevo jugador |
| `GET` | `/jugadores/{id}/` | Obtener un jugador específico |
| `PUT` | `/jugadores/{id}/` | Actualizar un jugador completo |
| `PATCH` | `/jugadores/{id}/` | Actualizar campos específicos |
| `DELETE` | `/jugadores/{id}/` | Eliminar un jugador |

#### Ejemplo de Petición - Crear Jugador

```json
POST /api/jugadores/

{
  "nombre": "Lionel Messi",
  "posicion": "Delantero",
  "numero_camiseta": 10,
  "equipo": 1
}
```

#### Ejemplo de Respuesta

```json
{
  "id": 1,
  "nombre": "Lionel Messi",
  "posicion": "Delantero",
  "numero_camiseta": 10,
  "equipo": 1
}
```

### Relación Equipo-Jugadores

Al consultar equipos, se incluyen automáticamente sus jugadores:

```json
GET /api/equipos/

[
  {
    "id": 1,
    "nombre": "Barcelona FC",
    "ciudad": "Barcelona",
    "categoria": "Profesional",
    "jugadores": [
      {
        "id": 1,
        "nombre": "Lionel Messi",
        "posicion": "Delantero",
        "numero_camiseta": 10,
        "equipo": 1
      }
    ]
  }
]
```

## 🧪 Pruebas

### Usando el Navegador

Django REST Framework proporciona una interfaz web navegable. Simplemente accede a:

```
http://127.0.0.1:8000/api/equipos/
http://127.0.0.1:8000/api/jugadores/
```

### Usando Postman o Thunder Client

1. **Crear un equipo (POST)**
   - URL: `http://127.0.0.1:8000/api/equipos/`
   - Body (JSON):
   ```json
   {
     "nombre": "Real Madrid",
     "ciudad": "Madrid",
     "categoria": "Profesional"
   }
   ```

2. **Crear un jugador (POST)**
   - URL: `http://127.0.0.1:8000/api/jugadores/`
   - Body (JSON):
   ```json
   {
     "nombre": "Cristiano Ronaldo",
     "posicion": "Delantero",
     "numero_camiseta": 7,
     "equipo": 1
   }
   ```

3. **Buscar equipos (GET)**
   - URL: `http://127.0.0.1:8000/api/equipos/?search=Madrid`

## 📝 Notas Importantes

- Para crear jugadores, primero debe existir al menos un equipo
- El campo `equipo` en jugadores es obligatorio (ForeignKey)
- Los IDs en las URLs deben ser números reales de registros existentes
- La búsqueda en equipos filtra por nombre y categoría simultáneamente

## 📁 Estructura del Proyecto

```
project-sportify/
├── src/
│   ├── sportify_api/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── sportify_app/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── manage.py
│   └── requirements.txt
└── README.md
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 👤 Autor

**Josue Zapata**

---

⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub!
