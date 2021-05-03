"""
Lena Heide
Matr.-Nr.: 767488
30.4.2021
"""

from nltk.tokenize import RegexpTokenizer
from AbstractFeatures import Features

class stChFeats(Features):
	"""
	A class for extraction of character features from a list of strings.
	Attributes
	----------
	text
		A tokenized given text. An inherited attribute from an abstract
		class Features().
	Methods
	-------
	outputter
		Count the number of uppercase, lowercase and numeric characters
		and return an appropriate output.
		An inherited method from an abstract class Features().
    """
	def __init__(self, text: list):
		tokenizer = RegexpTokenizer(r"\w+")
		tokenized_text = []
		# stores the length of the original strings for normalization
		self.nr_char = []
		for string in text:
			tokenized_text.append(tokenizer.tokenize(string))
			self.nr_char.append(len(string))
		self.text = tokenized_text
		
	def outputter(self) -> list:
		"""
		Create an appropriate output.
		Returns
		-------
		out : list
			Nested list with number of uppercase, lowercase and
			numeric characters for a sentence in a given text.
		"""
		# the output
		out = [[0,0,0] for s in self.text]
		# ranges to id chars
		upper = range(ord('A'),ord('Z')+1)
		lower = range(ord('a'),ord('z')+1)
		num = range(ord('0'),ord('9')+1)
		# iterate over the list of tokenized texts
		for i in range(len(self.text)):
			# the string's features
			nr_lower = 0
			nr_upper = 0
			nr_num = 0
			# count the features
			for token in self.text[i]:
				for ch in token:
					och = ord(ch)
					if och in lower:
						nr_lower += 1
					elif och in upper:
						nr_upper += 1
					elif och in num:
						nr_num += 1
			# normalize the features
			nr_lower = nr_lower/self.nr_char[i]
			nr_upper = nr_upper/self.nr_char[i]
			nr_num = nr_num/self.nr_char[i]
			
			out[i][0] = nr_upper
			out[i][1] = nr_lower
			out[i][2] = nr_num
		
		return out

if __name__ == "__main__":
	# demo text
	gid0 = "1 In the myriadic year of our Lord"
	gid1 = "- the ten thousandth year of the King Undying, the kindly"
	gid1 += " Prince of Death!-"
	gid2 = " Gideon Nav packed her sword, her shoes, and her dirty "
	gid2 += "magazines, and she escaped from the House of the Ninth."
	gidN = stChFeats([gid0,gid1,gid2])
	fl = gidN.outputter()
	
	print("This script contains the class stChFeatures which is used to"
			" store the number of upper-, lowercase and numeric "
			"characters of strings from a list in a matrix.\nThe index "
			"of the list with the features corresponds to the index of "
			"the string in the given list, the features themselves are "
			"stored in the following order: uppercase, lowercase, "
			"numeric.\n")
	print("The example sentence was taken from Muir's 'Gideon the "
			"Ninth':")
	print([gid0,gid1,gid2])
	print("The normalized features:")
	print(fl)
