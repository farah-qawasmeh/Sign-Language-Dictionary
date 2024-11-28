import cv2
import speech_recognition as sr
import arabic_reshaper
from bidi.algorithm import get_display
import time
import os

path = "C:\\Users\\dell\\Desktop\\images\\"
text = str(input())

a = "قم بالتحدث..."
reshaped_text = arabic_reshaper.reshape(a)
bidi_a = get_display(reshaped_text)

s = "جاري التحويل إلى نص..."
reshaped_text = arabic_reshaper.reshape(s)
bidi_s = get_display(reshaped_text)

d = "النص المحول:"
reshaped_text = arabic_reshaper.reshape(d)
bidi_d = get_display(reshaped_text)

f = "لم يتم التعرف على الصوت"
reshaped_text = arabic_reshaper.reshape(f)
bidi_f = get_display(reshaped_text)

g = "خطأ في طلب خدمة التحويل:"
reshaped_text = arabic_reshaper.reshape(g)
bidi_g = get_display(reshaped_text)

h = "لم يتم العثور على الصورة للحرف:"
reshaped_text = arabic_reshaper.reshape(h)
bidi_h = get_display(reshaped_text)

j = "تعذر الوصول إلى الكاميرا"
reshaped_text = arabic_reshaper.reshape(j)
bidi_j = get_display(reshaped_text)

# القاموس
thisdict = {
    "أ": path + 'a.jpg',
    "ط": path + 'zz.jpg',
    "ظ": path + 'xx.jpg',
    "و": path + 'w.jpg',
    "غ": path + 'uu.jpg',
    "ث": path + 'th.jpg',
    "ت": path + 't.jpg',
    "ص": path + 'sss.jpg',
    "ش": path + 'ss.jpg',
    "س": path + 's.jpg',
    "ز": path + 'rr.jpg',
    "ر": path + 'r.jpg',
    "ع": path + 'o.jpg',
    "ن": path + 'n.jpg',
    "م": path + 'm.jpg',
    "ل": path + 'l.jpg',
    "خ": path + 'kh.jpg',
    "ك": path + 'k.jpg',
    "ه": path + 'hh.jpg',
    "ح": path + 'h.jpg',
    "ج": path + 'g.jpg',
    "ق": path + 'ff.jpg',
    "ف": path + 'f.jpg',
    "ي": path + 'e.jpg',
    "ض": path + 'ddd.jpg',
    "ذ": path + 'dd.jpg',
    "د": path + 'd.jpg',
    "ب": path + 'b.jpg',
    "ء": path + 'aaa.jpg',
    "ى": path + 'aaw.jpg',
    "ا": path + 'ab.jpg',
    "ة": path + 'tt.jpg',
    " ": path + 'ccv.jpg',
    "ؤ": path + 'ppp.jpg',
}

# دالة للحصول على اسم الملف التالي المتاح
def get_next_filename(base_filename, save_path):
    i = 1
    while True:
        filename = f"{base_filename}_{i}.mp4"
        if not os.path.exists(os.path.join(save_path, filename)):
            return filename
        i += 1

while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(bidi_a)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print(bidi_s)
        text = recognizer.recognize_google(audio, language="ar")
        
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)

        print(bidi_text, bidi_d, "\n")
    except sr.UnknownValueError:
        print(bidi_f)
        continue
    except sr.RequestError as e:
        print(bidi_g, e)
        continue
 
    for chr in text:
        img = cv2.imread(thisdict.get(chr))
        if img is not None:
            resized_image = cv2.resize(img, (600, 800))
            cv2.imshow("The dictionary", resized_image)
            cv2.waitKey(400)
        else:
            print(f"{bidi_h}{chr}")

    key = cv2.waitKey(0) & 0xFF

    if key == 27:  # مفتاح الهروب للخروج
        break
    
    if key == ord('v'):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print(bidi_j)
            break
        
        save_path = "C:\\Users\\dell\\Desktop\\"
        filename = get_next_filename("dictionary", save_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(os.path.join(save_path, filename), fourcc, 20.0, (640, 480))
        
        while True:
            isSuccess, img = cap.read()
            if not isSuccess:
                print(bidi_j)
                break
            
            out.write(img)  # كتابة الإطار في ملف الفيديو
            
            # تغيير أبعاد الفيديو
            resized_frame = cv2.resize(img, (800, 600))
            cv2.imshow('Video', resized_frame)
            
            if cv2.waitKey(20) & 0xFF == 27:  # اضغط على ESC للخروج
                break

        cap.release()
        out.release()  # حفظ ملف الفيديو
        cv2.destroyAllWindows()

cv2.destroyAllWindows()
