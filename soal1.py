def review_stats(ratings):
    terendah = min(ratings)
    tertinggi = max(ratings)
    rataRata = sum(ratings) / len(ratings)
    
    return terendah, tertinggi, rataRata

#program utama

ratings = list(map(float, input().split(", ")))
terendah, tertinggi, rataRata = review_stats(ratings)
print(terendah, tertinggi, rataRata)