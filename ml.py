from wordfreq import zipf_frequency, word_frequency

from gensim.summarization import keywords
text = "Nuclear power is a clean and efficient way of boiling water to make steam, which turns turbines to produce electricity. Nuclear power plants use low-enriched uranium fuel to produce electricity through a process called fission the splitting of uranium atoms in a nuclear reactor. Uranium fuel consists of small, hard ceramic pellets that are packaged into long, vertical tubes. Bundles of this fuel are inserted into the reactor.A single uranium pellet, slightly larger than a pencil eraser, contains the same energy as a ton of coal, 3 barrels of oil, or 17,000 cubic feet of natural gas. Each uranium fuel pellet provides up to five years of heat for power generation. And because uranium is one of the world’s most abundant metals, it can provide fuel for the world’s commercial nuclear plants for generations to come. Nuclear power offers many benefits for the environment as well. Power plants don’t burn any materials so they produce no combustion by-products. Additionally, because they don’t produce greenhouse gases, nuclear plants help protect air quality and mitigate climate change. When it comes to efficiency and reliability, no other electricity source can match nuclear. Nuclear power plants can continuously generate large-scale, around-the-clock electricity for many months at a time, without interruption. Currently, nuclear energy supplies 12 percent of the world's electricity and approximately 20 percent of the energy in the United States. As of 2018, a total of 30 countries worldwide are operating 450 nuclear reactors for electricity generation. For decades, GE and Hitachi have been at the forefront of nuclear technology, setting the industry benchmark for reactor design and construction and helping utility customers operate their plants safely and reliably."

text = text.replace(".", " ")
text = text.replace(",", " ")
y = set(text.split(" "))
y=list(y)
x = keywords(text, words=100,scores = True, lemmatize = True)
x=list(x)
print("len x", len(x), "len y", len(y))

wList = []

for w in y:
    freq=round(float(zipf_frequency(w, 'en')), 3)
    wList.append([round((10-freq)/10-0.15,2), w])

print(sorted(wList))
print(x)
c=0
for a in x:
    for b in range(len(wList)):
        if wList[b][1] in a:
            a[1]+=wList[b][0]
    


print(x)

# print(y)
# for t in y:
#     if (1 - round(float(word_frequency(t, 'en'))*10000, 3)) > 0: 
#         numb = ((1 - round(float(word_frequency(t, 'en'))*10000, 3))+ x[c][1])/2
#         tList.append([numb, t])
#     c+=1

# print(sorted(tList))

# print(tList)

###########################################################################################

# from rake_nltk import Rake, Metric
# from collections import Counter
# r = Rake(max_length=3) # Uses stopwords for english from NLTK, and all puntuation characters.

# document='The function of this library is automatic summarization using a kind of natural language processing and neural network language model. This library enable you to create a summary with the major points of the original document or web-scraped text that filtered by text clustering. And this library applies pydbm to implement Encoder/Decoder based on LSTM (with an Attention mechanism) improving the accuracy of summarization by Sequence-to-Sequence(Seq2Seq) learning.'

# r.extract_keywords_from_text(document)

# # print(r.get_ranked_phrases_with_scores()) # To get keyword phrases ranked highest to lowest.

# print(Counter(document.split()).most_common())

# for i in range(len(r.get_ranked_phrases_with_scores())):
#     t=0
#     for w in r.get_ranked_phrases_with_scores()[i][1].split(" "):
#         t+=document.count(w)
#     print(t*r.get_ranked_phrases_with_scores()[i][0], r.get_ranked_phrases_with_scores()[i][1])
#     print(r.get_ranked_phrases_with_scores()[i][0], r.get_ranked_phrases_with_scores()[i][1])
#     print("-----------------------------------")


###########################################################################################

# from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
# from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
# from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

# # Object of automatic summarization.
# auto_abstractor = AutoAbstractor()
# # Set tokenizer.
# auto_abstractor.tokenizable_doc = SimpleTokenizer()
# # Set delimiter for making a list of sentence.
# auto_abstractor.delimiter_list = [".", "\n"]
# # Object of abstracting and filtering document.
# abstractable_doc = TopNRankAbstractor()
# # Summarize document.
# result_dict = auto_abstractor.summarize(document, abstractable_doc)

# # Output result.
# for sentence in result_dict["summarize_result"]:
#     print(sentence)