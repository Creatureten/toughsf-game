from burcat import Elementdb

db = Elementdb()
print(db.search("H2"))
hydrogen = db.getelementdata("H2  REF ELEMENT")
print(hydrogen.cp)
