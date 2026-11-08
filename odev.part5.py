from datetime import datetime

sinav = input("Sınav tarihi gir (Örnek: 2027-06-15 10:00): ")

# Aradaki karmaşık ayarlara takılmadan direkt standart formatı okur
sinavtarihi = datetime.fromisoformat(sinav)

bugun = datetime.now()

fark = sinavtarihi - bugun
toplam_saniye = fark.total_seconds()

kalan_gun = int(toplam_saniye // 86400)
kalan_saat = int((toplam_saniye % 86400) // 3600)

print(f"Kalan gün: {kalan_gun}, Kalan saat: {kalan_saat}")