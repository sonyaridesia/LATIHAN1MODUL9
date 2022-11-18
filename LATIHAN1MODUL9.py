#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:59:22 2022

@author: sonyaridesia
"""

def masukkan_file():
    nama = str(input("\nMasukan Nama mu: "))
    umur = int(input("\nMasukan Umur mu: "))
    alamat = str(input("\nMasukan Alamat mu: "))
    email = str(input("\nMasukan Email mu: "))
    dosen = str(input("\nMasukan Dosen Wali mu: "))
    file= open("Biodata.txt", "w")
    file.write(f'Nama:{nama}\nUmur:{umur}\nAlamat:{alamat}\nEmail:{email}\nDosen:{dosen}')
    file.close()
a = masukkan_file()
print(a)

def output_file():
    file = open("Biodata.txt", "r")
    text = file.read()
    print()
    print("Berikut Ini Data Kamu")
    print(text)
    file.close()
b = output_file()
print(b)