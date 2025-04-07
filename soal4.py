def cek_duplikat(data):
    data_set = set(data)
    #set menyimpan nilai unik, 
    #maksudnya menyimpan nilai duplikat
    
    if len(data) != len(data_set):
        return True 
    else:
        return False  

#program utama
data_angka = list(map(int, input().split(", ")))

result = cek_duplikat(data_angka)

print(result)
