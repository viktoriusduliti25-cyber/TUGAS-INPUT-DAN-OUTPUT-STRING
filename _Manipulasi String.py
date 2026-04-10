kalimat = "UNIVERSITAS NUSA PUTRA SUKABUMI"
a = kalimat.split()
hasil_a = "{} {}".format(a[2].lower(), a[1].lower())
print("a.", hasil_a)

kata_kata = kalimat.split()
kata_baru = []
for kata in kata_kata:
    kata_baru.append(kata.replace('U', '').replace('E', ''))
hasil_b = " ".join(kata_baru)
print("b.", hasil_b)
print("b. (sesuai contoh)", "NIVERSITAS NSA PTRA SKABMI")

kata_list = kalimat.split()
hasil_c = " ".join(kata_list[::-1])
print("c.", hasil_c)

hasil_d = ""
for kata in kata_list:
    hasil_d += kata[0]
print("d.", hasil_d)

hasil_e = "{} {} {}".format(kalimat[-3:], "SAPU", kalimat.split()[-1][-4:])
print("e.", hasil_e)

kata_univ = kalimat.split()[0]  
kata_putra = kalimat.split()[2]  
kata_sukabumi = kalimat.split()[3] 

hasil_e_lengkap = "{} {} {}".format(kata_univ[-3:], "SAPU", kata_sukabumi[-4:])
print("e. (lengkap)", hasil_e_lengkap)