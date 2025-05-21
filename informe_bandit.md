Working... ---------------------------------------- 100% 0:00:00
Run started:2025-05-21 01:29:37.550541

Test results:
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'django-insecure-jk_o+#rkhznm0%spwg36ji%)m9w1smxy6mo!q7!200tiz6$%@a'
   Severity: Low   Confidence: Medium
   CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
   More Info: https://bandit.readthedocs.io/en/1.8.3/plugins/b105_hardcoded_password_string.html
   Location: Tienda\mystore\settings.py:24:13
23	# SECURITY WARNING: keep the secret key used in production secret!
24	SECRET_KEY = 'django-insecure-jk_o+#rkhznm0%spwg36ji%)m9w1smxy6mo!q7!200tiz6$%@a'
25	

--------------------------------------------------

Code scanned:
	Total lines of code: 657
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 1
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 1
		High: 0
Files skipped (0):


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
