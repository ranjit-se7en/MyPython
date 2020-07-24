import pickle

# /*
# So what is pickling? Pickling is the serializing and de-serializing of python objects to a byte stream.
# Unpicking is the opposite.
#
# You may hear this methodology called serialization, marshalling or flattening in other languages,
# but it is pretty much exclusively referred to as pickling in Python. So what does pickling mean, simply?
#
# Pickling is used to store python objects. This means things like lists, dictionaries, class objects, and more.
#
# */


# words={1:"Who",2:"Are",3:"You"}
# with open("pickle_file.txt","wb") as pickle_file:
#     pickle.dump(words, pickle_file)

with open("pickle_file.txt","rb") as infile:
    print(pickle.load(infile))

