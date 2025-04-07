import re
# untuk memanipulasi 

def palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    start = 0
    end = len(s) - 1
    
    while start < end:
    #while ini akan terus berjalan selama 
    #start kurang dari end, yaitu selama 
    #ada karakter yang tersisa untuk dibandingkan 
    #dari kedua ujung string.
        if s[start] != s[end]:  
            return False
        start += 1
        end -= 1
    
    return True 

#program utama
input_string = input()

if palindrome(input_string):
    print("eureeka!")
else:
    print("suka blyat")
