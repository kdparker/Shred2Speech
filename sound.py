import time
from playsound import playsound

sound_dict = {
    # from the IPA to Guitar Chart in README, needed to change filenames due to windows DLL issues with playsound
    0: "sounds/e.wav",
    1: "sounds/ae.wav",
    2: "sounds/upside_down_v.wav",
    4: "sounds/edged_u.wav",
    8: "sounds/not_quite_p.wav",
    16: "sounds/upside_down_e.wav",
    3: "sounds/i.wav",
    5: "sounds/3.wav",
    9: "sounds/mirror_c.wav",
    17: "sounds/u.wav",
    6: "sounds/weird_a.wav",
    15: "sounds/capital_I.wav",
    47: "sounds/reverse_3.wav",
    30: "sounds/o.wav",
    10: "sounds/10.wav",
    18: "sounds/18.wav",
    12: "sounds/12.wav",
    20: "sounds/20.wav",
    24: "sounds/24.wav",
    7: "sounds/7.wav",
    11: "sounds/11.wav",
    13: "sounds/f.wav",
    14: "sounds/v.wav",
    22: "sounds/0.wav",
    26: "sounds/fancy_d.wav",
    28: "sounds/z.wav",
    32: "sounds/long_S.wav",
    33: "sounds/big_three.wav",
    34: "sounds/h.wav",
    36: "sounds/p.wav",
    40: "sounds/b.wav",
    48: "sounds/t.wav",
    35: "sounds/d.wav",
    37: "sounds/k.wav",
    41: "sounds/g.wav",
    49: "sounds/tS.wav",
    38: "sounds/d3.wav",
    42: "sounds/r.wav",
    50: "sounds/j.wav",
    44: "sounds/w.wav",
    52: "sounds/l.wav",
    56: "sounds/s.wav",
    39: "sounds/m.wav",
    43: "sounds/n.wav",
    45: "sounds/ng.wav",
}


def play_sound(key: int) -> None:
    if key in sound_dict:
        playsound(sound_dict[key], False)
