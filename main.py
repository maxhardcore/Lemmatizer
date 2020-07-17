import spacy
from spacy_spanish_lemmatizer import SpacyCustomLemmatizer

nlp = spacy.load("es_core_news_sm")
lemmatizer = SpacyCustomLemmatizer()
nlp.add_pipe(lemmatizer, name="lemmatizer", after="tagger")
for token in nlp(
    """Con estos fines, la Dirección de Gestión y Control Financiero monitorea
       la posición de capital del Banco y utiliza los mecanismos para hacer un
       eficiente manejo del capital."""
):
    print(token.lemma_)


