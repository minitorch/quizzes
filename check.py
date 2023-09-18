import glob, json, hashlib
import sys

salt = "pizzapizza"
all_correct = True
for f in glob.glob(f"{sys.argv[1]}.json"):
    them = json.load(open(f, "r"))
    them = list([{"answer": str(d["answer"])} for d in them])
    answer = hashlib.sha256((json.dumps(them) + salt).encode()).hexdigest()
    name = f[:-5]
    check = open(name + ".hash", "r").read()
    correct = answer.strip() == check.strip()
    print(name, "is correct" if correct else "is incorrect")
    all_correct = all_correct and correct

if all_correct:
    sys.exit(0)
else:
    sys.exit(1)
