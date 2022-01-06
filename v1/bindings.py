#1 = ON, 0 = OFF
#Example: 40 = Alternator off

#PINS:
#1 Master
#4 Alternator
#5 Avionics
#6 Parking break
#7 Nav lights
#8 Beacon lights
#9 Strobe lights
#10 Taxi lights
#11 Landing lights
#12 Pitot heat
#13B AP button
#14B APPR button
#15 Landing gear
#19B Flaps up button
#20B Flaps down button
#T+\- Thrust UP\DOWN
#M+\- Mixture UP\DOWN
#P+\- Propeller UP\DOWN
#A+\- Altitude UP\DOWN
#AB Altitude AP button -----
#H+\- Heading UP\DOWN
#HB Heading AP button ------
#V+\- VS UP\DOWN
#VB - VS AP button -----
#N+\- Nav freq UP\DOWN
#NB ...
#C+\- Com freq UP\DOWN
#CB ...
#B+\- Barometer UP\DOWN
#BB barometer push button (STD Baro)

keys = {
'ENTER': '13',
'SHIFT': '16',
'CTRL': '17',
'ALT': '18',
'SPACE': '32',
'PGUP': '33',
'PGDN': '34',
'END': '35',
'HOME': '36',
'LARR': '37',
'UARR': '38',
'RARR': '39',
'DARR': '40',
'INS': '45',
'DEL': '46',
'0': '48',
'1': '49',
'2': '50',
'3': '51',
'4': '52',
'5': '53',
'6': '54',
'7': '55',
'8': '56',
'9': '57',
'A': '65',
'B': '66',
'C': '67',
'D': '68',
'E': '69',
'F': '70',
'G': '71',
'H': '72',
'I': '73',
'J': '74',
'K': '75',
'L': '76',
'M': '77',
'N': '78',
'O': '79',
'P': '80',
'Q': '81',
'R': '82',
'S': '83',
'T': '84',
'U': '85',
'V': '86',
'W': '87',
'X': '88',
'Y': '89',
'Z': '90',
'NUM0': '96',
'NUM1': '97',
'NUM2': '98',
'NUM3': '99',
'NUM4': '100',
'NUM5': '101',
'NUM6': '102',
'NUM7': '103',
'NUM8': '104',
'NUM9': '105',
'MULT': '106',
'ADD': '107',
'SEP': '108',
'SUBTR': '109',
'DEC': '110',
'DIV': '111',
'F1': '112',
'F2': '113',
'F3': '114',
'F4': '115',
'F5': '116',
'F6': '117',
'F7': '118',
'F8': '119',
'F9': '120',
'F10': '121',
'F11': '122',
'F12': '123'
}

def multikeys(k1, k2, k3):
    if k3 == '':
        return str(keys[k1] + '_' + keys[k2])
    else:
        return str(keys[k1] + '_' + keys[k2] + '_' + keys[k3])

bindings = {
'10': multikeys('ALT', 'B', ''),
'11': multikeys('ALT', 'B', ''),
'40': multikeys('ALT', 'A', ''),
'41': multikeys('ALT', 'A', ''),
'50': keys['PGUP'],
'51': keys['PGUP'],
'60': multikeys('CTRL', 'DEC', ''),
'61': multikeys('CTRL', 'DEC', ''),
'70': multikeys('ALT', 'N', ''),
'71': multikeys('ALT', 'N', ''),
'80': multikeys('ALT', 'H', ''),
'81': multikeys('ALT', 'H', ''),
'90': keys['O'],
'91': keys['O'],
'100': multikeys('ALT', 'J', ''),
'101': multikeys('ALT', 'J', ''),
'110': multikeys('CTRL', 'L', ''),
'111': multikeys('CTRL', 'L', ''),
'120': multikeys('SHIFT', 'H', ''),
'121': multikeys('SHIFT', 'H', ''),
'13B': keys['Z'],
'14B': multikeys('CTRL','A', ''),
'150': keys['G'],
'151': keys['G'],
'19B': keys['F6'],
'20B': keys['F7'],
'T+': keys['F3'],
'T-': keys['F2'],
'M+': multikeys('SHIFT', 'CTRL', 'F3'),
'M-': multikeys('SHIFT', 'CTRL', 'F2'),
'P+': multikeys('CTRL', 'F3', ''),
'P-': multikeys('CTRL', 'F2', ''),
'A+': multikeys('CTRL', 'PGUP', ''),
'A-': multikeys('CTRL', 'PGDN', ''),
'H+': multikeys('CTRL', 'INS', ''),
'H-': multikeys('CTRL', 'DEL', ''),
'V+': multikeys('CTRL', 'HOME', ''),
'V-': multikeys('CTRL', 'END', ''),
'NB': multikeys('SHIFT', 'CTRL', 'N'),
'N+': multikeys('SHIFT', 'CTRL', 'NAV9'),
'N-': multikeys('SHIFT', 'CTRL', 'NAV3'),
}

