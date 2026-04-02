# Importamos Flask y herramientas que vamos a usar.
# Flask: crea la aplicación web.
# render_template: muestra archivos HTML.
# request: permite leer datos enviados desde formularios.
# send_from_directory: sirve para mostrar archivos guardados en una carpeta.
from flask import Flask, render_template, request, send_from_directory

# Importamos dos funciones desde qr_logic.py
# crear_qr: genera la imagen del código QR
# crear_link_whatsapp: construye el enlace de WhatsApp con número y mensaje
from qr_logic import crear_qr, crear_link_whatsapp

# Creamos la aplicación Flask.
# __name__ ayuda a Flask a ubicar carpetas como templates y static.
app = Flask(__name__)

# Guardamos en una variable el nombre de la carpeta
# donde se van a almacenar los QR generados.
CARPETA_QR = "generated_qr"


# Esta ruta corresponde a la página principal.
# Cuando el usuario entra a "/", Flask ejecuta esta función.
@app.route("/")
def inicio():
    # Mostramos el archivo index.html que está en la carpeta templates.
    return render_template("index.html")


# Esta ruta procesa el formulario del QR de WhatsApp.
# Solo acepta el método POST porque recibe datos enviados desde el formulario.
@app.route("/generar-whatsapp", methods=["POST"])
def generar_whatsapp():
    # Obtenemos el número que el usuario escribió en el input llamado "numero".
    # Si no existe, usamos una cadena vacía "".
    # .strip() elimina espacios al inicio y al final.
    numero = request.form.get("numero", "").strip()

    # Obtenemos el mensaje opcional del input llamado "mensaje".
    mensaje = request.form.get("mensaje", "").strip()

    # Validamos que sí se haya escrito un número.
    # Si no hay número, regresamos al formulario con un mensaje de error.
    if not numero:
        return render_template(
            "index.html",
            error="Por favor, escribe un número de WhatsApp."
        )

    try:
        # Creamos el link de WhatsApp.
        # Ejemplo:
        # https://wa.me/5215512345678?text=Hola
        link_whatsapp = crear_link_whatsapp(numero, mensaje)

        # Generamos el QR usando ese enlace.
        # El segundo parámetro es el nombre del archivo que se guardará.
        nombre_archivo = crear_qr(link_whatsapp, "qr_whatsapp.png")

    except ValueError as e:
        # Si ocurre un error de validación (por ejemplo número inválido),
        # regresamos al formulario mostrando el error.
        return render_template("index.html", error=str(e))

    except Exception as e:
        # Si ocurre cualquier otro error no esperado,
        # mostramos un mensaje simple.
        return f"Error interno: {e}"

    # Si todo sale bien, mostramos la pantalla de resultado.
    # Enviamos dos datos al HTML:
    # qr_generado: nombre del archivo QR creado
    # contenido: el link de WhatsApp que se convirtió en QR
    return render_template(
        "resultado.html",
        qr_generado=nombre_archivo,
        contenido=link_whatsapp
    )


# Esta ruta sirve para mostrar el archivo QR guardado dentro de generated_qr.
# <nombre_archivo> significa que esa parte de la URL cambia dinámicamente.
# Ejemplo: /qr/qr_whatsapp.png
@app.route("/qr/<nombre_archivo>")
def mostrar_qr(nombre_archivo):
    # Busca el archivo dentro de la carpeta generated_qr
    # y lo envía al navegador.
    return send_from_directory(CARPETA_QR, nombre_archivo)


# Esto hace que la aplicación se ejecute solo si abrimos app.py directamente.
if __name__ == "__main__":
    # debug=True es útil mientras desarrollas:
    # - recarga la app automáticamente cuando guardas cambios
    # - muestra errores detallados en pantalla
    app.run(debug=True)