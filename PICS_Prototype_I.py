from datetime import datetime

from tabulate import tabulate

listKomponen = [
    {'PartCode': 'CPST0001', 'NamaKomponen': 'IC 701', 'Kategori': 'IC', 
     'Suplier': 'Panasonic', 'HargaSatuan': 700, 'StokMasuk': [{'TanggalMasuk': '2025-09-01', 'Qty': 1000, 'Keluar':[]}]},
    {'PartCode': 'CPST0002', 'NamaKomponen': 'Resistor 891', 'Kategori': 'Resistor',
     'Suplier': 'SMT', 'HargaSatuan': 500, 'StokMasuk': [{'TanggalMasuk': '2025-09-01', 'Qty': 800, 'Keluar':[]}]},
    {'PartCode': 'CPST0003', 'NamaKomponen': 'Capasitor 651', 'Kategori': 'Capasitor', 
     'Suplier': 'Semicoductor Ltd', 'HargaSatuan': 600, 'StokMasuk': [{'TanggalMasuk': '2025-09-01', 'Qty': 1200, 'Keluar':[]}]},
    {'PartCode': 'CPST0004', 'NamaKomponen': 'CN 141', 'Kategori': 'Connector', 
     'Suplier': 'Panasonic', 'HargaSatuan': 150, 'StokMasuk': [{'TanggalMasuk': '2025-09-01', 'Qty': 700, 'Keluar':[]}]},
    {'PartCode': 'CPST0005', 'NamaKomponen': 'Switch 401', 'Kategori': 'Switch', 
     'Suplier': 'Panasonic', 'HargaSatuan': 700, 'StokMasuk': [{'TanggalMasuk': '2025-09-01', 'Qty': 1300, 'Keluar':[]}]},
]

listModelProduksi = [
    {'CodeModel': 'CAT12', 'KategoriModel': 'Camera', 'NamaKonsumen': 'FujiFilm',
     'TanggalMulaiProduksi':'', 'TanggalSelesaiProduksi': '', 'StatusApproved': False,
     'StatusProduksi': 'Scheduled', 'JumlahTarget': 2000,
     'KomponenDibutuhkan': ['CPST0001', 'CPST0002', 'CPST0003', 'CPST0004', 'CPST0005'],
     'QtyProduksiBerjalan': 0, 'SisaTarget': 2000},
    {'CodeModel': 'RE111', 'KategoriModel': 'Remote', 'NamaKonsumen': 'Honda', 
     'TanggalMulaiProduksi': '', 'TanggalSelesaiProduksi': '', 'StatusApproved': False,
     'StatusProduksi': 'Scheduled', 'JumlahTarget': 1500,
     'KomponenDibutuhkan': ['CPST0002', 'CPST0003', 'CPST0005'],
      'QtyProduksiBerjalan': 0, 'SisaTarget': 1500},
    {'CodeModel': 'SPD222', 'KategoriModel': 'SPEDOMETER', 'NamaKonsumen': 'Toyota', 
     'TanggalMulaiProduksi': '', 'TanggalSelesaiProduksi': '', 'StatusApproved': False,
     'StatusProduksi': 'Scheduled', 'JumlahTarget': 1200,
     'KomponenDibutuhkan': ['CPST0001', 'CPST0002', 'CPST0003', 'CPST0004'],
      'QtyProduksiBerjalan': 0, 'SisaTarget': 1200},
    {'CodeModel': 'CAT13', 'KategoriModel': 'Camera', 'NamaKonsumen': 'Ricoh', 
     'TanggalMulaiProduksi': '', 'TanggalSelesaiProduksi': '', 'StatusApproved': False,
     'StatusProduksi': 'Scheduled', 'JumlahTarget': 1800,
     'KomponenDibutuhkan': ['CPST0001', 'CPST0002', 'CPST0003', 'CPST0004', 'CPST0005'],
      'QtyProduksiBerjalan': 0, 'SisaTarget': 1800},
    {'CodeModel': 'DRN01', 'KategoriModel': 'Drone', 'NamaKonsumen': 'Toyota', 
     'TanggalMulaiProduksi': '', 'TanggalSelesaiProduksi': '', 'StatusApproved': False,
     'StatusProduksi': 'Scheduled', 'JumlahTarget': 200,
     'KomponenDibutuhkan': ['CPST0001', 'CPST0002', 'CPST0003', 'CPST0004', 'CPST0005'],
      'QtyProduksiBerjalan': 0, 'SisaTarget': 200},
]

