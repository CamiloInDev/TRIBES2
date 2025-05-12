# 👕 Tribes - Tienda de Ropa Online

**Tribes** es una página web para vender ropa alternativa. Permite que las personas se registren, inicien sesión con campos personalizados, gestionen su perfil, naveguen por productos organizados en categorías y utilicen un carrito de compras completo. El proyecto está hecho con Django (Python) y usa una base de datos para guardar los datos de usuarios, productos y carritos.

## ✨ ¿Qué tiene esta web?

- **Gestión de Usuarios**:
  - Registro de usuarios personalizado
  - Override de los usuarios por defecto con campos de teléfono y dirección
  - Inicio y cierre de sesión
  - Edición de perfil de usuario
  - Eliminación de cuenta

- **Catálogo de Productos**:
  - Organización por categorías
  - Visualización detallada de productos
  - Imágenes y descripciones
  - Navegación intuitiva

- **Carrito de Compras**:
  - Agregar productos al carrito
  - Actualizar cantidades
  - Eliminar productos
  - Calcular totales automáticamente
  - Acceso rápido desde el menú de usuario

- **Estructura y Diseño**:
  - Organización del proyecto en módulos
  - Conexión a base de datos (PostgreSQL o SQLite)
  - Diseño moderno con HTML y CSS
  - Menú desplegable para opciones de usuario

## 🧰 Lo que se usó

- Python y Django  
- Base de datos PostgreSQL  
- HTML y CSS básicos  
- Entorno virtual (venv)  

## ▶️ Cómo usarlo

1. **Abir el proyecto**  
   Abrir el proyrvtp
2. **Crear y activar el entorno virtual**  
   - En Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```  
   - En Mac/Linux:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. **Instalar lo necesario**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurar la base de datos** (en `settings.py`)  
   Cambia el nombre de la base de datos, usuario y contraseña si usas PostgreSQL.
5. **Crear las tablas**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Iniciar el servidor**  
   ```bash
   python manage.py runserver
   ```  
   Abre el navegador y entra a: http://127.0.0.1:8000

## 📁 Carpetas principales

- `usuarios`: todo lo relacionado al registro e inicio de sesión  
- `tiendaapp`: para mostrar productos más adelante  
- `templates`: archivos HTML  
- `static`: estilos (CSS)  

## 👤 Autor

Desarrollado por Camilo Infante  


---

Proyecto en desarrollo. Próximamente se agregará catálogo de productos, carrito y pagos.
