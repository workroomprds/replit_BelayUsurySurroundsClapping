## for dumb debugging
from src import something

subject = something.Something()
print("<<<")
##print("dir(subject)")
##print(dir(subject))
##print(getattr(subject, "newThing", None))
from pprint import pprint

pprint(dir(subject))
print(">>>")
