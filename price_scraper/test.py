import math

# Giesswein Vent Pantoffeln
links = []
links.append("https://www.amazon.de/-/en/GIESSWEIN-Unisex-Vent-Slippers-Chili/dp/B003DSHOVO/ref=sr_1_5?crid=20F3ONHOV98B0&keywords=giesswein%2Bentl%C3%BCftung&qid=1669162297&sprefix=gie%C3%9Fwein%2Bvent%2Caps%2C127&sr=8-5&th=1&psc=1")
links.append("https://www.amazon.de/-/en/GIESSWEIN-Unisex-Vent-Slippers-Chili/dp/B002BH4QOG/ref=sr_1_5?crid=20F3ONHOV98B0&keywords=giesswein%2Bentl%C3%BCftung&qid=1669162297&sprefix=gie%C3%9Fwein%2Bvent%2Caps%2C127&sr=8-5&th=1&psc=1")
links.append("https://www.amazon.de/-/en/GIESSWEIN-Unisex-Vent-Slippers-Chili/dp/B003W3WOC4/ref=sr_1_5?crid=20F3ONHOV98B0&keywords=giesswein%2Bentl%C3%BCftung&qid=1669162297&sprefix=gie%C3%9Fwein%2Bvent%2Caps%2C127&sr=8-5&th=1&psc=1")
links.append("https://www.amazon.de/-/en/GIESSWEIN-Unisex-Vent-Slippers-Chili/dp/B003WZJYOS/ref=sr_1_5?crid=20F3ONHOV98B0&keywords=giesswein%2Bentl%C3%BCftung&qid=1669162297&sprefix=gie%C3%9Fwein%2Bvent%2Caps%2C127&sr=8-5&th=1&psc=1")
links.append("https://www.amazon.de/-/en/GIESSWEIN-Unisex-Vent-Slippers-Chili/dp/B003WA59RE/ref=sr_1_5?crid=20F3ONHOV98B0&keywords=giesswein%2Bentl%C3%BCftung&qid=1669162297&sprefix=gie%C3%9Fwein%2Bvent%2Caps%2C127&sr=8-5&th=1&psc=1")


def read_links()->list[tuple[str,str,float]]:
    l = []
    with open("links.csv",'r') as f:
        for line in f:
            l.append(line.split(','))
    return l

print(read_links())
print(len(read_links()[0]))


