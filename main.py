import os
from dotenv import load_dotenv
from instagrapi import Client

# تحميل البيانات من ملف .env
load_dotenv()

username = os.getenv("INSTA_USER")
password = os.getenv("INSTA_PASS")

cl = Client()
cl.login(username, password)
print(f"تم تسجيل الدخول بنجاح باسم: {username}")
