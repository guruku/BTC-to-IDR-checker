# BTC-to-IDR-checker
Tools to check the exchange rate virtual money currency to Indonesia Rupiah from Bitcoin.co.id API

Simple tools to check exchange rate BTC to IDR using Python
Biar nggak susah-susah cek di web, pake API bitcoin.co.id

btc_idr.py = hanya check Bitcoin ke IDR
bit_idr.py = cek Bitcoin, Bitcoin Cash, Bitcoin Gold ke IDR
==========================================================================================================================
==========================================================================================================================
Update dari tools sebelumnya dari beberapa request

tidak seperti sebelumnya yang auto new-line setelah mendapatkan respond,
kali ini di ubah menjadi dinamis, jadi hanya Rp. Nominal yang berubah-ubah dan new-line

ada 3 file :
  btc_idr_dinamic.py  -> dinamical single line Bitcoin only (hanya BTC) 
  btcid_idr.py        -> dinamical full dari bitcoin.co.id untuk ke IDR
  bitcoincoid_idr.py  -> dinamical full dari bitcoin.co.id untuk ke IDR
  
bitcoincoid_idr.py dan btcid_idr.py memiliki hasil yang sama, tapi memiliki algoritma pemrograman yang berbeda
btcid_idr lebih berat di jalankan daripada bitcoincoid_idr.py jadi lebih di sarankan menggunakan bitcoincoid_idr.py

isi :
    Bitcoin to Indonesia Rupiah         
    Bitcoin Cash to Indonesia Rupiah    
    Bitcoin Gold to Indonesia Rupiah    
    Ethereum to Indonesia Rupiah                                   
    Ethereum Classic to Indonesia Rupiah                       
    Litecoin to Indonesia Rupiah                                     
    NXT to Indonesia Rupiah                                         
    Waves to Indonesia Rupiah                                     
    Ripple to Indonesia Rupiah                                   
    Zcoin to Indonesia Rupiah           

Stellar Lumens(XLM) to IDR API is Invalid, jadi tidak bisa di masukkan
