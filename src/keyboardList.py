keyboardMac = {
    "Key.esc": ["    esc", None, None, 100, 100, 180, 140],
    "Key.f1": ["F1", None, None, 190, 100, 230, 140],
    "Key.f2": ["F2", None, None, 240, 100, 280, 140],
    "Key.f3": ["F3", None, None, 290, 100, 330, 140],
    "Key.f4": ["F4", None, None, 340, 100, 380, 140],
    "Key.f5": ["F5", None, None, 390, 100, 430, 140],
    "Key.f6": ["F6", None, None, 440, 100, 480, 140],
    "Key.f7": ["F7", None, None, 490, 100, 530, 140],
    "Key.f8": ["F8", None, None, 540, 100, 580, 140],
    "Key.f9": ["F9", None, None, 590, 100, 630, 140],
    "Key.f10": ["F10", None, None, 640, 100, 680, 140],
    "Key.f11": ["F11", None, None, 690, 100, 730, 140],
    "Key.f12": ["F12", None, None, 740, 100, 780, 140],
    "'`'": ["`", "~", None, 100, 150, 140, 190],
    "'1'": ["1", "!", None, 150, 150, 190, 190],
    "'2'": ["2", "@", None, 200, 150, 240, 190],
    "'3'": ["3", "#", None, 250, 150, 290, 190],
    "'4'": ["4", "$", None, 300, 150, 340, 190],
    "'5'": ["5", "%", None, 350, 150, 390, 190],
    "'6'": ["6", "^", None, 400, 150, 440, 190],
    "'7'": ["7", "&", None, 450, 150, 490, 190],
    "'8'": ["8", "*", None, 500, 150, 540, 190],
    "'9'": ["9", "(", None, 550, 150, 590, 190],
    "'0'": ["0", ")", None, 600, 150, 640, 190],
    "'-'": ["-", "_", None, 650, 150, 690, 190],
    "'='": ["=", "+", None, 700, 150, 740, 190],
    "Key.backspace": ["    delete", None, None, 750, 150, 830, 190],
    "Key.tab": ["    tab", None, None, 100, 200, 180, 240],
    "'q'": ["Q", None, None, 190, 200, 230, 240],
    "'w'": ["W", None, None, 240, 200, 280, 240],
    "'e'": ["E", None, None, 290, 200, 330, 240],
    "'r'": ["R", None, None, 340, 200, 380, 240],
    "'t'": ["T", None, None, 390, 200, 430, 240],
    "'y'": ["Y", None, None, 440, 200, 480, 240],
    "'u'": ["U", None, None, 490, 200, 530, 240],
    "'i'": ["I", None, None, 540, 200, 580, 240],
    "'o'": ["O", None, None, 590, 200, 630, 240],
    "'p'": ["P", None, None, 640, 200, 680, 240],
    "'['": ["[", None, None, 690, 200, 730, 240],
    "']'": ["]", None, None, 740, 200, 780, 240],
    "'\\\\'": ["\\", None, None, 790, 200, 830, 240],
}

for i in range(13):
    print(190+50*i, 200, 230+50*i, 240, sep=", ")