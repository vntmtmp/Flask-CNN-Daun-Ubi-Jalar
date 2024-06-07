import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from controller.klasifikasi import classify_image

app = Flask(__name__)
app.secret_key = 'YumikaSebriyova@2024UHM'

# Lokasi folder untuk menyimpan file yang di-upload
UPLOAD_FOLDER = 'static/klasifikasi_img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Membatasi jenis file yang diperbolehkan
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_form')
def upload_form():
    return render_template('up_klasifikasi.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # Menyimpan file dengan nama klasifikasi_img.jpg
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'klasifikasi_img.jpg')
        file.save(file_path)

        # Klasifikasi gambar
        label, confidence = classify_image(file_path)

        # Format confidence menjadi persentase
        confidence_percentage = f"{confidence * 100:.1f}"

        return render_template('result.html', label=label, confidence=confidence_percentage)
    else:
        flash('File type not allowed')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
