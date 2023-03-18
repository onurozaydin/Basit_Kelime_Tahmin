import tkinter as tk
import random


kelimeler = ['elma', 'armut', 'kiraz', 'muz', 'karpuz', 'üzüm']



def oyunu_baslat():
    global kelime
    kelime = random.choice(kelimeler)
    tahmin_giris.delete(0, tk.END)
    yanit.config(text="")
    harf_etiketleri = [harf.config(text="_") for harf in harfler]



def tahmin_kontrol():
    tahmin = tahmin_giris.get()
    if tahmin == kelime:
        yanit.config(text="Tebrikler, doğru tahmin!")
    else:
        yanit.config(text="Maalesef yanlış tahmin, tekrar deneyin.")



root = tk.Tk()
root.geometry("500x250")
root.title("Kelime Tahmin Oyunu")

baslik = tk.Label(root, text="Kelime Tahmin Oyunu", font=("Helvetica", 16))
baslik.pack(pady=10)

harfler_frame = tk.Frame(root)
harfler_frame.pack(pady=5)

kelime = random.choice(kelimeler)
harfler = [tk.Label(harfler_frame, text="_", font=("Helvetica", 24)) for _ in range(len(kelime))]
for harf in harfler:
    harf.pack(side=tk.LEFT)

tahmin_frame = tk.Frame(root)
tahmin_frame.pack(pady=5)

tahmin_etiket = tk.Label(tahmin_frame, text="Tahmininizi Girin:", font=("Helvetica", 12))
tahmin_etiket.pack(side=tk.LEFT)

tahmin_giris = tk.Entry(tahmin_frame, font=("Helvetica", 12))
tahmin_giris.pack(side=tk.LEFT, padx=5)

tahmin_buton = tk.Button(tahmin_frame, text="Tahmin Et", font=("Helvetica", 12), command=tahmin_kontrol)
tahmin_buton.pack(side=tk.LEFT, padx=5)

yanit = tk.Label(root, text="", font=("Helvetica", 12), fg="red")
yanit.pack(pady=10)

yeniden_baslat_buton = tk.Button(root, text="Yeniden Başlat", font=("Helvetica", 12), command=oyunu_baslat)
yeniden_baslat_buton.pack(pady=10)
root.mainloop()