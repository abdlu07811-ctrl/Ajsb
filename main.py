import os
import time
from instagrapi import Client

# بيانات الحساب
username = "5s.wd"
password = "07823520Aa"
session_file = "session.json"

cl = Client()

def login():
    if os.path.exists(session_file):
        print("جاري تحميل الجلسة المحفوظة...")
        cl.load_settings(session_file)
        cl.login(username, password)
    else:
        print("جاري تسجيل دخول جديد وحفظ الجلسة...")
        cl.login(username, password)
        cl.dump_settings(session_file)
    print("تم تسجيل الدخول بنجاح!")

# تشغيل عملية الدخول
try:
    login()
except Exception as e:
    print(f"خطأ في الدخول: {e}")

# حلقة عمل البوت
while True:
    try:
        # هنا يمكنك وضع أوامر البوت الخاصة بك
        print("البوت يعمل الآن ويراقب الرسائل...")
        time.sleep(60)
    except Exception as e:
        print(f"حدث خطأ: {e}")
        time.sleep(60)
