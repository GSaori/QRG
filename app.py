# Importamos Flask y algunas herramientas que vamos a usar:
# - Flask: crea la aplicación web
# - render_template: sirve para mostrar archivos HTML
# - request: sirve para leer los datos enviados desde un formulario
# - send_from_directory: sirve para mostrar o descargar archivos guardados en una carpeta
from flask import Flask, render_template, request, send_from_directory

# Importamos la función crear_qr desde otro archivo.
# Esa función será la encargada de generar la imagen QR.
from qr_logic import crear_qr

# Aquí creamos la aplicación Flask.
# __name__ ayuda a Flask a ubicar carpetas como templates y static.
app = Flask(__name__)

# Guardamos en una variable el nombre de la carpeta donde estarán los QR generados.
CARPETA_QR = "generated_qr"


# Esta ruta representa la página principal de la app.
# Cuando el usuario entre a http://127.0.0.1:5000/
# Flask ejecutará esta función.
@app.route("/")
def inicio():
    # Renderiza y muestra el archivo index.html
    # que está dentro de la carpeta templates.
    return render_template("index.html")


# Esta ruta se encargará de procesar el formulario.
# Solo acepta el método POST porque el formulario enviará datos.
@app.route("/generar", methods=["POST"])
def generar():
    # request.form obtiene los datos que vienen del formulario HTML.
    # "contenido" debe coincidir con el atributo name del input en index.html.
    # .strip() elimina espacios al inicio y al final.
    contenido = request.form.get("contenido", "").strip()

    # Validamos que el usuario sí haya escrito algo.
    # Si la caja está vacía, volvemos a mostrar index.html
    # y mandamos un mensaje de error.
    if not contenido:
        return render_template(
            "index.html",
            error="Por favor, escribe un texto o URL."
        )

    # Si sí hay contenido, llamamos a la función crear_qr()
    # que está en qr_logic.py
    # Esa función crea la imagen y nos devuelve el nombre del archivo generado.
    nombre_archivo = crear_qr(contenido)

    # Después mostramos la página resultado.html
    # y le mandamos dos datos:
    # - qr_generado: nombre del archivo de imagen
    # - contenido: el texto o URL que escribió el usuario
    return render_template(
        "resultado.html",
        qr_generado=nombre_archivo,
        contenido=contenido
    )


# Esta ruta sirve para mostrar el archivo QR guardado dentro de generated_qr.
# <nombre_archivo> significa que esa parte de la URL cambiará dinámicamente.
# Ejemplo: /qr/mi_qr.png
@app.route("/qr/<nombre_archivo>")
def mostrar_qr(nombre_archivo):
    # send_from_directory busca el archivo dentro de la carpeta indicada
    # y se lo entrega al navegador.
    return send_from_directory(CARPETA_QR, nombre_archivo)


# Esta parte hace que el programa se ejecute solo si abrimos app.py directamente.
if __name__ == "__main__":
    # debug=True sirve durante el desarrollo:
    # - recarga automáticamente si guardas cambios
    # - muestra errores más detallados
    app.run(debug=True)