import matplotlib.pyplot as plt
from collections import Counter


dna = "adcgadcgadcgadcgadcg"

def get_freq(s, k):
    counts = Counter(s[i:i+k] for i in range(len(s)-k+1))
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

r1 = get_freq(dna, 1)
r2 = get_freq(dna, 2)
r3 = get_freq(dna, 3)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].bar(r1.keys(), r1.values())
axes[0].set_title('1-letter')

axes[1].bar(r2.keys(), r2.values())
axes[1].set_title('2-letter')

axes[2].bar(r3.keys(), r3.values())
axes[2].set_title('3-letter')

for ax in axes:
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()