kode_akses = {
    "produksi": "PRD123",
    "warehouse": "WH123"
}

permintaanProduksi = []

riwayatStokKeluar = []

def cek_akses(divisi):
    kode = input(f"Masukkan kode akses Divisi {divisi.capitalize()}: ")

    if divisi in kode_akses and kode == kode_akses[divisi]:
        print("Akses diterima.\n")
        return True
    else:
        print("Kode akses salah!\n")
        return False

# ___MENU UTAMA__#
def menu_utama():
    while True:
        print("\nProduction & Inventory Control System PT ZENIX LTD")

        menu = [
            ["1", "Divisi Produksi"],
            ["2", "Divisi Warehouse"],
            ["3", "Keluar"]
        ]

        print(tabulate(
            menu,
            headers=["No", "Menu"],
            tablefmt="grid"
        ))

        pilihan = input("Pilih menu [1-3]: ")

        if pilihan == "1":
            if cek_akses("produksi"):
                menu_produksi()

        elif pilihan == "2":
            if cek_akses("warehouse"):
                menu_warehouse()

        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!\n")

    ## DIV Produksi

##==Menu DIVISI PRODUKSI==##
def menu_produksi():
    while True:
        print("\n-----------------------------------------------")
        print("        MENU DIVISI PRODUKSI - PT ZENIX LTD")
        print("-----------------------------------------------")
        print("1. Schedule Production")
        print("2. Kebutuhan Komponen Produksi")
        print("3. Exit")
        print("-----------------------------------------------")

        menu = input("Pilih menu [1-3]: ")

        if menu == "1":
            menu_schedule_produksi()
        elif menu == "2":
            menu_kebutuhan_komponen()
        elif menu == "3":
            break
        else:
            print("Pilihan tidak valid!\n")

# 1. SCHEDULE PRODUKSI
def menu_schedule_produksi():
    while True:
        print("\n=== MENU SCHEDULE PRODUKSI ===")
        print("1. Lihat Schedule Produksi")
        print("2. Mulai Produksi")
        print("3. Selesaikan Produksi")
        print("4. Kembali ke Menu Produksi")

        sub = input("Masukkan pilihan [1-4]: ")

        if sub == "1":
            lihat_schedule()
        elif sub == "2":
            mulai_produksi()
        elif sub == "3":
            selesaikan_produksi()
        elif sub == "4":
            break
        else:
            print("Pilihan tidak valid!\n")

                    # Lihat Schedule produksi

## Sub Menu SCHEDULE PRODUKSI
def lihat_schedule():
    print("\n=== DAFTAR SCHEDULE PRODUKSI ===")

    tabel = []

    for model in listModelProduksi:
        tabel.append([
            model['CodeModel'],
            model['KategoriModel'],
            model['NamaKonsumen'],
            model['StatusProduksi'],
            model['JumlahTarget'],
            model['QtyProduksiBerjalan'],
            model['TanggalMulaiProduksi'] if model['TanggalMulaiProduksi'] else "-",
            model['TanggalSelesaiProduksi'] if model['TanggalSelesaiProduksi'] else "-"
        ])

    header = [
        "Code",
        "Kategori",
        "Konsumen",
        "Status",
        "Target",
        "Produksi",
        "Mulai",
        "Selesai"
    ]

    print(tabulate(tabel, headers=header, tablefmt="fancy_grid"))

                    # Mulai Produksi
