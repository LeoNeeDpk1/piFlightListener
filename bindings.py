#1 = ON, 0 = OFF
#Example: 40 = Alternator off, 81 = Beacon lights on

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
#A+\- Altitude UP\DOWN
#AB Altitude AP button
#H+\- Heading UP\DOWN
#HB Heading AP button
#V+\- VS UP\DOWN
#VB - VS AP button
#NB AP NAV button
#B+\- Barometer UP\DOWN
#BB barometer push button (STD Baro)

bindings = {
'10': 'TOGGLE_MASTER_BATTERY',
'11': 'TOGGLE_MASTER_BATTERY',
'40': 'TOGGLE_MASTER_ALTERNATOR',
'41': 'TOGGLE_MASTER_ALTERNATOR',
'50': 'TOGGLE_AVIONICS_MASTER',
'51': 'TOGGLE_AVIONICS_MASTER',
'60': 'PARKING_BRAKES',
'61': 'PARKING_BRAKES',
'70': 'TOGGLE_NAV_LIGHTS',
'71': 'TOGGLE_NAV_LIGHTS',
'80': 'TOGGLE_BEACON_LIGHTS',
'81': 'TOGGLE_BEACON_LIGHTS',
'90': 'STROBES_OFF',
'91': 'STROBES_ON',
'100': 'TOGGLE_TAXI_LIGHTS',
'101': 'TOGGLE_TAXI_LIGHTS',
'110': 'LANDING_LIGHTS_OFF',
'111': 'LANDING_LIGHTS_ON',
'120': 'PITOT_HEAT_TOGGLE',
'121': 'PITOT_HEAT_TOGGLE',
'13B': 'AP_MASTER',
'14B': 'AP_APR_HOLD',
'150': 'GEAR_DOWN',
'151': 'GEAR_UP',
'19B': 'FLAPS_DECR',
'20B': 'FLAPS_INCR',
'24B': 'ANTI_ICE_TOGGLE',
'A+': 'AP_ALT_VAR_INC',
'A-': 'AP_ALT_VAR_DEC',
'AB': 'AP_ALT_HOLD',
'H+': 'HEADING_BUG_INC',
'H-': 'HEADING_BUG_DEC',
'HB': 'AP_HDG_HOLD',
'V+': 'AP_VS_VAR_INC',
'V-': 'AP_VS_VAR_DEC',
'VB': 'AP_VS_VAR_SET_ENGLISH',
'NB': 'AP_NAV1_HOLD_ON',
'B+': 'KOHLSMAN_INC',
'B-': 'KOHLSMAN_DEC',
'BB': 'BARO_STD', #No such event. Simcontrol.py scenario
'E+': 'ELEV_TRIM_DN',
'E-': 'ELEV_TRIM_UP'
}

