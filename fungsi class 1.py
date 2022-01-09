# -*- coding: utf-8 -*-
"""

@materi : algoritma dan pemograman
@judul : fungsi class
@hari/tanggal : Senin/06/12/2021
@nim : 065002100023
@author : Tri Bintang Pamungkas 
"""

class mahasiswa:

   def __init__(self,nama,angkatan,nim):

        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan

   def biodata_mahasiswa(self):
       print("\nnama kamu adalah : ",self.nama)
       print("nim kamu adalah : ",self.nim)
       print("angkatan kamu adalah : ",self.angkatan)

nama = str(input("masukan nama mu : "))
nim = int(input("masukan nim kamu : "))
angkatan = int(input("masukan angkatan kamu: "))

biodata = mahasiswa(nama,angkatan,nim)
biodata.biodata_mahasiswa()
