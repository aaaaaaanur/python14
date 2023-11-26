group = {
    "Иван": "m",
    "Виктор": "m",
    "Анна": "f",
    "Жанна": "f",
    "Семён": "m",
    "Ада": "f",
    "Алла": "f",
    "Михаил": "m"
}

m = []
f = []

def mf():
    for i in group:
        if group[i] == "m":
            m.append(i)
        else:
            f.append(i)
    return 


mf()
print(f)
print(m)