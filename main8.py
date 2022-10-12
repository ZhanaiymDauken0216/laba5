resume = ["Dauken", "Zhanaiym", "87074870328", "SU", "Computer scince"]
print("Lastname:", resume[0], "\nName:", resume[1], "\nPhone:", resume[2], "\nUniversity:", resume[3], "\nSpeciality:", resume[4])

resume.append(20)
print("\n", resume)

resumesecond = ["1.06.2002", "020616600213"]
resume.extend(resumesecond)
print("\n", resume)

x = "87074870328"
resume.insert(2, x)
print("\n", resume)

resume.pop(5)
print("\n", resume)

resume.reverse()
print("\n", resume)

resume.clear()
print("\n", resume)