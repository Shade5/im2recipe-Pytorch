import lmdb
import pickle


env = lmdb.open('data/test_lmdb', max_readers=1, readonly=True, lock=False, readahead=False, meminit=False)
with open('data/test_keys.pkl', 'rb') as f:
	ids = pickle.load(f)

with env.begin(write=False) as txn:
	serialized_sample = txn.get(ids[0].encode())
	sample = pickle.loads(serialized_sample, encoding='latin1')

pass

