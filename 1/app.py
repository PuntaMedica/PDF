from flask import Flask, send_from_directory

app = Flask(__name__)

# Ruta para descargar el PDF
@app.route('/download')
def download():
    # send_from_directory enviará el archivo con Content-Disposition: attachment
    return send_from_directory(
        directory='static',      # carpeta donde está el PDF
        filename='mi_documento.pdf',
        as_attachment=True       # fuerza la descarga
    )

if __name__ == '__main__':
    # Hazlo accesible en tu red local
    app.run(host='0.0.0.0', port=6005)
