class Data:
    count = 0
    
    #constructor
    def __init__(self, nama: str, usia: int, no_hp: str, alamat: str):
        #public attribute
        self.nama = nama
        
        #protected attribute
        self.usia = usia
        
        # private attribute
        self.__no_hp = no_hp
        self.__alamat = alamat
        
        #setiap  objek Data dibuat maka nilai count akan bertambah
        self.id = Data.count
        Data.count += 1
        
    # untuk mengakses dan mengubah nilai atribut private
    def get_no_hp(self):
        return self.__no_hp

    def set_no_hp(self, no_hp: str):
        self.__no_hp = no_hp

    def get_alamat(self):
        return self.__alamat

    def set_alamat(self, alamat: str):
        self.__alamat = alamat
    
    # untuk mengakses atribut protected
    @property #decorator
    def usia(self):
        return self._usia
        
     # untuk mengubah atribut protected
    @usia.setter #decorator
    def usia(self, usia: int):
        self._usia = usia

class Karyawan(Data):
    #constructor
    def __init__(self, nama: str, usia: int, no_hp: str, alamat: str, no_id: str):
        # memanggil constructor parent class
        super().__init__(nama, usia, no_hp, alamat)

        # public attribute
        self.no_id = no_id

    @property
    def no_hp(self):
        return self.get_no_hp()

    @no_hp.setter
    def no_hp(self, no_hp: str):
        self.set_no_hp(no_hp)


def main():
    # Buat objek Data dan karyawan
    Data = Data("Qai", 20, "08123456890", "Belwis")
    karyawan = karyawan("Qai", 20, "08123456890", "Belwis", "1234")

    # print seluruh atribut Data
    print("dictionary atribut Data")
    for key, value in Data.__dict__.items():
        print('%-20s %s' % (key, value))

    # newline
    print()

    # print seluruh atribut karyawan
    print("dictionary atribut karyawan")
    for key, value in karyawan.__dict__.items():
        print('%-20s %s' % (key, value))

    # newline
    print()

    # percobaan mengakses atribut public
    print("Akses atribut public")
    print("Data nama: %s" % Data.nama)
    print("karyawan nama: %s" % karyawan.nama)

    '''
    Attribut nama adalah atribut public, sehingga dapat diakses dari luar kelas.
    Attribut public juga akan diturunkan ke subclass dari kelas tersebut.
    '''

    # newline
    print()

    # percobaan mengakses atribut protected
    print("Akses atribut protected")
    print("Umur: %d" % Data._usia)
    print("Umur: %d" % karyawan._usia)
    
    
    '''
    Attribut _usia adalah atribut protected, atribut protected adalah atribut yang hanya dapat diakses dari kelas tersebut dan kelas turunannya.
    Pemberian nama variable yang diawali dengan underscore _ adalah konvensi yang digunakan untuk menandakan bahwa variable tersebut adalah atribut protected. Akan tetapi, Python tidak akan membatasi akses ke atribut protected. hal ini dikarenakan Python didesain sebagai bahasa pemrograman yang mudah digunakan dan tidak terlalu ketat, beberapa orang menyebut access modifier atau information hiding sebagai hal yang unpythonic.

    As is true for modules, classes in Python do not put an absolute barrier between definition and user, but rather rely on the politeness of the user not to "break into the definition".
    — 9. Classes, The Python 2.6 Tutorial (2013)

    Python bergantung pada kebijaksanaan pengguna untuk tidak "mengganggu" definisi kelas, hal ini terlihat pada salah satu slogan pada Python yaitu "we're all responsible users here". jadi konsep access modifier atau information hiding ditetapkan dengan konvensi saja.
    '''

    # newline
    print()

    # percobaan mengakses atribut protected dengan decorator
    print("Akses atribut protected dengan decorator")
    print("Umur: %d" % data.usia)
    print("Umur: %d" % karyawan.usia)

    '''
    Di python juga terdapat decorator untuk mengakses atribut protected, decorator ini akan memanggil fungsi aksester yang telah dibuat pada kelas data. jadi atribut yang dibatasi aksesnya hanya dapat diakses melalui decorator.
    '''

    # newline
    print()

    # percobaan mengubah atribut private
    print("Akses atribut private")
    try:
        print("Nomor telepon: %s" % data.__no_hp)
    except AttributeError as e:
        print(e)

    try:
        print("Nomor telepon: %s" % karyawan.__no_hp)
    except AttributeError as e:
        print(e)

    '''
    Untuk mengakses atribut private, kita harus menggunakan fungsi aksester dan setter yang telah dibuat pada kelas data. Atribut private tidak dapat diakses dari luar kelas. Attribut private pada python ditandai dengan dua underscore (__) di depan nama variable.
    Sama halnya dengan atribut protected, Python sebenarnya tidak akan membatasi akses ke atribut private, akan tetapi sedikit berbeda dengan atribut protected, Python menerapkan konsep nama mangling untuk atribut private. Atribut private akan ditambahkan dengan nama kelasnya, sehingga atribut private pada kelas data akan menjadi _data__no_hp, seperti yang terlihat pada output dictionary key pada tiap instance. Hal ini dilakukan untuk menghindari konflik nama variable antar kelas.
    '''

    # newline
    print()

    # percobaan mengakses atribut private dengan aksester
    print("Akses atribut private dengan aksester")
    print("Nomor telepon: %s" % data.get_no_hp())
    print("Nomor telepon: %s" % karyawan.get_no_hp())

    # newline
    print()

    # percobaan mengaksess atribut private dengan nama mangling
    print("Akses atribut private dengan nama mangling")
    print("Nomor telepon: %s" % data._data__no_hp)
    print("Nomor telepon: %s" % karyawan._data__no_hp)

    '''
    Untuk melampaui batasan nama mangling, kita dapat mengakses atribut private dengan cara mengubah nama variable yang diawali dengan dua underscore (__) menjadi satu underscore (_) dan nama kelasnya, seperti yang terlihat pada percobaan mengakses atribut private pada objek data dan karyawan.
    Namun hal ini sangat tidak disarankan.
    Note pada subclass karyawan, nama mangling pada atribut private __no_hp tetap menjadi _data__no_hp karena atribut private pada kelas parent class tidak akan berubah.
    '''


if __name__ == "__main__":
    main()
        
