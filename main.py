# -*- coding: utf-8 -*-
import os
from flask import Flask, send_file

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    # Отдаём HTML-файл напрямую, без Jinja-шаблонизации
    return send_file(os.path.join(BASE_DIR, 'templates', 'index.html'))

if __name__ == '__main__':
    print('=' * 50)
    print('  KarpGram запущен!')
    print('  Открой в браузере: http://127.0.0.1:5000')
    print('=' * 50)
    app.run(host='0.0.0.0', port=5000, debug=False)