def mulai_produksi():
    code = input("Masukkan CodeModel yang ingin dimulai: ").upper()

    for model in listModelProduksi:
        if model['CodeModel'].upper() == code:

            if model['StatusProduksi'] == "Completed":
                print("Produksi sudah selesai.\n")
                return

            if model['JumlahTarget'] <= 0:
                print("Target produksi sudah terpenuhi.\n")
                model['StatusProduksi'] = "Completed"
                return

            print(f"\nJumlah Target Tersisa : {model['JumlahTarget']}")

            while True:
                qty = input("Masukkan jumlah produksi yang akan dijalankan: ")

                if not qty.isdigit():
                    print("Jumlah harus angka!")
                    continue

                qty = int(qty)

                if qty <= 0:
                    print("Jumlah harus lebih dari 0!")
                elif qty > model['JumlahTarget']:
                    print("Jumlah melebihi target!")
                else:
                    break

            model['JumlahTarget'] -= qty
            model['QtyProduksiBerjalan'] += qty
            model['StatusProduksi'] = "In Progress"
            model['TanggalMulaiProduksi'] = datetime.now().strftime("%Y-%m-%d")

            print("\nProduksi berhasil dimulai!")
            print(f"Qty Produksi : {qty}")
            print(f"Sisa Target  : {model['JumlahTarget']}\n")
            return

    print("CodeModel tidak ditemukan!\n")

                    # Selesaikan Produksi
def selesaikan_produksi():
    code = input("Masukkan CodeModel yang ingin diselesaikan: ").upper()

    for model in listModelProduksi:
        if model['CodeModel'].upper() == code:

            if model['StatusProduksi'] != "In Progress":
                print("Produksi belum berjalan atau sudah selesai.\n")
                return
            
            if model['StatusApproved'] == False:
                print("Produksi belum bisa diselesaikan!")
                print("Komponen belum di-approve oleh Warehouse.\n")
                return

            if model['JumlahTarget'] > 0:
                print(f"Produksi belum selesai, sisa target {model['JumlahTarget']} unit.\n")
                return

            model['StatusProduksi'] = "Completed"
            model['TanggalSelesaiProduksi'] = datetime.now().strftime("%Y-%m-%d")

            print("Produksi berhasil diselesaikan!\n")
            return

    print("CodeModel tidak ditemukan!\n")

# 2. KEBUTUHAN KOMPONEN            
def menu_kebutuhan_komponen():
    while True:
        print("\n=== MENU KEBUTUHAN KOMPONEN PRODUKSI ===")
        print("1. Lihat Kebutuhan Komponen per Model")
        print("2. Cek Stok Warehouse")
        print("3. Ajukan Permintaan Komponen")
        print("4. Kembali ke Menu Produksi")

        pilihKebutuhan = input("Masukkan pilihan [1-4]: ")

        if pilihKebutuhan == "1":
            lihat_kebutuhan_komponen()

        elif pilihKebutuhan == "2":
            cek_stok_warehouse()

        elif pilihKebutuhan == "3":
            ajukan_permintaan_komponen()

        elif pilihKebutuhan == "4":
            print("Kembali ke Menu Produksi...\n")
            break

        else:
            print("Pilihan tidak valid.\n")

                    # 1. Lihat Kebutuhan Komponen

## Sub Menu KEBUTUHAN KOMPONEN
def lihat_kebutuhan_komponen():
    code = input("Masukkan CodeModel: ").upper()
    ditemukan = False

    for model in listModelProduksi:
        if model['CodeModel'].upper() == code:
            ditemukan = True
            print("\n=== KEBUTUHAN KOMPONEN ===")
            print(f"Model    : {model['CodeModel']}")
            print(f"Konsumen : {model['NamaKonsumen']}")
            print("Komponen :")
            for komp in model['KomponenDibutuhkan']:
                print(f"- {komp}")
            print("-" * 40)
            break

    if not ditemukan:
        print("CodeModel tidak ditemukan!\n")

                    # 2. Cek Stok Warehouse
def cek_stok_warehouse():
    print("\n*** DAFTAR SEMUA KOMPONEN ***")

    tabel = []
    i = 1

    for komp in listKomponen:
        total_stok = 0
        for lot in komp['StokMasuk']:
            total_stok += lot['Qty']

        tabel.append([
            i,
            komp['PartCode'],
            komp['NamaKomponen'],
            komp['Kategori'],
            total_stok,
            komp['Suplier']
        ])
        i += 1

    header = ["Index", "PartCode", "Nama Komponen", "Kategori", "Stok", "Supplier"]

    print(tabulate(tabel, headers=header, tablefmt="fancy_grid"))

                    # 3. Ajukan Permintaan Komponen
