# Ctrl+Alt+Memes 🧠📸

Una app mínima en Flask para subir y mostrar memes sin login, sin cuentas.

---

### 🎯 Características:
- ✅ Subida de imágenes a una carpeta local (`static/memes/`)
- 🖼️ Galería automática de memes en la homepage
- 🛡️ Seguridad básica con headers HTTP (CSP, X-Frame, etc.)
- ⚙️ Sin base de datos, sin JS externo, sin complicaciones
- 🚄 Lista para desplegar en [Railway](https://railway.app) o cualquier WSGI

---

### 🧑‍💻 Uso local (desarrollo)
1. Clona el repositorio:

```bash

   git clone https://github.com/tu_usuario/ctrlaltmeme.git
   cd ctrlaltmeme

```

2. Instala dependencias:

```bash

    pip install -r requirements.txt

```

3. Asegúrate de que existe el directorio para los memes:

```bash

    mkdir -p app/static/memes

```

4. Corre la app local:

```bash

    python run.py

```

5. Abre en tu navegador:

```bash

    http://localhost:8081

```

---

### 🚀 Deploy en Railway:
1. Inicia sesión en Railway

2. Crea un nuevo proyecto y conecta tu repositorio

3. Railway detectará automáticamente el Procfile y wsgi.py

4. ¡Listo! Tu app estará en línea sin configuración extra

---

### ⚠️ Notas
- Esta app no incluye autenticación ni moderación: ten cuidado si la dejas pública.

- Ideal para entornos cerrados, tests rápidos, kioskos locales o bots automáticos.