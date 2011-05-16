import daservice, furiganaservice, jimservice, keyphraseservice, kouseiservice, maservice

MA_RESULT_MA = maservice.RESULT_MA
MA_RESULT_UNIQ = maservice.RESULT_UNIQ
MA_RESPONSE_SURFACE = maservice.RESPONSE_SURFACE
MA_RESPONSE_READING = maservice.RESPONSE_READING
MA_RESPONSE_POS = maservice.RESPONSE_POS
MA_RESPONSE_BASEFORM = maservice.RESPONSE_BASEFORM
MA_RESPONSE_FEATURE = maservice.RESPONSE_FEATURE
MA_FILTER_KEIYOUSHI = maservice.FILTER_KEIYOUSHI
MA_FILTER_KEIYOUDOUSHI = maservice.FILTER_KEIYOUDOUSHI
MA_FILTER_KANDOUSHI = maservice.FILTER_KANDOUSHI
MA_FILTER_FUKUSHI = maservice.FILTER_FUKUSHI
MA_FILTER_RENTAISHI = maservice.FILTER_RENTAISHI
MA_FILTER_SETSUZOKUSHI = maservice.FILTER_SETSUZOKUSHI
MA_FILTER_SETTOUJI = maservice.FILTER_SETTOUJI
MA_FILTER_SETSUBIJI = maservice.FILTER_SETSUBIJI
MA_FILTER_MEISHI = maservice.FILTER_MEISHI
MA_FILTER_DOUSHI = maservice.FILTER_DOUSHI
MA_FILTER_JOSHI = maservice.FILTER_JOSHI
MA_FILTER_JODOUSHI = maservice.FILTER_JODOUSHI
MA_FILTER_TOKUSHU = maservice.FILTER_TOKUSHU

JIM_FORMAT_ROMAN = jimservice.FORMAT_ROMAN
JIM_MODE_NORMAL = jimservice.MODE_NORMAL
JIM_MODE_ROMAN = jimservice.MODE_ROMAN
JIM_MODE_PREDICTIVE = jimservice.MODE_PREDICTIVE
JIM_RESPONSE_KATAKANA = jimservice.RESPONSE_KATAKANA
JIM_RESPONSE_HIRAGANA = jimservice.RESPONSE_HIRAGANA
JIM_RESPONSE_ALPHANUMERIC = jimservice.RESPONSE_ALPHANUMERIC
JIM_RESPONSE_HALF_KATAKANA = jimservice.RESPONSE_HALF_KATAKANA
JIM_RESPONSE_HALF_ALPHANUMERIC = jimservice.RESPONSE_HALF_ALPHANUMERIC
JIM_DICTIONARY_DEFAULT = jimservice.DICTIONARY_DEFAULT
JIM_DICTIONARY_NAME = jimservice.DICTIONARY_NAME
JIM_DICTIONARY_PLACE = jimservice.DICTIONARY_PLACE
JIM_DICTIONARY_ZIP = jimservice.DICTIONARY_ZIP
JIM_DICTIONARY_SYMBOL = jimservice.DICTIONARY_SYMBOL

KEYPHRASE_JSON_ORIGINAL = keyphraseservice.JSON_ORIGINAL
KEYPHRASE_JSON_LIBRALY = keyphraseservice.JSON_LIBRALY

KOUSEI_FILTER_GROUP_MISS = kouseiservice.FILTER_GROUP_MISS
KOUSEI_FILTER_GROUP_SIMPLIFY = kouseiservice.FILTER_GROUP_SIMPLIFY
KOUSEI_FILTER_GROUP_TO_BETTER = kouseiservice.FILTER_GROUP_TO_BETTER
KOUSEI_NO_FILTER_FALSE_CONVERSION = kouseiservice.NO_FILTER_FALSE_CONVERSION
KOUSEI_NO_FILTER_MISUSE = kouseiservice.NO_FILTER_MISUSE
KOUSEI_NO_FILTER_USE_ATTENTION = kouseiservice.NO_FILTER_USE_ATTENTION
KOUSEI_NO_FILTER_UNPLEASANT = kouseiservice.NO_FILTER_UNPLEASANT
KOUSEI_NO_FILTER_DEPENDENCE = kouseiservice.NO_FILTER_DEPENDENCE
KOUSEI_NO_FILTER_FOREIGN_PLACE = kouseiservice.NO_FILTER_FOREIGN_PLACE
KOUSEI_NO_FILTER_NAME = kouseiservice.NO_FILTER_NAME
KOUSEI_NO_FILTER_NOT_RA = kouseiservice.NO_FILTER_NOT_RA
KOUSEI_NO_FILTER_KANJI_OUTSIDE_THE_TABLE = kouseiservice.NO_FILTER_KANJI_OUTSIDE_THE_TABLE
KOUSEI_NO_FILTER_PHRASEOLOGY = kouseiservice.NO_FILTER_PHRASEOLOGY
KOUSEI_NO_FILTER_PARAPHRASE = kouseiservice.NO_FILTER_PARAPHRASE
KOUSEI_NO_FILTER_DOUBLE_NEGATION = kouseiservice.NO_FILTER_DOUBLE_NEGATION
KOUSEI_NO_FILTER_NOT_PARTICLE = kouseiservice.NO_FILTER_NOT_PARTICLE
KOUSEI_NO_FILTER_PLENASM = kouseiservice.NO_FILTER_PLENASM
KOUSEI_NO_FILTER_ABBREVIATION = kouseiservice.NO_FILTER_ABBREVIATION

class JLPAPIs(object):
    
    def __init__(self, appid, encoding=None):
        self.da = daservice.DAService(appid)
        self.furigana = furiganaservice.FuriganaService(appid)
        self.jim = jimservice.JIMService(appid)
        self.keyphrase = keyphraseservice.KeyphraseService(appid)
        self.kousei = kouseiservice.KouseiService(appid)
        self.ma = maservice.MAService(appid, encoding)

