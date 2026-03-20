from flask import Flask, render_template_string, url_for
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <title>האתר של הערשי</title>
    <style>
        body {
            direction: rtl;
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            margin: 0;
            padding: 0;
        }
        h1 {
            margin-top: 50px;
            font-size: 52px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        }
        img {
            margin-top: 30px;
            max-width: 70%;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transition: transform 0.3s;
        }
        img:hover {
            transform: scale(1.05);
        }
        footer {
            margin-top: 50px;
            opacity: 0.8;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>ברוך הבא לאתר של הערשי!</h1>
    <img src="{{ url_for('static', filename='image.jpg') }}" alt="תמונה">
    <footer>
        האתר נבנה באהבה
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render מספק פורט מהסביבה
    app.run(host="0.0.0.0", port=port)