def ajukan_permintaan_komponen():
    code = input("Masukkan CodeModel: ").upper()

    # CEK DUPLIKASI REQUEST
    for req in permintaanProduksi:
        if req['CodeModel'] == code and req['Status'] == "Pending":
            print("Permintaan untuk model ini sudah ada (Status: Pending).\n")
            return

    # CEK MODEL
    for model in listModelProduksi:
        if model['CodeModel'].upper() == code:

            if model['StatusProduksi'] != "In Progress":
                print("Produksi belum berjalan. Tidak bisa request komponen.\n")
                return

            daftarKomponen = []
            print("\nMasukkan jumlah kebutuhan komponen:")

            for komp in model['KomponenDibutuhkan']:
                while True:
                    qty_input = input(f"{komp} : ")
                    if qty_input.isdigit() and int(qty_input) > 0:
                        daftarKomponen.append({
                            'PartCode': komp,
                            'Qty': int(qty_input)
                        })
                        break
                    else:
                        print("Jumlah harus angka")

            permintaanProduksi.append({
                'CodeModel': code,
                'TanggalRequest': datetime.now().strftime("%Y-%m-%d"),
                'Komponen': daftarKomponen,
                'Status': 'Pending'
            })

            print("\nPermintaan komponen berhasil dikirim ke Warehouse!\n")
            return

    print("CodeModel tidak ditemukan!\n")

##==Menu DIVISI WAREHOUSE==##
def menu_warehouse():
    while True:
        print("\n-----------------------------------------------")
        print("        MENU DIVISI WAREHOUSE - PT ZENIX LTD")
        print("-----------------------------------------------")
        print("1. Stok Komponen")
        print("2. Tambah Komponen")
        print("3. Hapus Komponen")
        print("4. Update Stok")
        print("5. Permintaan Komponen dari Produksi")
        print("6. Keluar")
        print("-----------------------------------------------")

        menuWarehouse = input("Pilih menu [1-7]: ")

        if menuWarehouse == "1":
            menu_stok_komponen()

        elif menuWarehouse == "2":
            menu_tambah_komponen()

        elif menuWarehouse == "3":
            menu_hapus_komponen()

        elif menuWarehouse == "4":
            menu_update_stok()

        # elif menuWarehouse == "5":
        #     menu_fifo()

        elif menuWarehouse == "5":
            menu_permintaan_produksi()

        elif menuWarehouse == "6":
            print("Kembali ke menu utama...\n")
            break

        else:
            print("Menu belum tersedia atau tidak valid.\n")

            ###STOK KOmponen

# 1. STOK KOMPONEN
def menu_stok_komponen():
    while True:
        print("\n=== MENU STOK KOMPONEN ===")
        print("1. Lihat semua komponen")
        print("2. Lihat komponen berdasarkan PartCode")
        print("3. Kembali ke menu Warehouse")

        subMenu = input("Masukkan pilihan: ")

        if subMenu == "1":
            lihat_semua_komponen()

        elif subMenu == "2":
            detail_komponen()

        elif subMenu == "3":
            print("Kembali ke menu Warehouse...\n")
            break

        else:
            print("Pilihan tidak valid, coba lagi.\n")

##Sub Menu STOK KOMPONEN
def lihat_semua_komponen():
    print("\n*** DAFTAR SEMUA KOMPONEN ***")

    tabel = []
    i = 1

    for komp in listKomponen:
        total_stok = 0
        for lot in komp['StokMasuk']:
            total_stok += lot['Qty']

        harga = komp['HargaSatuan']
        total_cost = total_stok * harga

        tabel.append([
            i,
            komp['PartCode'],
            komp['NamaKomponen'],
            komp['Kategori'],
            total_stok,
            harga,
            total_cost
        ])

        i += 1

    header = [
        "Nomor",
        "PartCode",
        "Nama Komponen",
        "Kategori",
        "Stok",
        "Harga",
        "Total Cost"
    ]

    print(tabulate(tabel, headers=header, tablefmt="fancy_grid"))
