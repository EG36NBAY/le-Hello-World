# Banka hesap kayıtlarını tutan ana liste
# Her bir hesap (kullanici_adi, bakiye) şeklinde bir TUPLE olarak saklanır.
hesaplar = [
    ("ahmet123", 1500.0),
    ("zeynep_m", 3250.50),
    ("mehmet_k", 500.0)
]

def yeni_hesap_ekle(kullanici_adi, baslangic_bakiyesi):
    """
    Yeni kullanıcı adı ve bakiye bilgisini bir tuple olarak oluşturup
    ana listeye ekler.
    """
    # Tuple oluşturma: (kullanici_adi, bakiye)
    yeni_kayit = (kullanici_adi, float(baslangic_bakiyesi))
    hesaplar.append(yeni_kayit)
    print(f"\n[+] '{kullanici_adi}' kullanıcısı başarıyla eklendi.")

def hesaplari_listele():
    """
    Listede tutulan tüm tuple kayıtlarını döngü ile okur ve ekrana basar.
    """
    print("\n--- MEVCUT BANKA HESAPLARI ---")
    if not hesaplar:
        print("Kayıtlı hesap bulunamadı.")
        return

    # Tuple Unpacking (Paket Açma) ile elemanlara doğrudan erişim
    for index, (username, bakiye) in enumerate(hesaplar, start=1):
        print(f"{index}. Kullanıcı: {username:<15} | Bakiye: {bakiye:.2f} TL")

def bakiye_sorgula(kullanici_adi):
    """
    Girilen kullanıcı adını liste içindeki tuple'larda arar.
    """
    for username, bakiye in hesaplar:
        if username == kullanici_adi:
            print(f"\n[i] {username} hesabının güncel bakiyesi: {bakiye:.2f} TL")
            return
    print(f"\n[-] '{kullanici_adi}' isimli kullanıcı bulunamadı.")


# --- PROGRAMIN ÇALIŞTIRILMASI VE GİRDİ ALINMASI ---
if __name__ == "__main__":
    while True:
        print("\n=== ENTRY LEVEL BANKACILIK SİSTEMİ ===")
        print("1 - Tüm Hesapları Listele")
        print("2 - Yeni Hesap Ekle")
        print("3 - Bakiye Sorgula")
        print("4 - Çıkış")
        
        secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

        if secim == "1":
            hesaplari_listele()

        elif secim == "2":
            user_input = input("Yeni Kullanıcı Adı: ").strip()
            para_input = input("Başlangıç Bakiyesi (TL): ").strip()
            
            try:
                bakiye_val = float(para_input)
                yeni_hesap_ekle(user_input, bakiye_val)
            except ValueError:
                print("\n[!] Hata: Bakiye miktarı sayısal bir değer olmalıdır!")

        elif secim == "3":
            sorgu_user = input("Bakiyesini görmek istediğiniz Kullanıcı Adı: ").strip()
            bakiye_sorgula(sorgu_user)

        elif secim == "4":
            print("\nSistemden çıkılıyor...")
            break

        else:
            print("\n[!] Geçersiz seçim, lütfen tekrar deneyin.")