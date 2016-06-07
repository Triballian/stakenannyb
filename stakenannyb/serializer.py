import pickle

def serialize(obj, file):
    with open(file, 'bw') as f:
        pickle.dump(obj, f)

def deserialize(file):
    with open(file, 'br') as f:
        o = pickle.load(f)
    return o
    
    
    
    