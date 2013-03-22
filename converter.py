from font import FontLoader, Font
from textdrawer import TextDrawer

def main():
    text=getText()
    font=FontLoader().loadFont('fancyFont/')
    drawer=TextDrawer()
    drawer.setFont(font)
    drawer.draw(text)


def getText():
    if len(sys.argv) != 2:
        print "Bad arguments"
        sys.exit(1)

    return sys.argv[1]


if __name__ == '__main__':
    main()
	
