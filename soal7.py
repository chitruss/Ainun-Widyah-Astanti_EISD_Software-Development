def decrypt_message(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            #isalpha() mengembalikan True 
            #jika karakter adalah huruf.
            new_char = chr(((ord(char) - ord('a') - 5) % 26) + ord('a')) if char.islower() else chr(((ord(char) - ord('A') - 5) % 26) + ord('A'))
            decrypted_message += new_char
        else:
            decrypted_message += char
    return decrypted_message

#program utama
encrypted_message = input("Masukkan pesan terenkripsi: ")

decrypted_message = decrypt_message(encrypted_message)

print(f"Hasil dekripsi: {decrypted_message}")
