gorevler = [] # Görevlerin tutulduğu liste
DOSYA_ADI = "gorevler.txt" # Görevlerin kaydedileceği dosya adı

def dosyadan_oku():
    """Kayıtlı görevleri dosyadan okuyarak listeye yükleyen fonksiyon."""
    global gorevler
    try:
        # Dosya varsa içeriğini satır satır okuyup görev listesine ekler
        with open(DOSYA_ADI, "r", encoding = "utf-8") as dosya:
            gorevler = [satir.strip() for satir in dosya.readlines() if satir.strip()]
        print("Görevler başarıyla yüklendi.")
    except FileNotFoundError:
        # Dosya yoksa boş bir görev listesi başlatılır
        print("Görev dosyası bulunamadı. Yeni bir liste oluşturuldu.")
        gorevler = []
    except Exception as e:
        print(f"Dosya okuma hatası: {e}")
        gorevler = []

def dosyaya_yaz():
    """Mevcut görevleri dosyaya kaydeden fonksiyon."""
    try:
        # Listedeki her görevi dosyaya yazar
        with open(DOSYA_ADI, "w", encoding = "utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")
        print("Görevler başarıyla kaydedildi.")
    except Exception as e:
        print(f"Dosya yazma hatası: {e}")

def gorevleri_listele():
    """Mevcut görevleri numaralı şekilde ekrana yazdıran fonksiyon."""
    if not gorevler:
        print("Henüz görev bulunmamaktadır.")
    else:
        print("\n--- GÖREV LİSTESİ ---")
        for i, gorev in enumerate(gorevler, 1): # 1'den başlayarak numaralandırılır
            print(f"{i}. {gorev}")
        print("--------------------")

def yeni_gorev_ekle():
    """Kullanıcıdan yeni bir görev alıp listeye ekleyen fonksiyon."""
    while True:
        gorev = input("Yeni görev: ").strip() # Kullanıcıdan görev bilgisi alınır ve baştaki ve/veya sondaki boşluklar silinir
        if gorev:
            gorevler.append(gorev)
            print(f"'{gorev}' görevi eklendi.")
            dosyaya_yaz()
            break
        else:
            print("Boş görev eklenemez!") # Kullanıcının boş giriş yapmasına karşı önlem

def gorev_duzenle():
    """Mevcut bir görevi düzenlemeye yarayan fonksiyon."""
    gorevleri_listele()
    if not gorevler:
        return
    while True:
        try:
            gorev_no = input("Düzenlemek istediğiniz görevin numarası: ")
            if not gorev_no:
                print("Lütfen bir sayı girin!")
                continue
            gorev_no = int(gorev_no)
            if 1 <= gorev_no <= len(gorevler):
                # Eski görev yerine yeni görev metni alınır
                yeni_gorev = input(f"Yeni görev metni ({gorevler[gorev_no-1]}): ").strip()
                if yeni_gorev:
                    gorevler[gorev_no-1] = yeni_gorev
                    print("Görev başarıyla güncellendi.")
                    dosyaya_yaz()
                    break
                else:
                    print("Boş görev eklenemez!")
            else:
                print("Geçersiz görev numarası!")
        except ValueError:
            print("Lütfen bir sayı girin!")

def gorev_sil():
    """Seçilen görevi silen fonksiyon."""
    gorevleri_listele()
    if not gorevler:
        return
    while True:
        try:
            gorev_no = input("Silmek istediğiniz görevin numarası: ")
            if not gorev_no:
                print("Lütfen bir sayı girin!")
                continue
            gorev_no = int(gorev_no)
            if 1 <= gorev_no <= len(gorevler):
                silinen = gorevler.pop(gorev_no-1)
                print(f"'{silinen}' görevi silindi.")
                dosyaya_yaz()
                break
            else:
                print("Geçersiz görev numarası!")
        except ValueError:
            print("Lütfen bir sayı girin!")

def ana_menu():
    """Ana menüyü kullanıcıya gösteren fonksiyon."""
    print("\n--- TO-DO LIST UYGULAMASI ---")
    print("1. Görevleri Listele")
    print("2. Yeni Görev Ekle")
    print("3. Görev Düzenle")
    print("4. Görev Sil")
    print("5. Çıkış")

def main():
    """Programın çalışmasını başlatan ana fonksiyon."""
    print("To-Do List Uygulamasına Hoş Geldiniz!")
    dosyadan_oku() # Önceden kaydedilen görevler varsa yüklenir
    while True:
        ana_menu()
        secim = input("\nSeçiminiz (1-5): ").strip()
        if secim == "1":
            gorevleri_listele()
        elif secim == "2":
            yeni_gorev_ekle()
        elif secim == "3":
            gorev_duzenle()
        elif secim == "4":
            gorev_sil()
        elif secim == "5":
            print("Programdan çıkılıyor...") # Kullanıcı çıkmak istediğinde döngü sonlanır
            break
        else:
            print("Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")

if __name__ == "__main__":
    main()