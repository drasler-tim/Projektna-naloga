import requests

URL = "https://ev-database.org/#group=vehicle-group&rs-pr=10000_100000&rs-er=0_1000&rs-ld=0_1000&rs-ac=2_23&rs-dcfc=0_400&rs-ub=10_200&rs-tw=0_2500&rs-ef=100_350&rs-sa=-1_5&rs-w=1000_3500&rs-c=0_5000&rs-y=2010_2030&s=1&p=0-50"

OUTPUT_FILE = "avti.html"

def shrani_html(url, izhodna_datoteka):
    """Prenese HTML vsebino strani in jo shrani v datoteko."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    try:
        print(f"Prenašam stran: {url}")
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Napaka pri prenosu strani: {e}")
        return

    with open(izhodna_datoteka, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"HTML uspešno shranjen v datoteko '{izhodna_datoteka}'.")


if __name__ == "__main__":
    shrani_html(URL, OUTPUT_FILE)
