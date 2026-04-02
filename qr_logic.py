# Importamos os para trabajar con carpetas y rutas de archivos.
import os

# Importamos qrcode para generar la imagen QR.
import qrcode

# Nombre de la carpeta donde se guardarán las imágenes generadas.
CARPETA_SALIDA = "generated_qr"


# Esta función recibe el contenido que el usuario escribió
# y crea una imagen QR con ese contenido.
def crear_qr(contenido):
    # Si la carpeta de salida no existe, la creamos.
    if not os.path.exists(CARPETA_SALIDA):
        os.makedirs(CARPETA_SALIDA)

    # Aquí definimos el nombre del archivo.
    # Por ahora será siempre el mismo.
    # Más adelante lo puedes mejorar para que cada QR tenga nombre diferente.
    nombre_archivo = "mi_qr.png"

    # Unimos la carpeta y el nombre del archivo para obtener la ruta completa.
    ruta_completa = os.path.join(CARPETA_SALIDA, nombre_archivo)

    # qrcode.make(contenido) genera la imagen QR usando el texto o URL recibido.
    img = qrcode.make(contenido)

    # Guardamos la imagen en la ruta indicada.
    img.save(ruta_completa)

    # Regresamos solo el nombre del archivo,
    # para que Flask luego pueda mostrarlo en la página.
    return nombre_archivo