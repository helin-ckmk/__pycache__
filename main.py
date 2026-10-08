import os

# Tüm akor verilerimiz doğrudan Python sözlüğü (dictionary) olarak kodun içinde:
CHORDS_DATA = {
    "Am": {
        "name": "A minor (La Minör)",
        "difficulty": "Kolay",
        "barre": False,
        "frets": "x 0 2 2 1 0",
        "capo_tip": "Capo gerektirmez.",
        "description": "Yeni başlayanlar için en temel akorlardan biridir."
    },
    "C": {
        "name": "C major (Do Majör)",
        "difficulty": "Kolay",
        "barre": False,
        "frets": "x 3 2 0 1 0",
        "capo_tip": "Capo gerektirmez.",
        "description": "Açık pozisyonda sık kullanılan temel majör akor."
    },
    "F": {
        "name": "F major (Fa Majör)",
        "difficulty": "Zor",
        "barre": True,
        "frets": "1 3 3 2 1 1",
        "capo_tip": "Bare basmak zor gelirse 1. perdeye capo takıp Em basabilirsin.",
        "description": "1. perdede bare (barre) tutuşu gerektirir."
    },
    "G": {
        "name": "G major (Sol Majör)",
        "difficulty": "Orta",
        "barre": False,
        "frets": "3 2 0 0 0 3",
        "capo_tip": "Capo gerektirmez.",
        "description": "Serçe ve yüzük parmağı esnekliği ister."
    }
}

def display_chord_info(chord_symbol, chord_data):
    """Akor bilgilerini ekrana düzenli şekilde basar."""
    print("\n" + "="*40)
    print(f"AKOR: {chord_symbol} - {chord_data['name']}")
    print("="*40)
    print(f"• Zorluk Seviyesi : {chord_data['difficulty']}")
    print(f"• Bare (Barre) Mi?: {'Evet ' if chord_data['barre'] else 'Hayır '}")
    print(f"• Perde/Tel Düzeni: {chord_data['frets']} (En üst telden en alt tele)")
    print(f"• Capo İpucu      : {chord_data['capo_tip']}")
    print(f"• Açıklama        : {chord_data['description']}")
    print("="*40 + "\n")

def list_all_chords(chords):
    """Mevcut tüm akorları listeler."""
    print("\n Sistemde Kayıtlı Akorlar:")
    for symbol, info in chords.items():
        barre_str = "[Bare]" if info['barre'] else "[Açık]"
        print(f"- {symbol:<4} ({info['difficulty']} {barre_str})")
    print()

def main():
    chords = CHORDS_DATA

    print("Terminal Gitar Akor Rehberi'ne Hoş Geldiniz!")
    
    while True:
        print("\nNe yapmak istersiniz?")
        print("1. Akor Ara")
        print("2. Tüm Akorları Listele")
        print("3. Çıkış")
        
        choice = input("Seçiminiz (1-3): ").strip()

        if choice == "1":
            search = input("Aramak istediğiniz akor adını girin (Örn: Am, C, F): ").strip().upper()
            
            matched_key = None
            for key in chords:
                if key.upper() == search:
                    matched_key = key
                    break
            
            if matched_key:
                display_chord_info(matched_key, chords[matched_key])
            else:
                print(f"\n '{search}' akoru bulunamadı. Lütfen listedeki akorlardan birini deneyin.")
        
        elif choice == "2":
            list_all_chords(chords)
        
        elif choice == "3":
            print("\nİyi pratikler! Gitar çalmaya devam et")
            break
        else:
            print("\nGeçersiz seçim! Lütfen 1, 2 veya 3 yazın.")

if __name__ == "__main__":
    main()