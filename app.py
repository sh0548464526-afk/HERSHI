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
            margin: 0;
            font-family: 'Segoe UI', Arial;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-align: center;
        }

        .container {
            margin-top: 80px;
            animation: fadeIn 2s ease-in-out;
        }

        h1 {
            font-size: 52px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        }

        .image-box {
            margin-top: 30px;
        }

        img {
            max-width: 70%;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            transition: transform 0.3s;
        }

        img:hover {
            transform: scale(1.05);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        footer {
            margin-top: 50px;
            opacity: 0.8;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>ברוך הבא לאתר של הערשי!</h1>
        
        <div class="image-box">
            <img src="{{ url_for('static', filename='image.jpg') }}">
        </div>

        <footer>
            האתר נבנה באהבה ❤️
        </footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)