def detail_komponen():
    partcode = input("Masukkan PartCode: ").upper()

    for komp in listKomponen:
        if komp['PartCode'].upper() == partcode:

            print("\n=== FIFO STOK KOMPONEN ===")
            print(f"PartCode      : {komp['PartCode']}")
            print(f"Nama Komponen : {komp['NamaKomponen']}")
            print(f"Kategori      : {komp['Kategori']}")
            print("-" * 70)

            print(f"{'No':<5} {'Tanggal Masuk':<15} {'Qty Masuk':<10} "
                  f"{'Tanggal Keluar':<15} {'Qty Keluar':<10} {'Sisa'}")
            print("-" * 70)

            total_stok = 0
            no = 1

            for lot in komp['StokMasuk']:

                # 🔐 pastikan Keluar ada
                if 'Keluar' not in lot:
                    lot['Keluar'] = []

                qty_masuk = lot['Qty'] + sum(k['Qty'] for k in lot['Keluar'])
                qty_keluar = sum(k['Qty'] for k in lot['Keluar'])
                tanggal_keluar = lot['Keluar'][0]['TanggalKeluar'] if lot['Keluar'] else "-"

                sisa = lot['Qty']
                total_stok += sisa

                print(f"{no:<5} {lot['TanggalMasuk']:<15} {qty_masuk:<10} "
                      f"{tanggal_keluar:<15} {qty_keluar:<10} {sisa}")

                no += 1

            print("-" * 70)
            print(f"TOTAL STOK : {total_stok} pcs")
            print("-" * 70)
            return

    print("PartCode tidak ditemukan!\n")

            ### Tambah Komponen

# 2. TAMBAH KOMPONEN
def menu_tambah_komponen():
    while True:
        print("\n=== MENU TAMBAH KOMPONEN ===")
        print("1. Tambah Komponen Baru")
        print("2. Kembali ke Menu Warehouse")

        subMenuTambah = input("Masukkan pilihan: ")

        if subMenuTambah == "1":
            tambah_komponen_baru()

        elif subMenuTambah == "2":
            print("Kembali ke menu Warehouse...\n")
            break

        else:
            print("Pilihan tidak valid, coba lagi.\n")

##Sub Menu TAMBAH KOMPONEN
def tambah_komponen_baru():
    while True:
        part_code = input("Masukkan PartCode Komponen (8 karakter): ").upper()
        if len(part_code) == 8:
            break
        print("PartCode harus tepat 8 karakter!\n")

    for i in listKomponen:
        if i['PartCode'] == part_code:
            print("PartCode sudah terdaftar! Gunakan menu Update Stok.\n")
            return

    nama_komp = input("Masukkan Nama Komponen: ")
    kat_komp = input("Masukkan Kategori Komponen: ")
    nama_supp = input("Masukkan Nama Supplier: ")
    harga_pcs = int(input("Masukkan Harga Satuan Komponen: "))

    while True:
        qty_input = input("Masukkan Jumlah Stok Awal: ")
        if qty_input.isdigit() and int(qty_input) > 0:
            qty_awal = int(qty_input)
            break
        print("Jumlah stok harus angka dan > 0!")

    tanggal_masuk = datetime.now().strftime("%Y-%m-%d")

    print("\n=== KONFIRMASI TAMBAH KOMPONEN ===")
    print(f"PartCode      : {part_code}")
    print(f"Nama Komponen : {nama_komp}")
    print(f"Kategori      : {kat_komp}")
    print(f"Supplier      : {nama_supp}")
    print(f"Harga Satuan  : {harga_pcs}")
    print(f"Stok Awal     : {qty_awal}")
    print(f"Tanggal Masuk : {tanggal_masuk}")

    konfirmasi = input("Simpan komponen baru? (Y/N): ").upper()

    if konfirmasi == "Y":
        listKomponen.append({
            'PartCode': part_code,
            'NamaKomponen': nama_komp,
            'Kategori': kat_komp,
            'Suplier': nama_supp,
            'HargaSatuan': harga_pcs,
            'StokMasuk': [{'TanggalMasuk': tanggal_masuk, 'Qty': qty_awal}]
        })
        print("\nKomponen baru berhasil ditambahkan!\n")
    else:
        print("\nPenambahan komponen dibatalkan.\n")

