nama = 'Tika Ayu A'
program = 'Gerak Lurus'

print(f'Program {program} oleh {nama}')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'Jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'Sehingga kecepatan = {kecepatan} m/s')
    return jarak / waktu

# jarak = 1000
# waktu = 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)

def hitung_daya(usaha, waktu):
    daya = usaha / waktu
    print(f'Usaha = {usaha}J dibutuhkan dalam waktu = {waktu / 60}menit')
    print(f'Sehingga daya = {daya} J/s')
    return usaha / waktu

# usaha = 18000
# waktu = 3 * 60
daya = hitung_daya(18000, 3 * 60)
daya = hitung_daya(30000, 5 * 60)
