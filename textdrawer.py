class TextDrawer:
	def setFont(self, font):
		self.font = font

	def draw(self, text):
		for character in text:
			print self.font.letters[character.upper()]

    def loadFont(self, directory):
        font = Font("fancy")

        for filename in os.listdir(directory):
            font.letters[filename] = readFile(directory+filename)

        return font

    def readFile(filename):
        return open(filename).read()
