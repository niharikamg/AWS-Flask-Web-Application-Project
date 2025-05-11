import os
from flask import request, render_template

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            os.makedirs("uploads", exist_ok=True)
            path = os.path.join("uploads", file.filename)
            file.save(path)
            with open(path, 'r') as f:
                word_count = len(f.read().split())
            return f"Upload successful. Word count: {word_count}"
    return render_template('upload.html')
