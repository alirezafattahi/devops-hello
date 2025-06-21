# تصویر پایه رسمی Python نسخه 3.10
FROM python:3.11-slim

# مسیر کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل requirements.txt به مسیر کاری
COPY requirements.txt .

# نصب کتابخانه‌های مورد نیاز
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کل پروژه به داخل کانتینر
COPY . .

# پورت مورد استفاده برنامه
EXPOSE 5000

# فرمان اجرای برنامه
CMD ["python", "app.py"]
