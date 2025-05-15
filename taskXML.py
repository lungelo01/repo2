import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('movie.xml')
root = tree.getroot()

favourite_count = 0
non_favourite_count = 0

# Iterate through each <movie> element
for movie in root.iter('movie'):
    print("Child tags of <movie>:")
    for child in movie.iter():
        if child is not movie:  # Skip the <movie> tag itself
            print(f"  <{child.tag}>")

    # Print out the description using itertext()
    print("Description:")
    for text in movie.itertext():
        print(end="" f"{text.strip()}")

    # Count favourites and non-favourites
    fav = movie.attrib.get('favourite', '').lower()
    if fav == 'yes':
        favourite_count += 1
    else:
        non_favourite_count += 1

    print("-" * 30)

# Output the counts
print(f"Number of favourite movies: {favourite_count}")
print(f"Number of non-favourite movies: {non_favourite_count}")