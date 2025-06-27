import matplotlib.pyplot as plt
languages = ["Python", "Java"]
scores = {
    "Runtime Safety": [6, 9],    # JVM enforces stricter checks
    "SQLi Prevention": [7, 9],   # Java’s PreparedStatement is more foolproof
    "Tooling Support": [8, 7]    # Python has bandit, Java has FindSecBugs
}
for feature, values in scores.items():
    plt.bar(languages, values, label=feature)
plt.legend()
plt.title("Security Feature Comparison")
plt.savefig("security_comparison.png")