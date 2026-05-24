from instagrapi import Client
import time
import os

# 1. إعداد العميل وتعطيل الطلبات العامة لتجنب الأخطاء
cl = Client()
cl.public_requests_enabled = False 

# الـ Session ID الخاص بك
session_id = "78306536983%3AakVIDLasQXKnx6%3A18%3AAYf5bF1Y-y0L8G44n_t4yE1WlQp12P81a1N_gH5jAw"

# تسجيل الدخول
try:
    cl.login_by_sessionid(session_id)
    print(f"تم تسجيل الدخول بنجاح! البوت يعمل كـ: {cl.username}")
except Exception as e:
    print(f"خطأ في تسجيل الدخول: {e}")

admin_username = "85.kw"
products_file = "products.txt"
welcomed_users = set()

# تحميل المنتجات
def load_products():
    if not os.path.exists(products_file): return {"منتج1": "50$"}
    products = {}
    with open(products_file, "r") as f:
        for line in f:
            if ":" in line:
                key, val = line.strip().split(":", 1)
                products[key] = val
    return products

# حفظ المنتجات
def save_products(products):
    with open(products_file, "w") as f:
        for k, v in products.items():
            f.write(f"{k}:{v}\n")

products = load_products()

def auto_reply():
    threads = cl.direct_threads(amount=5)
    for thread in threads:
        if not thread.messages: continue
        last_message = thread.messages[0]
        sender_username = thread.users[0].username
        sender_id = thread.users[0].pk
        text = last_message.text
        
        # أوامر المدير (85.kw)
        if sender_username == admin_username:
            if text.startswith("إضافة:"):
                try:
                    _, name, price = text.split(":")
                    products[name] = price
                    save_products(products)
                    cl.direct_send(f"✅ تم حفظ {name} بسعر {price}", thread_ids=[thread.id])
                except:
                    cl.direct_send("خطأ: استخدم صيغة (إضافة:اسم:سعر)", thread_ids=[thread.id])
            elif text.startswith("حذف:"):
                _, name = text.split(":")
                if name in products:
                    del products[name]
                    save_products(products)
                    cl.direct_send(f"🗑️ تم حذف {name}", thread_ids=[thread.id])
                    
        # الترحيب والحجز للعملاء
        elif last_message.user_id != cl.user_id:
            # رسالة الترحيب
            if sender_id not in welcomed_users:
                full_name = thread.users[0].full_name or "عزيزي العميل"
                welcome_msg = f"👋 أهلاً بك يا {full_name} في متجرنا!\nكيف يمكننا مساعدتك اليوم؟"
                cl.direct_send(welcome_msg, thread_ids=[thread.id])
                welcomed_users.add(sender_id)
                time.sleep(2)
            
            # نظام الحجز
            if "حجز" in text:
                product_name = text.replace("حجز", "").strip()
                if product_name in products:
                    cl.direct_send(f"✅ تم تأكيد حجزك لـ {product_name}! سيتم التواصل معك قريباً.", thread_ids=[thread.id])
                    # إشعار المدير
                    admin_thread = cl.direct_thread_by_participants([admin_username])
                    cl.direct_send(f"⚠️ طلب حجز جديد من {sender_username}: {product_name}", thread_ids=[admin_thread.id])
                else:
                    cl.direct_send("❌ عذراً، هذا المنتج غير متوفر.", thread_ids=[thread.id])
            else:
                # عرض المنتجات
                reply_text = "📦 قائمة منتجاتنا:\n" + "\n".join([f"🔹 {k}: {v}" for k, v in products.items()])
                cl.direct_send(reply_text, thread_ids=[thread.id])

while True:
    try:
        auto_reply()
    except Exception as e:
        print(f"حدث خطأ: {e}")
    time.sleep(60)
