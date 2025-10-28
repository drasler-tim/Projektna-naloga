import re
import csv

with open("avti.html", encoding="utf-8") as f:
    vsebina = f.read()

# Vzorec za celoten blok vozila
vzorec_avta = re.compile(
    r'<div class="item-data">(.*?)'
    r'<div class="hidden">',
    re.DOTALL
)

# Posamezni podatki
id_avta = re.compile(
    r'<a href="/car/(?P<id>\d+)',
  re.DOTALL
)

naslov_avta = re.compile(
    r'<a href="/car/[0-9]+/(?P<naslov>[A-Za-z0-9-]+)',
 re.DOTALL
)

#znamka_avta = re.compile(
# r'<a href=/car/[0-9]+/(?P<znamka>[A-Za-z]+)',
#  re.DOTALL
#)

model_avta = re.compile(
    r'<span class="model">(?P<model>[^<]+)',
 re.DOTALL
)

doseg_avta = re.compile(
    r'<span class="erange_real">(?P<doseg>[\d.]+) \w+</span>',
 re.DOTALL
)

kapaciteta_baterije = re.compile(
    r'<span class="battery hidden">(?P<kapaciteta>[0-9.]+)</span>',
 re.DOTALL
)

ucinkovitost_avta = re.compile(
    r'<span class="efficiency">(?P<ucinkovitost>\d+) Wh/km</span>',
 re.DOTALL
)

hitro_polnenje = re.compile(
    r'<span class="fastcharge_speed hidden">(?P<hitro_polnenje>\d+)</span>',
 re.DOTALL
)

teza_avta = re.compile(
    r'<span class="weight hidden">(?P<teza>\d+)</span>',
 re.DOTALL
)

moznost_vleke = re.compile(
    r'<span class="towweight hidden">(?P<vleka>\d+)</span>',
 re.DOTALL
)

pospesek_avta = re.compile(
    r'<span class="acceleration hidden">(?P<pospesek>[0-9.]+)</span>',
 re.DOTALL
)

prtljaga_volumen = re.compile(
    r'<span class="cargosort hidden">(?P<prtljaga>\d+)</span>',
 re.DOTALL
)

en_postanek = re.compile(
    r'<span class="long_distance_total_sort hidden">(?P<en_postanek>\d+)</span>',
 re.DOTALL
)

price_range = re.compile(
    r'<span class="priceperrange hidden">(?P<price_range>\d+)</span>',
 re.DOTALL
)

cena = re.compile(
    r'<span class="pricefilter hidden">(?P<cena>\d+)</span>',
 re.DOTALL
)

def pridobi(podatki, regex):
    m = regex.search(podatki)
    return m.group(1) if m else None

avtomobili = []
count = 0
for avto in vzorec_avta.finditer(vsebina):
    podatki = avto.group(1)

    avtomobili.append({
        "id": pridobi(podatki, id_avta),
        "naslov": pridobi(podatki, naslov_avta),
#        "znamka": pridobi(podatki, znamka_avta),
        "model": pridobi(podatki, model_avta),
        "doseg": pridobi(podatki, doseg_avta),
        "kapaciteta_baterije": pridobi(podatki, kapaciteta_baterije),
        "ucinkovitost": pridobi(podatki, ucinkovitost_avta),
        "hitro_polnenje": pridobi(podatki, hitro_polnenje),
        "teza": pridobi(podatki, teza_avta),
        "vleka": pridobi(podatki, moznost_vleke),
        "pospesek": pridobi(podatki, pospesek_avta),
        "prtljaga": pridobi(podatki, prtljaga_volumen),
        "en_postanek": pridobi(podatki, en_postanek),
        "price_range": pridobi(podatki, price_range),
        "cena": pridobi(podatki, cena),
    })
    
    
    count += 1

# Prikaz rezultatov
for avto in avtomobili:
    print(avto)

print(f"Število pobranih avtov je: {count}")

# Shranjevanje podatkov v csv
with open("avtomobili.csv", "w", newline="", encoding="utf-8") as dat:
        fieldnames = avtomobili[0].keys()
        writer = csv.DictWriter(dat, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(avtomobili)

print("Podatki uspešno shranjeni v 'avtomobili.csv'")
