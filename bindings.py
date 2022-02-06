# 1 = ON, 0 = OFF, B = Button (state is not needed).
# Example: 60 = pin 6 off, 151 = pin 15 on.
# Check your piFlightBox configuration.


# BUTTON : EVENT_ID
bindings = {
'1B': 'TOGGLE_MASTER_BATTERY',
'4B': 'TOGGLE_MASTER_ALTERNATOR',
'5B': 'TOGGLE_AVIONICS_MASTER',
'60': 'PARKING_BRAKES',
'61': 'PARKING_BRAKES',
'7B': 'TOGGLE_BEACON_LIGHTS',
'8B': 'STROBES_TOGGLE',
'9B': 'TOGGLE_TAXI_LIGHTS',
'10B': 'LANDING_LIGHTS_TOGGLE',
'11B': 'AP_APR_HOLD',
'12B': 'AP_MASTER',
'13B': 'TOGGLE_NAV_LIGHTS',
'14B': 'PITOT_HEAT_TOGGLE',
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
#'NB': 'AP_NAV1_HOLD_ON',
'B+': 'KOHLSMAN_INC',
'B-': 'KOHLSMAN_DEC',
'BB': '@BARO_STD', #scenario
'E+': 'ELEV_TRIM_DN',
'E-': 'ELEV_TRIM_UP',

#Potentiometer names from piFlightBox config.py
'THROTTLE': 'THROTTLE_SET',
'MIXTURE': 'MIXTURE_SET',

}

#SCENARIOS:
scenarios = [
    {"name":"@BARO_STD", "id": "KOHLSMAN_SET", "value": 1013}

]


