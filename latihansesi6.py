# membuat aplikasi
nama = input("\nMasukan nama mahasiswa : ")
nilai = input("input nilai akhir : ")

if (nilai.isnumeric() == True):
    nilai_int = int(nilai)
    if nilai_int >= 90:
        grade = "A"
        predikat = "Dengan pujian"

    elif nilai_int >= 80:
        grade = "B"
        predikat = "Sangat memuaskan"

    elif nilai_int >= 70:
        grade = "C"
        predikat = "Memuaskan"
    elif nilai_int >= 60:
        grade = "D"
        predikat = "Tidak memuaskan"
    elif nilai_int >= 0:
        grade = "E"
        predikat = "Tidak lulus"
    
    print ("\n-------------")
    print("Nama mahasiswa : ", nama)
    print("grade anda : ", grade)
    print("predikat anda : ", predikat)

else:
    print("\nMaaf input anda salah")

print("\n===================")


