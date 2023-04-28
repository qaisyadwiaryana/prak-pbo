from abc import ABC, abstractmethod

class AkunBank(ABC):
    def __init__(self, nama: str, tahun_daftar, saldo: float):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo

    def lihat_saldo(self):
        print('%s memiliki saldo Rp %d' % (self.nama, self.saldo))

    @abstractmethod
    def transfer_saldo(self, transfer):
        pass

    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def transfer_saldo(self, transfer):
        if(self.tahun_daftar >= 3 and transfer > 100000):
            fee_adm = 0
        elif(self.tahun_daftar < 3 and transfer > 100000):
            fee_adm = 2000
        elif(transfer <= 100000):
            fee_adm = 0
        print("Fee admin: Rp " + str(fee_adm))

    def lihat_suku_bunga(self):
        if(self.tahun_daftar >=3 and self.saldo >= 1000000000):
            bunga = 0.01
        elif(self.tahun_daftar < 3 and self.saldo >= 1000000000):
            bunga = 0.02
        elif(self.saldo < 1000000000):
            bunga = 0.03
        print("Bunga per bulan adalah : " + str(bunga))

class AkunSilver(AkunBank):
    def transfer_saldo(self, transfer):
        if(self.tahun_daftar >= 3 and transfer > 100000):
            fee_adm = 2000
        elif(self.tahun_daftar < 3 and transfer > 100000):
            fee_adm = 5000
        elif(transfer <= 100000):
            fee_adm = 0
        print("Fee admin: Rp " + str(fee_adm))

    def lihat_suku_bunga(self):
        if(self.tahun_daftar >=3 and self.saldo >= 10000000):
            bunga = 0.01
        elif(self.tahun_daftar < 3 and self.saldo >= 10000000):
            bunga = 0.02
        elif(self.saldo < 10000000):
            bunga = 0.03
        print("Bunga per bulan adalah : " + str(bunga))


p1 = AkunGold("Harry", 2019 , 10000000)
p1.lihat_saldo()
p1.lihat_suku_bunga()
p1.transfer_saldo(50000)
p1.lihat_saldo
