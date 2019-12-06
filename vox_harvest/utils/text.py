import re
import os
from num2words import num2words

SUPPORTED_LANG = ['fr', 'en']

NUMBER_RE = re.compile(r"([0-9]+)")

FR_ABRV = [(re.compile(x[0], re.IGNORECASE), x[1]) for x in[
    (r"M\. ", "Monsieur "),
    (r" Mme ", " Madame "),
    (r"Mlle", "Mademoiselle"),
    (r"MM\.", "Messieur"),
    (r"Mgr", "Monseigneur"),
    (r" Mmes ", " Mesdames "),
    (r"N°", "numéro "),
    (r"Bat\.", "batiment"),
    (r"Ex\. ", "exemple "),
    (r"Cpt\.", "Capitaine"),
    (r"Sgt\.", "Sergent"),
    (r"jr\.", "junior"),
    (r"&", " et ")]]

FR_ORDINAL = re.compile(r"([0-9]+)[e|re|de]", re.IGNORECASE)

def split_text(input_text: str, separators: list = ['\.', '\n', ';', '!', '\?']):
    # Insert separator character
    regex = re.compile("({})".format("|".join(separators)))
    text_aug = regex.sub(r"\1|", input_text)
    sentences = text_aug.split('|')
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 1:
            cleaned_sentences.append(sentence)
        elif len(sentence) == 1:
            cleaned_sentences[-1] += sentence
    return cleaned_sentences

def get_cleaner_fun(lang: str)-> callable:
    if not lang.lower() in SUPPORTED_LANG:
        raise NotImplementedError("{} language is not implemented yet".format(lang))
    return LANG_CLEANER_MAP[lang.lower()]

def french_cleaner(text: str) -> str:
    def number_cleaner(text: str) -> str:
        def replace_ordinal(m):
            return num2words(m.group(1), to='ordinal', lang='fr')

        def replace_number(m):
            return num2words(m.group(1), lang='fr')

        #Ordinal
        text = FR_ORDINAL.sub(replace_ordinal, text)
        #Non ordinal
        text = re.sub(r"([0-9]+),([0-9]+)", r"\1 virgule \2", text)
        text = NUMBER_RE.sub(replace_number, text)
        return text

    def abrv_cleaner(text: str) -> str:
        for regex, replacement in FR_ABRV:
            text = re.sub(regex, replacement, text)
        return text
    
    text = abrv_cleaner(text)
    return number_cleaner(text)

def english_cleaner(text:str):
    pass

def cleaner(text, lang, separators):
    try:
        clean_fun = get_cleaner_fun(lang)
    except NotImplementedError as e:
        raise ValueError(e.args)
    sentences = split_text(text, separators)
    sentences_cleaned = []
    for sentence in sentences:
        sentences_cleaned.append(clean_fun(sentence))


LANG_CLEANER_MAP = {'fr': french_cleaner, 'en': english_cleaner}