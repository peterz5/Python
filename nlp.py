import nltk
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer

example_sentence = 'This is an example showing off stop word filtration'
stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
	if w not in stop_words:
		filtered_sentence.append(w) 

ps = PorterStemmer()

example_words=["python", 'pythoner', 'pythoning', 'pythoned', 'pythonly']

for w in example_words:
	#print(ps.stem(w))
	pass

new_text = 'It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once'

words = word_tokenize(new_text)

for w in words:
	#print(ps.stem(w))
	pass

train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized= custom_sent_tokenizer.tokenize(sample_text)

def process_content(tokenized):
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)

			#print(tagged)

			chunkGram = r"""Chunk: {<RB.?>'<VB.?>*<NNP>+<NN>?'}"""
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			chunked.draw()

	except Exception as e:
		print(str(e))

process_content(tokenized)


