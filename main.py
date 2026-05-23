import os
import time
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()
cl = Client()

try:
    cl.login(os.getenv("INSTA_USER"), os.getenv("INSTA_PASS"))
    print("تم تسجيل الدخول بنجاح")
except Exception as e:
    print(f"فشل تسجيل الدخول: {e}")

user_states = {}
ADMIN_ID = "73347573618" 

def handle_message(thread_id, user_id, text):
    if user_id not in user_states:
        user_states[user_id] = {'step': 1}
        cl.direct_send("مرحباً بك في متجر 5s.wd! يرجى كتابة اسم المنتج:", thread_ids=[thread_id])
        return

    step = user_states[user_id]['step']
    
    if step == 1:
        user_states[user_id].update({'product': text, 'step': 2})
        cl.direct_send("ما هو اسمك الكريم؟", thread_ids=[thread_id])
    elif step == 2:
        user_states[user_id].update({'name': text, 'step': 3})
        cl.direct_send("رقم هاتفك؟", thread_ids=[thread_id])
    elif step == 3:
        user_states[user_id].update({'phone': text, 'step': 4})
        cl.direct_send("عنوانك؟", thread_ids=[thread_id])
    elif step == 4:
        user_states[user_id]['address'] = text
        order = user_states[user_id]
        
        cl.direct_send("تم تأكيد طلبك بنجاح!", thread_ids=[thread_id])
        
        order_summary = f"طلب جديد:\nالاسم: {order['name']}\nالمنتج: {order['product']}\nالهاتف: {order['phone']}\nالعنوان: {order['address']}"
        cl.direct_send(order_summary, user_ids=[ADMIN_ID])
        
        del user_states[user_id]

while True:
    try:
        threads = cl.direct_threads()
        for thread in threads:
            last_message = thread.messages[0]
            if last_message.user_id != cl.user_id:
                handle_message(thread.id, last_message.user_id, last_message.text)
    except Exception as e:
        print(f"خطأ: {e}")
    
    # فحص كل دقيقة
    time.sleep(60)
فحص كل دقيقة
