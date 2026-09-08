print ("KALKULATOR SEDERHANA")

angka1 = float(input('Masukkan angka pertama = '))
angka2 = float(input('Masukkan angka kedua = '))
operasi = input('Masukkan operasi (+, -, x, /)= ')
if operasi == '+':
    hasil = angka1 + angka2
    print(f'Hasilnya adalah {hasil}')
elif operasi == '-':
    hasil = angka1 - angka2
    print(f'Hasilnya adalah {hasil}')
elif operasi == 'x':
    hasil = angka1 * angka2
    print(f'Hasilnya adalah {hasil}')
elif operasi == '/':
    hasil = angka1 / angka2
    print(f'Hasilnya adalah {hasil}')
else:
    print('Masukkan operasi yang benar')