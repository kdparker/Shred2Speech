from unittest import skip
import requests

with open('secrets/merriamwebster', 'r') as client_file:
    key = client_file.read().strip()

ipa_to_note: dict[str, str] = {
    "e": "โฌ",
    "รฆ": "๐ขโฌ",
    "ส": "๐ดโฌ",
    "ส": "๐กโฌ",
    "ษ": "๐ตโฌ",
    "ษ": "๐ โฌ",
    "i": "๐ข๐ดโฌ",
    "ษ": "๐ข๐กโฌ",
    "ษ": "๐ข๐ตโฌ",
    "u": "๐ข๐ โฌ",
    "ษ": "๐ด๐กโฌ",
    "ษช": "๐ข๐ด๐ก๐ตโฌ",
    "ษ": "๐ข๐ด๐ก๐ตโฌ",
    "oส": "๐ด๐ก๐ต๐ โฌ",
    "ษชษ": "๐ด๐ตโฌ",
    "eษ": "๐ด๐ โฌ",
    "eษช": "๐ก๐ตโฌ",
    "ษษช": "๐ก๐ โฌ",
    "aษช": "๐ต๐ โฌ",
    "ษส": "๐ข๐ด๐กโฌ",
    "aส": "๐ข๐ด๐ตโฌ",
    "f": "๐ข๐ก๐ตโฌ",
    "v": "๐ด๐ก๐ตโฌ",
    "ฮธ": "๐ด๐ก๐ โฌ",
    "รฐ": "๐ด๐ต๐ โฌ",
    "z": "๐ก๐ต๐ โฌ",
    "ส": "โฌ",
    "ส": "๐ขโฌ",
    "h": "๐ดโฌ",
    "p": "๐กโฌ",
    "b": "๐ตโฌ",
    "t": "๐ โฌ",
    "d": "๐ข๐ดโฌ",
    "k": "๐ข๐กโฌ",
    "g": "๐ข๐ตโฌ",
    "สส": "๐ข๐ โฌ",
    "dส": "๐ด๐กโฌ",
    "r": "๐ด๐ตโฌ",
    "j": "๐ด๐ โฌ",
    "w": "๐ก๐ตโฌ",
    "l": "๐ก๐ โฌ",
    "s": "๐ต๐ โฌ",
    "m": "๐ข๐ด๐กโฌ",
    "n": "๐ข๐ด๐ตโฌ",
    "ng": "๐ข๐ก๐ตโฌ",
}

def make_chart_for_ipa(pronounciation:str) -> str:
    output = ""
    skip_next = False
    for i, char in enumerate(pronounciation):
        if skip_next:
            skip_next = False
            continue
        if i < len(pronounciation) - 1:
            pair = char + pronounciation[i]
            if pair in ipa_to_note:
                output += ipa_to_note[pair]
                skip_next = True
                continue
        if char in ipa_to_note:
            output += ipa_to_note[char]
    return output

def run():
    while True:
        print("Input a single word to get the chart for it")
        word = input()
        dictionary_response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/learners/json/{word}?key={key}").json()
        ipas = []
        for definition in dictionary_response:
            if "hwi" in definition:
                hwi = definition["hwi"]
                for pronounciations in (hwi.get("prs", []) + hwi.get("altprs", [])):
                    if "ipa" in pronounciations:
                        ipas.append(pronounciations["ipa"])
        ipas = set(ipas)
        if not ipas:
            print("No definition found on Merriam Webster")
        for ipa in ipas:
            print(f"{ipa} - {make_chart_for_ipa(ipa)}")
    

if __name__ == "__main__":
    run()