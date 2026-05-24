from instagrapi import Client
import time
import os

cl = Client()

# إعدادات الحماية والتمويه الثابتة
cl.public_requests_enabled = False
cl.set_user_agent("Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")

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
                    print(f"لم نتمكن من إرسال إشعار للمدير: {admin_err}")
                
                del user_states[sender_id]
            continue

        if sender_id not in welcomed_users:
            welcome_msg = f"👋 أهلاً بك يا {full_name} في متجرنا الإلكتروني!"
            cl.direct_send(welcome_msg, thread_ids=[thread.id])
            welcomed_users.add(sender_id)
            time.sleep(1)
        
        if "حجز" in text:
            product_name = text.replace("حجز", "").strip()
            if product_name in products:
                user_states[sender_id] = {
                    "step": "waiting_for_phone",
                    "product": product_name,
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
            state = user_states[sender_id]
            if state["step"] == "waiting_for_phone":
                state["phone"] = text
                state["step"] = "waiting_for_address"
                cl.direct_send("📍 ممتاز، والآن يرجى كتابة عنوانك بالتفصيل لشحن الطلب:", thread_ids=[thread.id])
            elif state["step"] == "waiting_for_address":
                state["address"] = text
                save_order(sender_username, full_name, state["product"], state["phone"], state["address"])
                cl.direct_send(f"🎉 تم تأكيد حجزك لـ ({state['product']}) بنجاح يا {full_name}!\nسيتواصل معك فريق المبيعات قريباً.", thread_ids=[thread.id])
                
                try:
                    admin_thread = cl.direct_thread_by_participants([admin_username])
                    report = f"⚠️ **طلب حجز جديد** ⚠️\n\n👤 العميل: @{sender_username}\n📦 المنتج: {state['product']}\n📞 الهاتف: {state['phone']}\n📍 العنوان: {state['address']}"
                    cl.direct_send(report, thread_ids=[admin_thread.id])
                except Exception as admin_err:
                    print(f"لم نتمكن من إرسال إشعار للمدير: {admin_err}")
                
                del user_states[sender_id]
            continue

        if sender_id not in welcomed_users:
            welcome_msg = f"👋 أهلاً بك يا {full_name} في متجرنا الإلكتروني!"
            cl.direct_send(welcome_msg, thread_ids=[thread.id])
            welcomed_users.add(sender_id)
            time.sleep(1)
        
        if "حجز" in text:
            product_name = text.replace("حجز", "").strip()
            if product_name in products:
                user_states[sender_id] = {
                    "step": "waiting_for_phone",
                    "product": product_name,
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
