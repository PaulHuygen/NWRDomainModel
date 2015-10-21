from KafNafParserPy import *
import os
import sys

def get_entity_terms(entity):
    for ref in entity.get_references():
        terms=ref.get_span().get_span_ids()
        return terms


def get_terms_mention(parser, terms):
    term_text=[]
    sent=-1
    for t in terms:
        term=parser.get_term(t)
        target_ids=term.get_span().get_span_ids()
        for tid in target_ids:
            word=parser.get_token(tid).get_text()
            if sent==-1:
                sent=int(parser.get_token(tid).get_sent())
            term_text.append(word)
    res=(" ").join(term_text)
    return res, sent

def get_entity_mention(parser, entity):
    terms=get_entity_terms(entity)
    return get_terms_mention(parser, terms)

if __name__=="__main__":
    tokens=0
    links=0
    entities=0
    types=0
    t_array=[]
    path="/Users/filipilievski/Gold/" + sys.argv[1] + "/"
    for root, dirs, files in os.walk(path):
        for filename in files:
            f=root + "/" + filename
            parser=KafNafParser(f)
	    for token in parser.get_tokens():
		tokens+=1
            for entity in parser.get_entities():
                mention, sent = get_entity_mention(parser, entity)
                if sent<=6:
		    entities+=1
		    if entity.get_type() not in t_array:
			types+=1
			t_array.append(entity.get_type())
                    for extref in entity.get_external_references():
                        if extref.get_reference() and extref.get_reference()!="None":
				links+=1
    print tokens, entities, links, types, t_array
                    
