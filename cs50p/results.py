results = ["Mario", "Luigi"]

results.append("Toad")
results.append("Yoshi")
results.append("Princess Peach")

results.append(["Bowser", "Donkey Kong", "Wario"])
results.remove(["Bowser", "Donkey Kong", "Wario"])
results.extend(["Bowser", "Donkey Kong", "Wario"])

results.remove("Bowser")
results.insert(0, "Bowser")

results.reverse()

print(results)