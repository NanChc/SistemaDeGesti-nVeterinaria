# 🐾 Huellas — Veterinaria

Sitio web completo para una clínica veterinaria, con frontend estático y un sistema de gestión de pacientes (CRUD) construido con Django.

---

## 📋 Descripción

**Huellas** es una aplicación web que combina una landing page institucional con un módulo interno de administración de fichas clínicas. Permite al equipo de la veterinaria registrar, consultar, editar y dar de baja a los pacientes de forma simple y organizada.

---

## ✨ Funcionalidades

- **Landing page** con secciones de inicio, servicios, equipo y contacto
- **Alta de pacientes** — registro de nombre, especie, raza, edad, dueño/a, teléfono y estado
- **Listado de fichas** con buscador en tiempo real por nombre de paciente o dueño/a
- **Modificación** de datos de un paciente existente
- **Baja de pacientes** del fichero con confirmación
- **Estados de ficha**: Activo, En tratamiento, Próximo a vacunar, Dado de baja
- Diseño **responsive** adaptado a móvil, tablet y escritorio

---

## 🛠️ Tecnologías

| Capa | Tecnología |
|---|---|
| Frontend | HTML5, Tailwind CSS |
| Backend | Python, Django |
| Base de datos | SQLite |
| Control de versiones | Git / GitHub |

---

## 🚀 Cómo correr el proyecto localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/huellas-veterinaria.git
cd huellas-veterinaria
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Correr el servidor de desarrollo

```bash
python manage.py runserver
```

Abrí el navegador en [http://localhost:8000](http://localhost:8000)

---

## 👩‍💻 Autora

**Nancy** — Desarrolladora Full Stack  
🔗 [github.com/tu-usuario](https://github.com/NanChc)

---

## 📄 Licencia

Este proyecto fue desarrollado con fines académicos y de portfolio personal.
