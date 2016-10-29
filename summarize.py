from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def generateSum(loc):
	# print("hi")
	parser = PlaintextParser.from_file(loc, Tokenizer("english"))
	summarizer = LexRankSummarizer()
	summary = summarizer(parser.document, 5)
	lis=[]
	for sentence in summary:
		lis.append(sentence)
	return lis	

	