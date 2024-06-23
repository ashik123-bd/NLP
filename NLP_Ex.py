import spacy
nlp = spacy.load('en_core_web_sm')

about_text = ('I am a python developer currently'
              'working for a london-based Fintech'
              'company. I am interested in learning '
              'Natural Language Processing.')

about_doc = nlp(about_text)
sentences = list(about_doc.sents)

for sentence in sentences:
    print(sentence)


for token in about_doc:
    print(token, token.idx)    