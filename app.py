import logging
from flask import jsonify
from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
db = SQLAlchemy(app)

# تنظیمات لاگ
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("app.log"),     # لاگ در فایل
        logging.StreamHandler()             # لاگ در ترمینال
    ]
)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))

@app.route("/")
def index():
    return Response("سلام! این صفحه‌ی اصلیه", content_type="text/html; charset=utf-8")

@app.route("/status")
def status():
    return Response("وضعیت سالمه ✅", content_type="text/html; charset=utf-8")

@app.route("/visit")
def visit():
    from flask import request
    visitor = Visitor(ip=request.remote_addr)
    
    ip = request.remote_addr
    app.logger.info(f"Visit from {ip}")

    db.session.add(visitor)
    db.session.commit()
    return f"IP {visitor.ip} ثبت شد!"

@app.route("/health")
def health():
    app.logger.info("Health check called")
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
