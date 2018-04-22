import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
 
def word_feats(words):
    return dict([(words.strip(), True)])

#positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)','yes' ]
#negative_vocab = [ 'bad', 'terrible','useless', 'hate', ':(' , 'not at all','not', 'no', "didn't","don't"]
#neutral_vocab = [ 'movie','the','sound','was','is','actors','did','words' ]


positive_vocab = open('positive_words.txt','r')
negative_vocab = open('negative_words.txt','r')
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','words' ]
 
positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
 
train_set = negative_features + positive_features + neutral_features
 
classifier = NaiveBayesClassifier.train(train_set) 
 
# Predict
def predict(sentence):
	neg = 0
	pos = 0
	#sentence = "I am satisfied"
	sentence = sentence.lower()
	words = sentence.split(' ')
	for word in words:
		classResult = classifier.classify( word_feats(word))
		if classResult == 'neg':
			neg = neg + 1
		if classResult == 'pos':
			pos = pos + 1
		
	positive = str(float(pos)/len(words))
	negative = str(float(neg)/len(words))
	
	return positive, negative
	
#pos,neg = predict("somewhat")
#print("\nPositive: "+pos+"\nnegative: "+neg)