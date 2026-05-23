import time
from instagrapi import Client

# بيانات الدخول
username = "5s.wd"
password = "07823520Aa"

cl = Client()

# إعدادات لزيادة الأمان وتجاوز الحظر
cl.request_timeout = 10 

try:
    print("جاري محاولة تسجيل الدخول...")
    cl.login(username, password)
    print("تم تسجيل الدخول بنجاح!")
except Exception as e:
    print(f"حدث خطأ: {e}")
    # إذا فشل، سيطبع لنا السبب بالضبط
