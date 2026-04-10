score = 100
indeks = "E"

if (score >= 55 and score <65) :
    indeks = "D"
elif (score >= 65 and score <75) :
    indeks = "C"
elif (score >= 75 and score <85) :
    indeks = "B"
elif (score >= 85) :
    indeks = "A"

print(f"Indeks nilai anda adalah {indeks}")
