# NWR Domain Model

## Dependencies

* Python libraries: os, json, sys
* Clone dbpediaEnquirerPy from https://github.com/rubenIzquierdo/dbpediaEnquirerPy
* Clone KafNafParserPy from https://github.com/cltl/KafNafParserPy
* Dictionary file for lemma-to-entity information from https://www.dropbox.com/s/rl6ypazj2a9wnt5/lemma.json?dl=0

In the current version, dependencies 2-4 need to be placed in the root folder of NWRDomainModel directory, on the same level with the script "domain_model.py".

Note:
- You need to install dbpediaEnquirerPy dependencies: in the folder dbpediaEnquiererPy run: . install_dependencies.sh
- Make sure the dictionary file is called lemma.json: e.g. from the NWRDomainModel directory, run: wget -O lemma.json https://www.dropbox.com/s/rl6ypazj2a9wnt5/lemma.json?dl=1

## How to run

cat inputfile | python domain_model.py [dbpedia-endpoint] > outpufile

Currently, dbpedia-endpoint attribute allows optionally having a local endpoint instead of dbpedia remote one. Inputfile is an input NAF file. 
