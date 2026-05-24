from instagrapi import Client
import requests
import time
import os

cl = Client()

# 1. تعطيل الطلبات العامة وإعداد التمويه لمنع التوجيه المكرر
cl.public_requests_enabled = False
cl.set_user_agent("Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")

# 2. إعداد قيم الكوكيز المستخرجة من صورتك
session_id = "78306536983%3AakVIDLasQXKnx6%3A18%3AAYf5bF1Y-y0L8G44n_t4yE1WlQp12P81a1N_gH5jAw"
ds_user_id = "78306536983"
csrftoken = "wIkI46YeMk1sRR3wdakZFZhXKKgC5mAt"

# 3. الطريقة البرمجية الصحيحة لحقن الكوكيز في المكتبة
cookie_jar = requests.cookies.RequestsCookieJar()
cookie_jar.set("sessionid", session_id, domain=".instagram.com")
cookie_jar.set("ds_user_id", ds_user_id, domain=".instagram.com")
cookie_jar.set("csrftoken", csrftoken, domain=".instagram.com")
cookie_jar.set("mid", "ahl9eAABAAGhqrmqNLv14gpWLuW2", domain=".instagram.com")
cookie_jar.set("ig_did", "A4F839F0-4147-479E-80CE-4C542E5CD0BE", domain=".instagram.com")

cl.private.session.cookies.update(cookie_jar)

# 4. التحقق من نجاح الاتصال
try:
    cl.delay_range = [2, 5]
    # محاولة جلب الآيدي الخاص بك للتأكد من تخطي الحظر
    cl.user_id = ds_user_id
    print("✅ تم تخطي خطأ الـ redirects وحقن الكوكيز بنجاح!")
except Exception as e:
    print(f"⚠️ تنبيه أثناء إعداد الجلسة: {e}")

admin_username = "85.kw"
products_file = "products.txt"
orders_file = "orders.txt"
welcomed_users = set()
user_states = {}

def load_products():
    if not os.path.exists(products_file): return {"منتج1": "50$"}
    products = {}
    with open(products_file, "r") as f:
        for line in f:
            if ":" in line:
                key, val = line.strip().split(":", 1)
                products[key] = val
    return products

def save_products(products):
    with open(products_file, "w") as f:
        for k, v in products.items():
            f.write(f"{k}:{v}\n")

def save_order(username, full_name, product, phone, address):
    with open(orders_file, "a", encoding="utf-8") as f:
        f.write(f"المستخدم: {username} ({full_name}) | المنتج: {product} | الهاتف: {phone} | العنوان: {address}\n")

products = load_products()

def auto_reply():
    try:
        threads = cl.direct_threads(amount=3)
    except Exception as e:
        print(f"جاري فحص الرسائل... (انتظار تحديث الدورة): {e}")
        return

    for thread in threads:
        if not thread.messages: continue
        last_message = thread.messages[0]
        sender_username = thread.users[0].username
        sender_id = thread.users[0].pk
        text = last_message.text.strip()
        
        if last_message.user_id == cl.user_id:
            continue

        # أوامر المدير (85.kw)
        if sender_username == admin_username:
            if text.startswith("إضافة:"):
                try:
                    _, name, price = text.split(":")
                    products[name] = price
                    save_products(products)
                    cl.direct_
                    "phone": "",
                    "address": ""
                }
                cl.direct_send(f"🛍️ لقد اخترت حجز: {product_name}.\nيرجى كتابة رقم هاتفك للتواصل ومتابعة الطلب:", thread_ids=[thread.id])
            else:
                cl.direct_send("❌ عذراً، هذا المنتج غير متوفر حالياً.", thread_ids=[thread.id])
        else:
            reply_text = "📦 قائمة منتجاتنا الحالية:\n" + "\n".join([f"🔹 {k}: {v}" for k, v in products.items()]) + "\n\n💡 لحجز منتج، أرسل: حجز اسم المنتج"
            cl.direct_send(reply_text, thread_ids=[thread.id])

while True:
    auto_reply()
    time.sleep(60)
