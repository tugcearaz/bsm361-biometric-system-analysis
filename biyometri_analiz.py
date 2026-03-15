import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import combinations

# -------------------------
# 1. VERİYİ OKU
# -------------------------
data = np.load("Features.npz")
Features = data["Features"]

# ilk 100 kişi
Features = Features[:, :100, :]

# -------------------------
# 2. NORMALIZATION [0,1]
# -------------------------
min_val = Features.min()
max_val = Features.max()

Features_norm = (Features - min_val) / (max_val - min_val)

# -------------------------
# 3. SCORE FONKSİYONU
# -------------------------
def score(v1, v2):
    dist = euclidean(v1, v2)
    return 1 / (1 + dist)

# -------------------------
# 4. GENUINE SCORES
# (aynı kişi farklı zaman)
# -------------------------
genuine_scores = []

for person in range(100):
    vectors = Features_norm[:, person, :]
    
    for i, j in combinations(range(10), 2):
        s = score(vectors[i], vectors[j])
        genuine_scores.append(s)

genuine_scores = np.array(genuine_scores)

# -------------------------
# 5. IMPOSTER SCORES
# (farklı kişiler)
# -------------------------
imposter_scores = []

for time in range(10):
    for p1 in range(100):
        for p2 in range(p1+1, 100):
            v1 = Features_norm[time, p1]
            v2 = Features_norm[time, p2]
            s = score(v1, v2)
            imposter_scores.append(s)

imposter_scores = np.array(imposter_scores)

# -------------------------
# 6. SCORE DAĞILIMI
# -------------------------
plt.figure()
plt.hist(genuine_scores, bins=50, alpha=0.6, label="Genuine")
plt.hist(imposter_scores, bins=50, alpha=0.6, label="Imposter")
plt.legend()
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# 7. FAR ve FRR
# -------------------------
thresholds = np.linspace(0, 1, 500)

FAR = []
FRR = []

for t in thresholds:
    
    far = np.sum(imposter_scores >= t) / len(imposter_scores)
    frr = np.sum(genuine_scores < t) / len(genuine_scores)
    
    FAR.append(far)
    FRR.append(frr)

FAR = np.array(FAR)
FRR = np.array(FRR)

# -------------------------
# 8. EER
# -------------------------
diff = np.abs(FAR - FRR)
idx = np.argmin(diff)

EER = (FAR[idx] + FRR[idx]) / 2
eer_threshold = thresholds[idx]

print("EER:", EER)
print("Threshold:", eer_threshold)

# -------------------------
# 9. FAR & FRR vs Threshold
# -------------------------
plt.figure()
plt.plot(thresholds, FAR, label="FAR")
plt.plot(thresholds, FRR, label="FRR")
plt.scatter(eer_threshold, EER, label="EER")
plt.legend()
plt.xlabel("Threshold")
plt.ylabel("Error Rate")
plt.title("FAR & FRR vs Threshold")
plt.show()

# -------------------------
# 10. ROC (FAR vs FRR)
# -------------------------
plt.figure()
plt.plot(FAR, FRR)
plt.xlabel("FAR")
plt.ylabel("FRR")
plt.title("FAR vs FRR")
plt.show()