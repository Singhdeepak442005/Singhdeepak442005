import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "Technology": ["HTML", "CSS", "Linux", "Bash", "Python", "GitHub"],
    "Proficiency": [60, 50, 70, 70, 60, 85]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(8,5))
barplot = sns.barplot(x="Technology", y="Proficiency", data=df, palette="muted")

for p in barplot.patches:
    barplot.annotate(f"{p.get_height()}%", 
                     (p.get_x() + p.get_width()/2., p.get_height()), 
                     ha="center", va="bottom", fontsize=10)

plt.title("Tech Stack Progress", fontsize=14, fontweight="bold")
plt.ylabel("Proficiency (%)")
plt.ylim(0, 100)

plt.savefig("scripts/tech_progress.png", dpi=300)
plt.close()
