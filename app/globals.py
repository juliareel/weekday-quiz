MONTH_CODE_MAPPING = {  1:0,
                        2:3,
                        3:3,
                        4:6,
                        5:1,
                        6:4,
                        7:6,
                        8:2,
                        9:5,
                        10:0,
                        11:3,
                        12:5 }

CENTURY_CODE_MAPPING = {17:4,
                        18:2,
                        19:0,
                        20:6,
                        21:4,
                        22:2,
                        23:0 }

DAY_MAPPING = { 0:'sunday',
                1:'monday',
                2:'tuesday',
                3:'wednesday',
                4:'thursday',
                5:'friday',
                6:'saturday' }

DAY_MAPPING_ABBR = {0:'sun',
                    1:'mon',
                    2:'tue',
                    3:'wed',
                    4:'thu',
                    5:'fri',
                    6:'sat' }

QUIZ_TYPES = {  'Mod 7 Division': 'Modulo 7 of a random number',
                'Floor 4 Division': 'Integer division by 4',
                'Day of Week': 'Find the day of the week for a given date',
                'Year Code': 'Calculate the year code',
                'Month Code': 'Find the month code',
                'Century Code': 'Find the century code'
}

QUIZ_INPUT_TYPE = { 'Day of Week': 'date',
                    'Year Code': 'date',
                    'Month Code': 'date',
                    'Century Code': 'date',
                    'Mod 7 Division': 'int',
                    'Floor 4 Division': 'int'}
