import os
import time
from instagrapi import Client

# بيانات تسجيل الدخول
username = "5s.wd"
password = "07823520Aa"

cl = Client()

try:
    cl.login(username, password)
    print("تم الاتصال بإنستغرام بنجاح!")
    # الحصول على معرف حسابك لاستقبال الطلبات عليه
    ADMIN_ID = cl.user_id_from_username("85k.w")
except Exception as e:
    print(f"حدث خطأ في الاتصال: {e}")
    ADMIN_ID = None

user_states = {}

def handle_message(thread_id, user_id, text):
    if user_id not in user_states:
        user_states[user_id] = {'step': 1}
        welcome_msg = "أهلاً بك يا غالي في متجرنا! 😊 نحن سعداء جداً بتواصلك معنا. \n\nمن فضلك، ما هو اسم المنتج الذي نال إعجابك وتود طلبه؟"
        cl.direct_send(welcome_msg, thread_ids=[thread_id])
        return

    step = user_states[user_id]['step']
    
    if step == 1:
        user_states[user_id].update({'product': text, 'step': 2})
        cl.direct_send("اختيار رائع جداً! 😍 نتشرف بمعرفة اسمك الكريم؟", thread_ids=[thread_id])
    elif step == 2:
        user_states[user_id].update({'name': text, 'step': 3})
        cl.direct_send("أهلاً بك يا بطل! يسعدنا تزويدنا برقم هاتفك لنتواصل معك؟ 📱", thread_ids=[thread_id])
    elif step == 3:
        user_states[user_id].update({'phone': text, 'step': 4})
        cl.direct_send("وصلنا لنهاية الطريق! أين عنوان سكنك لنرسل لك الطلب؟ 🚚", thread_ids=[thread_id])
    elif step == 4:
        user_states[user_id]['address'] = text
        order = user_states[user_id]
        
        cl.direct_send("يا سلام! تم تأكيد طلبك بنجاح. 🎉 سنقوم بتجهيزه فوراً وسيتواصل معك فريقنا قريباً. شكراً لثقتك بنا! 🙏", thread_ids=[thread_id])
        
        # إرسال الطلب لحسابك 85k.w
        if ADMIN_ID:
            order_summary = f"🚨 طلب جديد من العميل!\n\n📦 المنتج: {order['product']}\n👤 الاسم: {order['name']}\n📞 الهاتف: {order['phone']}\n📍 العنوان: {order['address']}"
            cl.direct_send(order_summary, user_ids=[ADMIN_ID])
        
        del user_states[user_id]

# تشغيل البوت وفحص الرسائل
while True:
    try:
        threads = cl.direct_threads()
        for thread in threads:
            last_message = thread.messages[0]
            if last_message.user_id != cl.user_id:
                handle_message(thread.id, last_message.user_id, last_message.text)
    except Exception as e:
        print(f"حدث خطأ أثناء الفحص: {e}")
    
    time.sleep(60)
