import lmdb
import pickle


env = lmdb.open('data/test_lmdb', max_readers=1, readonly=True, lock=False, readahead=False, meminit=False)
with open('data/test_keys.pkl', 'rb') as f:
	ids = pickle.load(f)

ids = ['08d87a1983', 'd86247bb3b', '8eff33a35e', 'c98d265032', 'fca5e551be']

for id in ids:
	with env.begin(write=False) as txn:
		serialized_sample = txn.get(id.encode())
		sample = pickle.loads(serialized_sample, encoding='latin1')

		print(sample['imgs'][0]['id'])

