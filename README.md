# Shred2Speech

A speech synthesizer based on a guitar hero controller. Requires a 360 X-Plorer Controller on a windows machine to make work.


To run, run python shred2speech after installing requirements, you may find dictionary.py useful to generate charts, however you will need a merriam webster learner dictionary api key in the secrets directory to run it.

Xinput from https://github.com/r4dian/Xbox-Controller-for-Python/blob/master/xinput.py
Sounds taken and edited from http://www.phonetics.ucla.edu/course/chapter1/chapter1.html and wikipedia

## IPA to Guitar

|Symbol |Examples |Chart |#|
|--|--|--|--|
|e|Went, intend, send, letter.|β¬|0
|Γ¦|Cat, hand, nap, flat, have.|π’β¬|1
|Κ|Fun, love, money, one, London, come.|π΄β¬|2
|Κ|Put, look, should, cook, book, look.|π‘β¬|4
|Ι|Rob, top, watch, squat, sausage.|π΅β¬|8
|Ι|Alive, again, mother.|π β¬|16
|i|Need, beat, team.|π’π΄β¬|3
|Ι|Nurse, heard, third, turn.|π’π‘β¬|5
|Ι|Talk, law, bored, yawn, jaw.|π’π΅β¬|9
|u|Few, boot, lose, gloomy, fruit, chew.|π’π β¬|17
|Ι|Fast, car, hard, bath.|π΄π‘β¬|6
|Ιͺ|Kit, Bit, Chip|π’π΄π‘π΅β¬|15
|Ι|Hello|π’π΄π‘π΅β¬|47
|oΚ|Hello|π΄π‘π΅π β¬|30
|ΙͺΙ|Near, ear, clear, tear, beer, fear|π΄π΅β¬|10
|eΙ|Hair, there, care, stairs, pear|π΄π β¬|18
|eΙͺ|Face, space, rain , case, eight|π‘π΅β¬|12
|ΙΙͺ|Joy, employ, toy, coil, oyster.|π‘π β¬|20
|aΙͺ|My, sight, pride, kind, flight|π΅π β¬|24
|ΙΚ|No, donβt, stones, alone, hole|π’π΄π‘β¬|7
|aΚ|Mouth, house, brown, cow, out|π’π΄π΅β¬|11
|f|Full, Friday, fish, knife.|π’π‘π΅β¬|13
|v|Vest, village, view, cave.|π΄π‘π΅β¬|14
|ΞΈ|Thought, think, Bath.|π΄π‘π β¬|22
|Γ°|There, those, brothers, others.|π΄π΅π β¬|26
|z|Zoo, crazy, lazy, zigzag, nose.|π‘π΅π β¬|28
|Κ|Shirt, rush, shop, cash.|β¬|32
|Κ|Television, delusion, casual|π’β¬|33
|h|High, help, hello.|π΄β¬|34
|p|Pin, cap, purpose, pause.|π‘β¬|36
|b|Bag, bubble, build, robe.|π΅β¬|40
|t|Time, train, tow, late.|π β¬|48
|d|Door, day, drive, down, feed.|π’π΄β¬|35
|k|Cash, quick, cricket, sock.|π’π‘β¬|37
|g|Girl, green, grass, flag.|π’π΅β¬|41
|ΚΚ|Choose, cheese, church, watch.|π’π β¬|49
|dΚ|Joy, juggle, juice, stage.|π΄π‘β¬|38
|r|Road, roses, river, ring, ride.|π΄π΅β¬|42
|j|Yellow, usual, tune, yesterday, yard.|π΄π β¬|50
|w|Wall, walk, wine, world.|π‘π΅β¬|44
|l|Law, lots, leap, long, pill, cold, chill,|π‘π β¬|52
|s|Sit, Sap|π΅π β¬|56
|m|Tim|π’π΄π‘β¬|39
|n|Tin|π’π΄π΅β¬|43
|ng|Ting|π’π‘π΅β¬|45