import xml.etree.ElementTree as ET
data_tree = ET.parse("./parentChild.xml")
data_root = data_tree.getroot()
print(data_root.tag)


for name in data_root.findall("./child/PLACES/place/place/place/name/[id='3344444']"):
    print(name.attrib.text())
    f = open("output.txt", "a")
    f.write(name.attrib.text())
    f.close()

for name in data_root.findall("./child/PLACES/place/place/place/name/[id='7788888']"):
    print(name.attrib.text())
    f = open("output.txt", "a")
    f.write(name.attrib.text())
    f.close()

for name in data_root.findall("./child/PLACES/place/place/place/name/[id='4444444']"):
    print(name.attrib.text())
    f = open("output.txt", "a")
    f.write(name.attrib.text())
    f.close()

for name in data_root.findall("./child/PLACES/place/place/place/name/[id='8888888']"):
    print(name.attrib.text())
    f = open("output.txt", "a")
    f.write(name.attrib.text())
    f.close()
