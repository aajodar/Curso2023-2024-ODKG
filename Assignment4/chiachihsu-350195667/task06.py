# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PflZyQaEPH4as8F_3jKWMUnbJXHrCOUb

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

# TO DO
# Visualize the results
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g.triples((ns.University,None,None)):
  print(s,p,o)
print(g.serialize(format="ttl"))

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
# Visualize the results
g.add((ns.Researcher, RDF.type, RDFS.Class))
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g.triples((None,None,ns.Person)):
  print(s,p,o)
print(g.serialize(format="ttl"))

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# TO DO
# Visualize the results
g.add((ns.JaneSmith, RDF.type, ns.Researcher))
for s, p, o in g.triples((None,None,ns.Researcher)):
  print(s,p,o)
print(g.serialize(format="ttl"))

"""**TASK 6.4: Add to the individual JaneSmith the email address, fullName, given and family names**"""

# TO DO
# Visualize the results
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.JaneSmith, vcard.EMAIL, Literal("JaneSmith@mail.com")))
g.add((ns.JaneSmith, vcard.FN, Literal("Jane Smith")))
g.add((ns.JaneSmith, vcard.Given, Literal("Jane")))
g.add((ns.JaneSmith, vcard.Family, Literal("Smith")))
for s, p, o in g.triples((ns.JaneSmith,None,None)):
  print(s,p,o)
print(g.serialize(format="ttl"))

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# TO DO
# Visualize the results

g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith, ns.workplace, ns.UPM ))

for s, p, o in g.triples((ns.JohnSmith,None,None)):
    print(s,p,o)
print(g.serialize(format="ttl"))

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary**"""

# TO DO
# Visualize the results
from rdflib import FOAF

g.add((ns.John, FOAF.knows, ns.Jane))

for s, p, o in g.triples((None,FOAF.knows,None)):
    print(s,p,o)
print(g.serialize(format="ttl"))