from instagrapi import Client

cl = Client()

# نستخدم الجلسة مباشرة لتجاوز أي حظر أو تحدي أمني
session_id = "78306536983%3AakVIDLasQXKnx6%3A18%3AAYf5bF1Y-y0L8G44n_t4yE1WlQp12P81a1N_gH5jAw"

try:
    cl.login_by_sessionid(session_id)
    print("تم تسجيل الدخول بنجاح عبر الجلسة! البوت يعمل الآن.")
    
    # هنا ضع الكود الخاص بمهام البوت (مثل الرد على الرسائل أو غيره)
    # مثال:
    # cl.inbox_seen()
    
except Exception as e:
    print(f"حدث خطأ أثناء الاتصال: {e}")
