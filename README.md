# Generador de QR con Flask

Este proyecto es una aplicación web desarrollada con **Python** y **Flask** que permite generar códigos QR a partir de un texto o una URL ingresada por el usuario.

La aplicación recibe la información desde un formulario web, genera el código QR y lo muestra en una página de resultado, donde también se puede descargar la imagen.

---

## Características

- Interfaz web sencilla
- Generación de códigos QR a partir de texto o URL
- Validación básica para evitar campos vacíos
- Visualización del QR generado
- Opción para descargar la imagen
- Estructura organizada con Flask

---

## Tecnologías utilizadas

- **Python**
- **Flask**
- **qrcode**
- **Pillow**
- **HTML**
- **CSS**

---

## Estructura del proyecto

generador_qr/
│
├── app.py
├── qr_logic.py
│
├── templates/
│   ├── index.html
│   └── resultado.html
│
├── static/
│   └── css/
│       └── estilos.css
│
└── generated_qr/

### Descripción de archivos y carpetas

- **app.py**  
  Archivo principal de la aplicación Flask. Aquí se definen las rutas y se conecta el formulario con la lógica del QR.

- **qr_logic.py**  
  Contiene la función que genera el código QR y guarda la imagen en la carpeta correspondiente.

- **templates/**  
  Contiene los archivos HTML de la aplicación.

- **static/**  
  Contiene los archivos estáticos, como CSS, imágenes o JavaScript.

- **generated_qr/**  
  Carpeta donde se guardan los códigos QR generados.

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3
- pip

---

## Instalación

1. Clona este repositorio o descarga los archivos del proyecto.
2. Abre una terminal dentro de la carpeta del proyecto.
3. Instala las dependencias con el siguiente comando:

```bash
pip install flask qrcode pillow