# 3. HAPUS KOMPONEN
def menu_hapus_komponen():

    if len(listKomponen) == 0:
        print("Tidak ada komponen untuk dihapus.\n")
        return

    lihat_semua_komponen()

    partcode = input("\nMasukkan PartCode komponen yang ingin dihapus: ").upper()
    ditemukan = False

    for i in range(len(listKomponen)):
        komp = listKomponen[i]

        if komp['PartCode'].upper() == partcode:
            ditemukan = True

            print("\n=== KONFIRMASI HAPUS KOMPONEN ===")
            print(f"PartCode      : {komp['PartCode']}")
            print(f"Nama Komponen : {komp['NamaKomponen']}")
            print(f"Kategori      : {komp['Kategori']}")
            print(f"Supplier      : {komp['Suplier']}")

            konfirmasi = input("\nApakah yakin ingin menghapus komponen ini? (Y/N): ").upper()

            if konfirmasi == "Y":
                del listKomponen[i]
                print("\nKomponen berhasil dihapus!\n")
            else:
                print("\nPenghapusan dibatalkan.\n")

            break

    if not ditemukan:
        print(f"Komponen dengan PartCode '{partcode}' tidak ditemukan!\n")

# 4. UPDATE STOK KOMPONEN
def menu_update_stok():
    while True:
        print("\n=== MENU UPDATE STOK ===")
        print("1. Update Stok Komponen")
        print("2. Kembali ke Menu Warehouse")

        pilihUpdate = input("Masukkan pilihan: ")

        if pilihUpdate == "1":
            update_stok_komponen()

        elif pilihUpdate == "2":
            print("Kembali ke menu Warehouse...\n")
            break

        else:
            print("Pilihan tidak valid.\n")

## Sub Menu UPDATE STOK KOMPONEN
def update_stok_komponen():
    lihat_semua_komponen()
    partcode = input("Masukkan PartCode: ").upper()
    ditemukan = False

    for komp in listKomponen:
        if komp['PartCode'].upper() == partcode:
            ditemukan = True
            
            while True:
                jumlah_input = input("Masukkan jumlah stok masuk: ")
                if not jumlah_input.isdigit():
                    print("Jumlah harus berupa angka!")
                    continue

                jumlah_masuk = int(jumlah_input)

                if jumlah_masuk <= 0:
                    print("Jumlah harus lebih dari 0!")
                    continue

                break

            tanggal_masuk = datetime.now().strftime('%Y-%m-%d')
            stok_sebelum = sum(lot['Qty'] for lot in komp['StokMasuk'])
            stok_setelah = stok_sebelum + jumlah_masuk

            print("\n=== KONFIRMASI UPDATE STOK ===")
            print(f"PartCode      : {komp['PartCode']}")
            print(f"Nama Komponen : {komp['NamaKomponen']}")
            print(f"Stok Sebelum  : {stok_sebelum}")
            print(f"Jumlah Masuk  : {jumlah_masuk}")
            print(f"Stok Setelah : {stok_setelah}")
            print(f"Tanggal Masuk: {tanggal_masuk}")

            konfirmasi = input("Simpan update stok? (Y/N): ").upper()

            if konfirmasi == "Y":
                komp['StokMasuk'].append({
                    'TanggalMasuk': tanggal_masuk,
                    'Qty': jumlah_masuk
                })
                print("\nStok berhasil ditambahkan!\n")
            else:
                print("\nUpdate stok dibatalkan.\n")

            return

    if not ditemukan:
        print(f"PartCode '{partcode}' tidak ditemukan!\n")

# 5. PERMINTAAN PRODUKSI
def menu_permintaan_produksi():
    while True:
        print("\n=== PERMINTAAN KOMPONEN DARI PRODUKSI ===")
        print("1. Lihat Daftar Permintaan")
        print("2. Approve & Keluarkan Stok (FIFO)")
        print("3. Riwayat Stok Keluar")
        print("4. Kembali ke Menu Warehouse")

        pilihRequest = input("Masukkan pilihan [1-4]: ")

        if pilihRequest == "1":
            lihat_daftar_permintaan()

        elif pilihRequest == "2":
            approve_permintaan_fifo()

        elif pilihRequest == "3":
            riwayat_stok_keluar_produksi()

        elif pilihRequest == "4":
            print("Kembali ke Menu Warehouse...\n")
            break

        else:
            print("Pilihan tidak valid.\n")              

