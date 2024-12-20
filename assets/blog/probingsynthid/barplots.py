import matplotlib.pyplot as plt

spoofing = [0.81, 0.82, 0.15, 0.09, 0.04, 0.15, 0.05]
scrubbing = [0.02, 0.26, 0.91, 0.98, 0.98, 0.95, 1.00]
scrubbing_us = [0.90, 0.85, 0.98, 1.00, 0.99, 1.00, 1.00]
labels = [
    "SelfHash h=4",
    "LeftHash h=3",
    "LeftHash h=4",
    "SynthID (no cache)",
    "SynthID",
    "SynthID (n=90k)",
    "SynthID (n=90k, BD)",
]
transitions = [
    "",
    "Increase context size",
    "Add tournament sampling",
    "Add caching",
    "Increase attacker budget 3x",
    "Use Bayesian detector",
]

# barplot of spoofing
plt.figure(figsize=(18, 8))
plt.bar(labels, spoofing, color="#aa8dd8")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylabel("Spoofing Success (FPR*@1e-3)", fontsize=18)
plt.ylim(0, 1.05)
plt.gca().yaxis.set_label_coords(-0.04, 0.5)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)
plt.savefig("spoofing.pdf", bbox_inches="tight")

plt.clf()
plt.figure(figsize=(18, 8))
plt.bar(labels, scrubbing_us, color="#aa8dd8")
plt.bar(labels, scrubbing, color="#606060")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylabel("Scrubbing Success (FNR*@1e-3)", fontsize=18)
plt.ylim(0, 1.05)
plt.gca().yaxis.set_label_coords(-0.04, 0.5)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)
plt.savefig("scrubbing.pdf", bbox_inches="tight")
# raleway font

# remove spines
