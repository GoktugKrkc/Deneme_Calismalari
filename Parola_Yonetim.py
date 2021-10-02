#import
import tkinter as tk
import random
#------------------------
def none():
    pass

#Şifre Oluştur / 9 Haneli Şifre Oluşturmaktadır.
def Sifre_Olustur():
    kucukHarf = ["a","b","c","d","e","f","g","h","j","k","m","n","o","p","r","s","t","u","v","y","z","q","w","x"]
    buyukHarf = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","Q","W","X"]
    sembol = ["!","<",">","+","%","&","/","=","?","-","_",",",".",":","*"]
    rakam = ["0","1","2","3","4","5","6","7","8","9"]
    
    parola = []
    for i in range(0,4):
        kckH = random.choice(kucukHarf)
        bykH = random.choice(buyukHarf)
        smb = random.choice(sembol)
        rkm = random.choice(rakam)
        parola.append(kckH)
        parola.append(bykH)
        parola.append(smb)
        parola.append(rkm)
        
    parola = random.sample(parola,9)
    global sifre 
    sifre = ""
    sifre = sifre.join(parola)
    sifreYazim.configure(text = sifre)

"""
    Öncelikle semboller(küçük ve büyük harfler + diğer semboller) tanımlandı.
    Tanımlanan semboller arasından rastgele seçim yapabilmek ve bu seçimleri
        kaydedebilmek için önce boş bir liste(parola) oluşturuldu. Ardından
        for döngüsü oluşturularak semboller seçildi ve bu listeye eklendi.
    random.sample ile liste içi elemanların yerleri karıştırıldı. Bunun amacı
        döngü içi küçükharf-büyükharf-sembol sıralamasını bozmaktır.
    Şifrenin atanacağı sifre değişkeni diğer def'lerde kullanılabilmek için
        global yapıldı ve .join metodu ile liste halinde şifre string yapıya çevrildi.
    Arayüzde oluşturulacak olan şifrenin ekranda gözükmesi için oluşturulan
        sifreYazim etiketine atama yapmak amacıyla .configure metodu kullanıldı.
    
"""

#-------------------------------------------------------------------------
#Şifreyi Kaydet
def SifreKayit():
    with open("Şifreler.txt","a") as sifreDosya:
        sifreDosya.write(f"Kullanıcı Adı: " + kullaniciAdi_Ent.get() + "        Kullanım Yeri: "+ kullanimYeri_Ent.get() + "        Şifre: " + sifre+"\n")
"""
    Oluşturulan şifrenin kaydedilmek ve daha sonra ulaşılabilir olması amacıyla
        Şifreler adında bir .txt dosyası oluşturuldu. Bu dosyaya; Kullanıcı Adı,
        şifrenin kullanım yeri ve şifre kaydedildi.
"""
#-------------------------------------------------------------------------
#Şifreyi Göster
def Sifre_Göster():
    dosya = open("Şifreler.txt","r")
    print(dosya.read())
"""
    İhtiyaç halinde tekrar bulunabilmesi amacıyla şifrenin okunacağı kod dizisi.
"""

#-------------------------------------------------------------------------------------
#Pencere
pencere = tk.Tk() #Arayüz taşıyıcı pencere
pencere.title("Parola Yönetim Aracı") #Pencere başlığı
pencere.geometry("450x225") #pencere boyutu
pencere.configure(bg = "darkblue") #pencerenin arkaplan rengi
pencere.minsize(width = 450, height = 225) #pencerenin minimum boyutu
pencere.maxsize(width = 450, height = 225) #pencerenin maksimum boyutu


#------------------------
#Label
kullanimYeri = tk.Label(pencere, text = "Kullanım Yeri:", bg = "darkgreen", fg = "yellow")
kullaniciAdi = tk.Label(pencere, text = "Kullanıcı Adı:", bg = "darkgreen", fg = "yellow")
sifreniz = tk.Label(pencere, text = "Şifreniz:", bg = "darkgreen", fg = "yellow")
sifreYazim = tk.Label(pencere, bg = "darkgreen", fg = "yellow")


#------------------------
#Entry
kullanimYeri_Ent = tk.Entry(pencere, bg = "darkgreen", fg = "yellow")
kullaniciAdi_Ent = tk.Entry(pencere, bg = "darkgreen", fg = "yellow")


#------------------------
#Button
sifreOlustur = tk.Button(pencere, text = "Şifre Oluştur", bg = "darkgreen", fg = "yellow", command = Sifre_Olustur)
kayitSifre = tk.Button(pencere, text = "Şifreyi Kaydedin", bg = "darkgreen", fg = "yellow", command = SifreKayit)
sifreGoster = tk.Button(pencere, text = "Şifreyi Göster", bg = "darkgreen", fg = "yellow", command = Sifre_Göster)


#------------------------
#xyz.Yerleştir
kullanimYeri.place(x = 25, y = 25)
kullaniciAdi.place(x = 25, y = 75)
sifreniz.place(x = 25,y = 125)
sifreYazim.place(x = 75, y= 125)
kullanimYeri_Ent.place(x = 175, y = 25)
kullaniciAdi_Ent.place(x = 175, y = 75)
sifreOlustur.place(x = 75, y = 175)
kayitSifre.place(x = 175, y = 175)
sifreGoster.place(x =295, y =175)


#------------------------
pencere.mainloop() #pencerenin kapanmaması için yazılan dögü kodu.
