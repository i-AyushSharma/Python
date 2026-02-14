import re

# pattern = "was"
# text = "Captain James Cook (7 November 1728 – 14 February 1779) was a British Royal Navy officer, explorer, and cartographer who led three voyages of exploration to the Pacific and Southern Oceans between 1768 and 1779. During these voyages, he sailed tens of thousands of miles across largely uncharted areas, mapping coastlines, islands, and features across the globe. He completed the first known circumnavigation of the main islands of New Zealand, and led the first recorded visit by Europeans to the east coast of Australia and the Hawaiian Islands. Renowned for exceptional seamanship and courage in times of danger, he was also a pioneer in the prevention of scurvy. In his three Pacific voyages, Cook encountered numerous indigenous peoples, many with little or no previous contact with Europeans, leading to violent encounters in which indigenous peoples and Cook's crew members were killed. Cook was killed in Hawaii in 1779, when a dispute with Native Hawaiians turned violent."
# match = re.search(pattern, text)
# print(match)

pattern = r"[A-Z]+ritish"
text = "Captain James Cook (7 November 1728 – 14 February 1779) was a British Royal Navy officer, explorer, and cartographer who led three voyages of exploration to the Pacific and Southern Oceans between 1768 and 1779. During these voyages, he sailed tens of thousands of miles across largely uncharted areas, mapping coastlines, islands, and features across the globe. He completed the first known circumnavigation of the main islands of New Zritish, and led the first recorded visit by Europeans to the east coast of Australia and the Hawaiian Islands. Renowned for exceptional seamanship and courage in times of danger, he was also a pioneer in the prevention of scurvy. In his three Pacific voyages, Cook encountered numerous indigenous peoples, many with little or no previous contact with Europeans, leading to violent encounters in which indigenous peoples and Cook's crew members were killed. Cook was killed in Hawaii in 1779, when a dispute with Native Hawaiians turned violent."
match = re.search(pattern, text)
print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])