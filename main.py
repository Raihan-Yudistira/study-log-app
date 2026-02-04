catatan = []

# set untuk menyimpan mapel favorit (unik)
favorit = set()

def tambah_catatan():
    """Minta input `mapel`, `topik`, dan `durasi` (menit) lalu simpan ke list `catatan`.

    Struktur yang disimpan: {'mapel': str, 'topik': str, 'durasi_menit': int}
    Fungsi melakukan validasi sederhana agar mudah dipahami pemula.
    """
    mapel = input("Mapel: ").strip()
    if not mapel:
        print("Mapel tidak boleh kosong.")
        return

    topik = input("Topik: ").strip()
    if not topik:
        print("Topik tidak boleh kosong.")
        return

    # validasi durasi — harus bilangan bulat positif
    while True:
        durasi = input("Durasi belajar (menit): ").strip()
        if not durasi:
            print("Durasi tidak boleh kosong.")
            continue
        if not durasi.isdigit():
            print("Masukkan angka bulat saja (contoh: 25).")
            continue
        durasi_menit = int(durasi)
        if durasi_menit <= 0:
            print("Durasi harus lebih dari 0.")
            continue
        break

    entry = {
        'mapel': mapel,
        'topik': topik,
        'durasi_menit': durasi_menit,
    }

    catatan.append(entry)
    print(f"✅ Catatan ditambahkan: {mapel} — {topik} ({durasi_menit} menit)")
    return entry

def lihat_catatan():
    """Tampilkan semua catatan secara rapi.

    Output terminal contoh:
    No  Mapel        Topik                 Durasi (menit)
    1   Matematika   Persamaan kuadrat     45

    Jika belum ada catatan, tampilkan pesan yang sesuai.
    Fungsi mengembalikan list `catatan` (berguna untuk pengujian).
    """
    if not catatan:
        print("\nBelum ada catatan belajar — tambahkan catatan dengan memilih menu 1.")
        return []

    # Tentukan lebar kolom berdasarkan isi (sederhana & ramah pemula)
    no_w = 3
    mapel_w = max(len("Mapel"), *(len(item.get('mapel', '')) for item in catatan)) + 4
    topik_w = max(len("Topik"), *(len(item.get('topik', '')) for item in catatan)) + 2
    durasi_w = max(len("Durasi (menit)"), *(len(str(item.get('durasi_menit', ''))) for item in catatan)) + 2

    # Header
    header = f"{'No'.ljust(no_w)}{'Mapel'.ljust(mapel_w)}{'Topik'.ljust(topik_w)}{'Durasi (menit)'.rjust(durasi_w)}"
    sep = '-' * len(header)
    print('\n' + header)
    print(sep)

    # Baris data
    total = 0
    for i, item in enumerate(catatan, start=1):
        m = item.get('mapel', '-')
        t = item.get('topik', '-')
        d = item.get('durasi_menit', 0)
        fav_mark = ' ★' if m in favorit else ''
        total += (d or 0)
        print(f"{str(i).ljust(no_w)}{(m + fav_mark).ljust(mapel_w)}{t.ljust(topik_w)}{str(d).rjust(durasi_w)}")

    # Footer: jumlah catatan + total waktu
    print(sep)
    print(f"Total: {len(catatan)} catatan — {total} menit")
    print("(★ = mapel favorit)")
    return catatan

    # Footer: jumlah catatan + total waktu
    print(sep)
    print(f"Total: {len(catatan)} catatan — {total} menit")
    return catatan

def tambah_favorit():
    """Tandai sebuah mapel sebagai favorit (unik)."""
    mapel = input("Mapel yang akan ditandai favorit: ").strip()
    if not mapel:
        print("Mapel tidak boleh kosong.")
        return
    favorit.add(mapel)
    print(f"✅ '{mapel}' ditandai sebagai favorit.")
    return mapel

def lihat_favorit():
    """Tampilkan daftar mapel favorit (urut alfabet)."""
    if not favorit:
        print("\nBelum ada mapel favorit — tandai mapel menggunakan menu 'Tambah mapel favorit'.")
        return []
    print("\nMapel favorit:")
    for i, m in enumerate(sorted(favorit), start=1):
        print(f"{i}. {m}")
    return list(favorit)

def total_waktu():
    """Hitung total durasi (dalam menit) dari semua catatan dan tampilkan hasilnya.

    - Jika tidak ada catatan: tampilkan pesan dan kembalikan 0
    - Mengembalikan total menit sebagai `int` (berguna untuk pengujian)
    """
    if not catatan:
        print("\nBelum ada catatan — total waktu: 0 menit")
        return 0

    total = sum((item.get('durasi_menit') or 0) for item in catatan)

    # Format jam + menit untuk keterbacaan jika >= 60 menit
    jam, menit = divmod(total, 60)
    if jam:
        print(f"\nTotal waktu belajar: {total} menit ({jam} jam {menit} menit)")
    else:
        print(f"\nTotal waktu belajar: {total} menit")

    return total

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Tambah mapel favorit")
    print("6. Lihat mapel favorit")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "5":
        tambah_favorit()
    elif pilihan == "6":
        lihat_favorit()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")