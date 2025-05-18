from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/memes'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    @app.after_request
    def add_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; "
            "img-src 'self' data:; "
            "style-src 'self'; "
            "script-src 'none'; "
            "object-src 'none'; "
            "frame-ancestors 'none';"
        )
        return response

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/', methods=['GET', 'POST'])
    def index():
        #if request.method == 'POST':
        #    file = request.files.get('file')
        #    if file and allowed_file(file.filename):
        #        filename = secure_filename(file.filename)
        #        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #        return redirect(url_for('index'))

        memes = sorted(os.listdir(app.config['UPLOAD_FOLDER']), reverse=True)
        return render_template('index.html', memes=memes)

    @app.route('/static/memes/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    return app

application = create_app()

