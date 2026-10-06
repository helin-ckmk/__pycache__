ogrenciler = [
    ["Ahmet", [90,85,80]],
    ["Merve",[88,92,94]],
    ["Cem",[65,70,72]]
]
for ogrenci in ogrenciler:
    ad, notlar = ogrenci
    ortalama = sum(notlar) / len(notlar)
    print(f"{ad} - Ortama Not: {ortalama:.2f}")