color = {
        'fore':
        {   # Foreground
            'black'    : '30',   #  black
            'red'      : '31',   #  red
            'green'    : '32',   #  green
            'yellow'   : '33',   #  yellow
            'blue'     : '34',   #  blue
            'purple'   : '35',   #  purple
            'cyan'     : '36',   #  blue-green
            'white'    : '37',   #  white
        },

        'back' :
        {   # Background
            'black'     : '40',  #  black
            'red'       : '41',  #  red
            'green'     : '42',  #  green
            'yellow'    : '43',  #  yellow
            'blue'      : '44',  #  blue
            'purple'    : '45',  #  purplr
            'cyan'      : '46',  #  blue-green
            'white'     : '47',  #  white
        },

        'mode' :
        {   # Display
            'normal'    : '0',   #  default
            'highlight' : '1',   #  highlight
            'underline' : '4',   #  underline
            'blink'     : '5',   #  blink
            'inverse'   : '7',   #  inverse
            'hide'      : '8',   #  unvisible
        },

        'default' :
        {
            'end' : '0',
        },
}
def custom(fore=None, back=None, display=None):
    if fore:
        try:
            fore = color['fore'][fore]
        except:
            print('Foreground key: {} is error'.format(fore))
    if back:
        try:
            back = color['back'][back]
        except:
            print('Background key: {} is error'.format(back))
    if display:
        try:
            display = color['mode'][display]
        except:
            print('display key: {} is error'.format(display))

    style = ';'.join([s for s in [display, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % color['default']['end'] if style else ''
    return (style, end)