##Sub Menu PERMINTAAN PRODUKSI
def lihat_daftar_permintaan():
    if len(permintaanProduksi) == 0:
        print("Belum ada permintaan dari produksi.\n")
        return

    print("\n=== DAFTAR PERMINTAAN ===")
    print(f"{'Index':<6} {'Model':<10} {'Tanggal':<15} {'Status':<10}")
    print("-" * 50)

    index = 0
    for req in permintaanProduksi:
        print(
            f"{index:<6} "
            f"{req['CodeModel']:<10} "
            f"{req['TanggalRequest']:<15} "
            f"{req['Status']:<10}"
        )
        index += 1

    print("-" * 50)

                    # Approve & FIFO
def approve_permintaan_fifo():
    if len(permintaanProduksi) == 0:
        print("Tidak ada permintaan untuk diproses.\n")
        return

    index_req = input("Masukkan index permintaan: ")

    if not index_req.isdigit():
        print("Index harus berupa angka!\n")
        return

    index_req = int(index_req)

    if index_req < 0 or index_req >= len(permintaanProduksi):
        print("Index tidak valid!\n")
        return

    req = permintaanProduksi[index_req]

    if req['Status'] != "Pending":
        print("Permintaan ini sudah diproses.\n")
        return

    # VALIDASI STOK
    for komp_req in req['Komponen']:
        partcode = komp_req['PartCode']
        qty_needed = komp_req['Qty']
        ditemukan = False

        for item in listKomponen:
            if item['PartCode'] == partcode:
                ditemukan = True
                stok_tersedia = sum(lot['Qty'] for lot in item['StokMasuk'])

                if stok_tersedia < qty_needed:
                    print(f"Stok {partcode} tidak mencukupi!")
                    print("Permintaan dibatalkan.\n")
                    return
                break

        if not ditemukan:
            print(f"PartCode {partcode} tidak ditemukan di warehouse.\n")
            return

    # FIFO Proses + Histori LOT
    tanggal_keluar = datetime.now().strftime("%Y-%m-%d")

    for komp_req in req['Komponen']:
        partcode = komp_req['PartCode']
        qty_keluar = komp_req['Qty']

        for item in listKomponen:
            if item['PartCode'] == partcode:
                sisa = qty_keluar

                for lot in item['StokMasuk']:
                    if sisa <= 0:
                        break

                    if lot['Qty'] <= 0:
                        continue  # skip lot kosong

                    # pastikan histori keluar ada
                    if 'Keluar' not in lot:
                        lot['Keluar'] = []

                    if lot['Qty'] <= sisa:
                        qty_diambil = lot['Qty']
                        lot['Qty'] = 0
                        sisa -= qty_diambil
                    else:
                        qty_diambil = sisa
                        lot['Qty'] -= sisa
                        sisa = 0

                    # catat histori keluar PER LOT
                    lot['Keluar'].append({
                        'TanggalKeluar': tanggal_keluar,
                        'Qty': qty_diambil,
                        'CodeModel': req['CodeModel'],
                        'Alasan': 'Produksi'
                    })

                break

    req['Status'] = "Approved"

    for model in listModelProduksi:
        if model['CodeModel'] == req['CodeModel']:
            model['StatusApproved'] = True
            break

    print("Permintaan berhasil diproses & stok dikeluarkan.\n")
def riwayat_stok_keluar_produksi():
    print("\n=== RIWAYAT STOK KELUAR ===")

    data_ditemukan = False
    no = 1

    print(f"{'No':<4} {'Tanggal':<12} {'PartCode':<10} {'Qty':<6} {'Model':<10} {'Alasan':<10}")
    print("-" * 70)

    for item in listKomponen:
        partcode = item['PartCode']

        for lot in item['StokMasuk']:
            if 'Keluar' not in lot:
                continue

            for keluar in lot['Keluar']:
                data_ditemukan = True

                print(
                    f"{no:<4} "
                    f"{keluar['TanggalKeluar']:<12} "
                    f"{partcode:<10} "
                    f"{keluar['Qty']:<6} "
                    f"{keluar.get('CodeModel','-'):<10} "
                    f"{keluar.get('Alasan','-'):<10}"
                )
                no += 1

    if not data_ditemukan:
        print("Belum ada stok keluar.\n")
        return

    print("-" * 70)

menu_utama()