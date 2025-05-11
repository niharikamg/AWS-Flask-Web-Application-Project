
# Deploying a Flask Web App on AWS EC2

## 📌 Overview
This project demonstrates how to deploy a **Flask web application** on an **AWS EC2 instance** using **Apache**, **mod_wsgi**, and **SQLite3**.  
It includes:
- User **registration** and **authentication**
- **Profile display** with session tracking
- **File upload** with **word count analysis** (Extra Credit)

---

## 🔗 Live Links
- 🌐 Web App: http://ec2-18-118-165-82.us-east-2.compute.amazonaws.com/
- 💻 GitHub Repository: https://github.com/niharikamg/AWS-Flask-Web-App-Project

---

##  Prerequisites
- AWS account with EC2 access
- Basic terminal & Linux skills
- Python, Flask, and SQLite understanding

---

##  Setup Instructions

###  Launch EC2 Instance
1. Log in to [AWS Console](https://aws.amazon.com/)
2. Launch **Ubuntu Server 24.04 LTS** (Free Tier)
3. Allow inbound traffic for ports **22 (SSH)**, **80 (HTTP)**, and **443 (HTTPS)**
4. Generate/download a **.pem** key pair
5. Note your instance's **public IP** or **DNS**

---

###  Connect via SSH
```bash
ssh -i your-key.pem ubuntu@<your-ec2-public-ip>
````

---

###  Install Required Packages

```bash
sudo apt update
sudo apt install apache2 libapache2-mod-wsgi-py3 python3-pip python3-flask sqlite3 -y
```

---

###  Setup Flask App

```bash
sudo mkdir -p /var/www/flaskapp/templates
cd /var/www/flaskapp
```

Upload the following files:

* `flaskapp.py`
* `flaskapp.wsgi`
* `templates/register.html`
* `templates/login.html`
* `templates/profile.html`
* `templates/upload.html` (Extra Credit)

Optional local test:

```bash
python3 flaskapp.py
```

---

###  Configure Apache

```bash
sudo nano /etc/apache2/sites-available/flaskapp.conf
```

Paste:

```apache
<VirtualHost *:80>
    ServerName ec2-18-118-165-82.us-east-2.compute.amazonaws.com
    WSGIDaemonProcess flaskapp threads=5
    WSGIScriptAlias / /var/www/flaskapp/flaskapp.wsgi

    <Directory /var/www/flaskapp>
        Require all granted
    </Directory>

    Alias /static /var/www/flaskapp/static
    <Directory /var/www/flaskapp/static/>
        Require all granted
    </Directory>
</VirtualHost>
```

Enable and restart Apache:

```bash
sudo a2ensite flaskapp.conf
sudo systemctl reload apache2
```

---

##  Extra Credit: File Upload + Word Count

###  Route in `flaskapp.py`

```python
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
```

###  Create Template: `templates/upload.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Upload File</title>
</head>
<body>
    <h2>Upload Limerick File</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file"><br><br>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```

###  Create Upload Directory

```bash
mkdir /var/www/flaskapp/uploads
chmod 777 /var/www/flaskapp/uploads
```

---

##  Reference

* Tutorial followed: [Running a Flask app on AWS EC2](https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/)

---

##  Submission Details

* 🔗 EC2 URL: [http://ec2-18-118-165-82.us-east-2.compute.amazonaws.com/](http://ec2-18-118-165-82.us-east-2.compute.amazonaws.com/)
* 🔗 GitHub Repo: [https://github.com/niharikamg/AWS-Flask-Web-App-Project](https://github.com/niharikamg/AWS-Flask-Web-App-Project)

---
