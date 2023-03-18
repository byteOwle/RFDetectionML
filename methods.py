from imports import *
global X, lbl,snrs,mods

def load_dataset(data):
    # Load the dataset ...
    #  You will need to seperately download or generate this file
    Xd = data
    # Xd = pickle.load(open("RML2016.10a_dict.pkl",'rb'))
    global snrs,mods,lbl,X
    X = []
    lbl = []
    snrs,mods= map(lambda j: sorted(list(set(map(lambda x: x[j], Xd.keys())))), [1,0])
    for mod in mods:
        for snr in snrs:
            X.append(Xd[(mod,snr)])
            for i in range(Xd[(mod,snr)].shape[0]):  lbl.append((mod,snr))
    X = np.vstack(X)
    return snrs, mods

def partition_data():
    # Partition the data
    #  into training and test sets of the form we can train/test on 
    #  while keeping SNR and Mod labels handy for each
    global X_train,X_test,Y_train,Y_test
    np.random.seed(2016)
    n_examples = X.shape[0]
    n_train = n_examples * 0.5
    train_idx = np.random.choice(range(0,int(n_examples)), size=int(n_train), replace=False)
    test_idx = list(set(range(0,n_examples))-set(train_idx))
    X_train = X[train_idx]
    X_test =  X[test_idx]
    def to_onehot(yy):
        yy1 = np.zeros([len(yy), max(yy)+1])
        yy1[np.arange(len(yy)),yy] = 1
        return yy1
    Y_train = to_onehot(list(map(lambda x: mods.index(lbl[x][0]), train_idx)))
    Y_test = to_onehot(list(map(lambda x: mods.index(lbl[x][0]), test_idx)))