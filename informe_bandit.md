


## Resumen de errores y soluciones

**Error encontrado:**
- Bandit detectó una posible contraseña/clave secreta hardcodeada en el archivo `settings.py`:
  - `SECRET_KEY = 'django-insecure-jk_o+#rkhznm0%spwg36ji%)m9w1smxy6mo!q7!200tiz6$%@a'`
  - Severidad: Baja
  - Confianza: Media
  - CWE-259: [Más información](https://cwe.mitre.org/data/definitions/259.html)

**Solución aplicada:**
- Se creó un archivo `.env` para almacenar la variable `SECRET_KEY` de forma segura fuera del código fuente.
- Se instaló la librería `python-dotenv` y se modificó `settings.py` para cargar la clave secreta desde el archivo `.env` usando `os.environ` y `load_dotenv`.
- Se agregó `.env` al archivo `.gitignore` para evitar subir información sensible al repositorio.

**Resultado:**
- El proyecto ahora sigue buenas prácticas de seguridad y Bandit ya no debería reportar este problema si se vuelve a ejecutar el análisis.
