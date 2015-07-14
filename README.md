# NWR Domain Model

## Dependencies

* Python libraries: os, json, sys
* Clone dbpediaEnquirerPy from https://github.com/rubenIzquierdo/dbpediaEnquirerPy
* Clone KafNafParserPy from https://github.com/cltl/KafNafParserPy
* Dictionary file for lemma-to-entity information from https://www.dropbox.com/s/rl6ypazj2a9wnt5/lemma.json?dl=0

In the current version, dependencies 2-4 need to be placed in the root folder of NWRDomainModel directory, on the same level with the script "domain_model.py".

## How to run

python domain_model.py inputfile [dbpedia-endpoint]

Currently, dbpedia-endpoint attribute allows optionally having a local endpoint instead of dbpedia remote one. Inputfile is an input NAF file. The script creates an output file with a name:

outputfile = inputfile + ".out"
