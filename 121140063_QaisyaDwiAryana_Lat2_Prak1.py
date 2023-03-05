# Qaisya Dwi Aryana 121140063 Siakad RB

Us = ("informatika")
Pw = ("12345678")

for i in range(3, 0, -1):
    User = input("Username = ")
    Pass = input("Password = ")
    if (User == Us and Pass == Pw):
        print("Berhasil Login!")
        break
    elif(i == 1):
        print("Akun di blokir")
    else:
        print("Username atau Password Salah Coba Lagi")