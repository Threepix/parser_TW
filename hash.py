import hashlib
import random
import string
from threading import Thread
import time

hash_1 = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad"
hash_2 = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"
hash_3 = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def check_hash(hash):
    start_time=time.time()
    while True:
        res = generate_random_string(5)
        fun = hashlib.sha256(res.encode()).hexdigest()
        if fun == hash:
            print(res,(time.time()-start_time))
            break

th1 = Thread(target=check_hash,args=(hash_1,))
th1.start()
th2 = Thread(target=check_hash,args=(hash_2,))
th2.start()
th3 = Thread(target=check_hash,args=(hash_3,))
th3.start()

