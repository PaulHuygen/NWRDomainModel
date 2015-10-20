from dbpediaEnquirerPy import *
from KafNafParserPy import *
import os
def get_entity_sent(filename, parser, entity):
    terms=[]
    for ref in entity.get_references():
        termbs=ref.get_span().get_span_ids()
	if len(termbs)==0:
		w.write(filename + "\t" + entity.get_id() + "\n")
		return 100
	print termbs, len(termbs)
	start=termbs[0]
	start_sent=parser.get_token(start).get_sent()
    	return start_sent

w=open("empty_spans.txt", "w")
w2=open("empty_files.txt", "w")

if __name__=="__main__":
	my_dbpedia = Cdbpedia_enquirer()
	path="/Users/filipilievski/annotations/"
	for root, dirs, files in os.walk(path):
        	for filename in files:
			print filename
            		if filename.endswith(".naf"):
				f=root + "/" + filename
				try:
					parser=KafNafParser(f)
				except:
					w2.write(filename + "\n")
					continue
				for entity in parser.get_entities():
					sent = get_entity_sent(filename, parser, entity)
					print sent
					if int(sent)<=6:
						print entity.get_type()
						ent_type=entity.get_type()
						if ent_type!="MISC" and ent_type.strip()!="":
						    if ent_type=="ORGANIZATION":
							ent_type="http://dbpedia.org/ontology/Organisation"
						    elif ent_type=="PERSON":
							ent_type="http://dbpedia.org/ontology/Person"
						    elif ent_type=="LOCATION":
							ent_type="http://dbpedia.org/ontology/Place"
						    for extref in entity.get_external_references():
							dblink=extref.get_reference()
							link_types=my_dbpedia.get_dbpedia_ontology_labels_for_dblink(dblink)
							print link_types
							print (ent_type in link_types)
