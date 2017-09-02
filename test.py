import re
from eng_rules import hybrid_g2p

regex_ = re.compile("[^A-Za-z0-9 ,.?\-']+")
with open("brown_nolines.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    lines = [l for l in lines if l != "" and l[0] != "#"]
    lines = [regex_.sub("", l).upper() for l in lines]

for n, l in enumerate(lines):
    print("Testing line {} of the Brown Corpus".format(n))
    try:
        hybrid_g2p(l)
    except:
        from IPython import embed; embed(); raise ValueError()
