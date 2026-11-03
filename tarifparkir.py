def hitung_tarif_parkir(jenis_kendaraan, durasi_jam, status_inap)

    if jenis == "becak":
        return 1000

    elif jenis == "motor":
        if status_inap:
            return 15000

        tarif_masuk = 2000
        if durasi_jam <= 2:
            total_tarif = tarif_masuk
        else: 
            jam_progresif = durasi_jam - 2
            total_tarif = tarif_masuk + (jam_progresif * 1000)  
        # jika durasi lebih dari 2 jam maka ada tambahan tarif progresif Rp. 1.000 di jam berikutnya
        if total_tarif > 10000:
            total_tarif = 10000
            return total_tarif

    elif jenis == "mobil": 
        if status_inap:
            return 20000

        tarif_masuk = 4000
        if durasi_jam <= 2:
            total_tarif = tarif_masuk
        # jika durasi lebih dari 2 jam maka ada tambahan tarif progresif Rp. 2.000 di jam berikutnya
        else:
            jam_progresif = durasi_jam - 2 
            total_tarif = tarif_masuk + (jam_progresif * 2000)

        if total_tarif > 15000:
            total_tarif = 15000
        return total_tarif