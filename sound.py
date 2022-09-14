import time
from playsound import playsound

sound_dict = {
    # from the IPA to Guitar Chart in README, needed to change filenames due to windows DLL issues with playsound
    0: ["sounds/e.wav"],
    1: ["sounds/ae.wav"],
    2: ["sounds/upside_down_v.wav"],
    4: ["sounds/edged_u.wav"],
    8: ["sounds/not_quite_p.wav"],
    16: ["sounds/upside_down_e.wav"],
    3: ["sounds/i.wav"],
    5: ["sounds/3.wav"],
    9: ["sounds/mirror_c.wav"],
    17: ["sounds/u.wav"],
    6: ["sounds/weird_a.wav"],
    10: ["sounds/capital_I.wav", "sounds/upside_down_e.wav"],
    18: ["sounds/e.wav", "sounds/upside_down_e.wav"],
    12: ["sounds/e.wav", "sounds/capital_I.wav"],
    20: ["sounds/mirror_c.wav", "sounds/capital_I.wav"],
    24: ["sounds/a.wav", "sounds/capital_I.wav"],
    7: ["sounds/upside_down_e.wav", "sounds/edged_u.wav"],
    11: ["sounds/a.wav", "sounds/edged_u.wav"],
    13: ["sounds/f.wav"],
    14: ["sounds/v.wav"],
    22: ["sounds/0.wav"],
    26: ["sounds/fancy_d.wav"],
    28: ["sounds/z.wav"],
    32: ["sounds/long_S.wav"],
    33: ["sounds/big_three.wav"],
    34: ["sounds/h.wav"],
    36: ["sounds/p.wav"],
    40: ["sounds/b.wav"],
    48: ["sounds/t.wav"],
    35: ["sounds/d.wav"],
    37: ["sounds/k.wav"],
    41: ["sounds/g.wav"],
    49: ["sounds/long_S.wav"], # todo add "sounds/ʈ.wav", before
    38: ["sounds/d.wav", "sounds/big_three.wav"],
    42: ["sounds/r.wav"],
    50: ["sounds/j.wav"],
    44: ["sounds/w.wav"],
    52: ["sounds/l.wav"],
}

def play_sound(key: int) -> None:
    for i, sound in enumerate(sound_dict.get(key, [])):
        if i > 0:
            time.sleep(0.05)
        playsound(sound, False)