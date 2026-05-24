from instagrapi import Client
import time
import os

cl = Client()

# إعدادات الحماية والتمويه الثابتة
cl.public_requests_enabled = False
cl.set_user_agent("Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")

session_file = "instagram_session.json"

# تشغيل البوت بالاعتماد الكلي على الجلسة المرفوعة يدويًا
if os.path.exists(session_file):
    try:
        print("🔄 جاري تحميل الجلسة الجاهزة من الملف...")
        cl.load_settings(session_file)
        cl.user_id = "78306536983"
        print("🚀 تم شحن الجلسة بنجاح! البوت مستعد الآن لقراءة الرسائل.")
    except Exception as e:
        print(f"❌ فشل تشغيل الجلسة المرفوعة: {e}")
else:
    print("❌ خطأ: ملف instagram_session.json غير موجود في المستودع! يرجى إنشاؤه أولاً.")

# إعداد المتغيرات والملفات لنظام المتجر
admin_username = "85.kw"
products_file = "products.txt"
orders_file = "orders.txt"
welcomed_users = set()
user_states = {}

def load_products():
    if not os.path.exists(products_file): 
        return {"منتج1": "50$"}
    products = {}
    with open(products_file, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, val = line.strip().split(":", 1)
                products[key] = val
    return products

def save_products(products_dict):
    with open(products_file, "w", encoding="utf-8") as f:
        for k, v in products_dict.items():
            f.write(f"{k}:{v}\n")

def save_order(username, full_name, product, phone, address):
    with open(orders_file, "a", encoding="utf-8") as f:
        f.write(f"المستخدم: {username} ({full_name}) | المنتج: {product} | الهاتف: {phone} | العنوان: {address}\n")

products = load_products()

def auto_reply():
    try:
        threads = cl.direct_threads(amount=3
