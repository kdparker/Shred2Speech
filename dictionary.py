from unittest import skip
import requests

with open('secrets/merriamwebster', 'r') as client_file:
    key = client_file.read().strip()

ipa_to_note: dict[str, str] = {
    "e": "⬇",
    "æ": "🟢⬇",
    "ʌ": "🔴⬇",
    "ʊ": "🟡⬇",
    "ɒ": "🔵⬇",
    "ə": "🟠⬇",
    "i": "🟢🔴⬇",
    "ɜ": "🟢🟡⬇",
    "ɔ": "🟢🔵⬇",
    "u": "🟢🟠⬇",
    "ɑ": "🔴🟡⬇",
    "ɪ": "🟢🔴🟡🔵⬇",
    "ɛ": "🟢🔴🟡🔵⬆",
    "oʊ": "🔴🟡🔵🟠⬇",
    "ɪə": "🔴🔵⬇",
    "eə": "🔴🟠⬇",
    "eɪ": "🟡🔵⬇",
    "ɔɪ": "🟡🟠⬇",
    "aɪ": "🔵🟠⬇",
    "əʊ": "🟢🔴🟡⬇",
    "aʊ": "🟢🔴🔵⬇",
    "f": "🟢🟡🔵⬇",
    "v": "🔴🟡🔵⬇",
    "θ": "🔴🟡🟠⬇",
    "ð": "🔴🔵🟠⬇",
    "z": "🟡🔵🟠⬇",
    "ʃ": "⬆",
    "ʒ": "🟢⬆",
    "h": "🔴⬆",
    "p": "🟡⬆",
    "b": "🔵⬆",
    "t": "🟠⬆",
    "d": "🟢🔴⬆",
    "k": "🟢🟡⬆",
    "g": "🟢🔵⬆",
    "ʈʃ": "🟢🟠⬆",
    "dʒ": "🔴🟡⬆",
    "r": "🔴🔵⬆",
    "j": "🔴🟠⬆",
    "w": "🟡🔵⬆",
    "l": "🟡🟠⬆",
    "s": "🔵🟠⬆",
    "m": "🟢🔴🟡⬆",
    "n": "🟢🔴🔵⬆",
    "ng": "🟢🟡🔵⬆",
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
            hwi = definition["hwi"]
            for pronounciations in (hwi.get("prs", []) + hwi.get("altprs", [])):
                if "ipa" in pronounciations:
                    ipas.append(pronounciations["ipa"])
        ipas = set(ipas)
        for ipa in ipas:
            print(f"{ipa} - {make_chart_for_ipa(ipa)}")
    

if __name__ == "__main__":
    run()