while True: 
    
    print("""
      ---KC FotoCopy---
      <=================>
      ->SEdia:
       1. Print
       2. FotoCopy
       0. Exit
      """)
    
    a = int(input("\nPilih Nomor Berapa? : "))
    
    if a == 1:
        nanyaPrint = int(input("Print Berapa Lembar ? : "))
        warna = input("Mau Print Berwarna? \n-> mau\n-> tidak\n: ")
        if warna == "mau":
            warnaPrint = 2_500 #Harga Print Berwarna/Lembar
            hargaPrintWarna = nanyaPrint * warnaPrint
            print(f"\nHarga Print Sebanyak {nanyaPrint} Lembar Sebesar : RP. {hargaPrintWarna},00")
        elif warna == "tidak":       
            hpPrint = 1_500 #Harga Print/Lembar
            hargaHpPrint = nanyaPrint * hpPrint
            print(f"\nHarga Print Sebanyak {nanyaPrint} Lembar Sebesar : RP. {hargaHpPrint},00")
            
    elif a == 2:
        nanyaFC = int(input("Mau FotoCopy Berapa Lembar? : "))
        hpFC = 1_000 #Harga FotoCopy/Lembar 
        hargaHpFC = nanyaFC * hpFC
        print(f"\nHarga FotoCopy Sebanyak {nanyaFC} Lembar Sebesar : RP. {hargaHpFC},00")
    elif a == 0:
        print("\nExit\nTerima Kasih Telah Berkunjunng Di KC FotoCopy")
        break    
    else:
        print("\nMaaf, Pilihan Tidak Tersedia\nTerima Kasih Telah Berkunjung Di KC FotoCopy")
        break
    
    z = input("Mau Lagi (y/n)? ")
    if z == "n":
        print("\nProgram Selesai\nTerima Kasih Telah berkunjug Di KC FotoCopy")
        break