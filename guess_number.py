# Created By Prayitno
# Politeknik Negeri Semarang

def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3

    while guess < guess_limit:
        user = int(input("Masukkan angka > "))
        if user == secret_number:
            print("Selamat, anda berhasil menemukan angkanya")
            break
        else:
            guess += 1
    else:
        print(f"Ana tidak menemukan angkanya, angka rahasisanya adalah {secret_number}")