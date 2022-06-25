# Program stack mahasiswa
# I.S : pengguna memilih menu
# F.S : program akan menampilkan hasil pilihan menu

MAKS_SISA = 20

sisa = []

# Function untuk memeriksa stack kosong
def Kosong(Top) :
    if (Top==0) :
        return True
    else :
        return False

# Function untuk memeriksa stack penuh
def Penuh(Top) :
    if (Top==MAKS_SISA) :
        return True
    else :
        return False

# Memasukan data ke stack mahasiswa
def Push(sisa_bagi) :
    Top = len(sisa)
    if (not Penuh(Top)) :
        sisa.append(sisa_bagi)
    else :
        print("Data mahasiswa sudah penuh!")

# Menampilkan data stack (Hasil pop)
def TampilDataPop(sisa) : 
    Top = len(sisa)
    if() :
        print()
    else :
        print("Data mahasiswa kosong!")

# Mengeluarkan isi stack
def Pop(Nim, Nama, Nilai, Indeks) :
    Top = len(Nim)
    if (not Kosong(Top)) :
        Nim.pop()
        Nama.pop()
        Nilai.pop()
        Indeks.pop()
    else :
        print("Data mahasiswa kosong!")

def Bagi(desimal) :
    while desimal > 1 :
        sisa_bagi = desimal % 2 
        div = desimal // 2
        print('sisa bagi : ',sisa_bagi)
        print('div : ',div)
        desimal = div
        # push



# I n p u t 
desimal = int(input("Masukkan Nilai Desimal : "))
Bagi(desimal)