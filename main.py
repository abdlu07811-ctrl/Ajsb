import os
import time
from instagrapi import Client

# تسجيل الدخول
username = "5s.wd"
password = "07823520Aa" # يرجى التأكد من كلمة السر وتغييرها بعد انتهاء التجربة للأمان

cl = Client()
try:
    cl.login(username, password)
    print("تم الاتصال بإنستغرام بنجاح!")
except Exception as e:
    print(f"حدث خطأ في الاتصال: {e}")

# حلقة فحص الرسائل
while True:
    try:
        # فحص الرسائل الجديدة
        threads = cl.direct_threads()
        for thread in threads:
            print(f"فحص محادثة: {thread.id}")
    except Exception as e:
        print(f"حدث خطأ أثناء الفحص: {e}")
    
    # انتظار لمدة دقيقة قبل الفحص التالي
    time.sleep(60)
