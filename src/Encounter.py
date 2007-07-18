#
# encounter.py
# July 17, 2007
# Nick Loadholtes
#
# The data structure for an encounter
#



encounter = {
    'title' : 'Mike talking to Tom',
    'preamble' : 'Mike are you ok?',
    'conversation' : [(),
                      ('Are You ok?', 'yes_or_no(2,3)'),
                      ('Good, I\'m glad to hear that', '4'),
                      ('What? Toughen up you crybaby...', 'None'),
                      ('There was a bad earthquake!', 'pause(5)'),
                      ('I need you to go check on my neighbors, make sure they\
                      are ok.', 'None')
                      ],
    }


