from docx.enum.text import WD_COLOR_INDEX

def color_paragraph(paragraph, color:str):
    # Get the style of the paragraph
    if color == 'black':
        color_element = WD_COLOR_INDEX.BLACK
    elif color == 'blue':
        color_element = WD_COLOR_INDEX.BLUE
    elif color == 'green':
        color_element = WD_COLOR_INDEX.BRIGHT_GREEN
    elif color == 'dark blue':
        color_element = WD_COLOR_INDEX.DARK_BLUE
    elif color == 'dark red':
        color_element = WD_COLOR_INDEX.DARK_RED
    elif color == 'dark yellow':
        color_element = WD_COLOR_INDEX.DARK_YELLOW
    elif color == 'dark green':
        color_element = WD_COLOR_INDEX.GREEN
    elif color == 'pink':
        color_element = WD_COLOR_INDEX.PINK
    elif color == 'red':
        color_element = WD_COLOR_INDEX.PINK
    elif color == 'white':
        color_element = WD_COLOR_INDEX.WHITE
    elif color == 'teal':
        color_element = WD_COLOR_INDEX.TEAL
    elif color == 'yellow':
        color_element = WD_COLOR_INDEX.YELLOW
    elif color == 'violet':
        color_element = WD_COLOR_INDEX.VIOLET
    elif color == 'gray25':
        color_element = WD_COLOR_INDEX.GRAY_25
    elif color == 'gray50':
        color_element = WD_COLOR_INDEX.GRAY_50
    
    return color_element