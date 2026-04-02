# Importamos os para trabajar con carpetas y rutas de archivos.
import os

# Importamos la librería qrcode para generar la imagen QR.
import qrcode

# Importamos quote para convertir texto normal en texto válido para URL.
# Esto sirve para que los espacios y caracteres especiales del mensaje
# no rompan el enlace de WhatsApp.
from urllib.parse import quote

# Nombre de la carpeta donde se guardarán las imágenes QR.
CARPETA_SALIDA = "generated_qr"


# Esta función recibe el contenido que queremos convertir en QR.
# contenido: puede ser una URL, texto o en este caso un enlace de WhatsApp.
# nombre_archivo: es el nombre con el que se guardará la imagen.
def crear_qr(contenido, nombre_archivo="mi_qr.png"):
    # Si la carpeta de salida no existe, la creamos.
    if not os.path.exists(CARPETA_SALIDA):
        os.makedirs(CARPETA_SALIDA)

    # Construimos la ruta completa del archivo.
    # Ejemplo: generated_qr/mi_qr.png
    ruta_completa = os.path.join(CARPETA_SALIDA, nombre_archivo)

    # Generamos la imagen QR usando el contenido recibido.
    img = qrcode.make(contenido)

    # Guardamos la imagen en la ruta indicada.
    img.save(ruta_completa)

    # Regresamos el nombre del archivo para poder mostrarlo después en Flask.
    return nombre_archivo


# Esta función arma un enlace directo a WhatsApp.
# numero: número telefónico
# mensaje: texto opcional que aparecerá listo para enviarse
def crear_link_whatsapp(numero, mensaje=""):
    # Quitamos espacios al inicio y al final del número.
    numero = numero.strip()

    # Dejamos solo los dígitos del número.
    # Esto elimina espacios, guiones, paréntesis o signos.
    numero_limpio = "".join(c for c in numero if c.isdigit())

    # Validamos que al menos haya quedado un número válido.
    if not numero_limpio:
        raise ValueError("Debes escribir un número válido.")

    # Creamos la base del enlace de WhatsApp.
    # Formato: https://wa.me/NUMERO
    link = f"https://wa.me/{numero_limpio}"

    # Si el usuario escribió un mensaje, lo agregamos a la URL.
    # quote() convierte el mensaje a formato válido para enlace.
    if mensaje.strip():
        link += f"?text={quote(mensaje.strip())}"

    # Regresamos el link completo.
    return link