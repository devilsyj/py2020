from xml.etree import ElementTree as ET
xmlfile = r'/Users/devilsyj/Desktop/pytest/test.xml'
tree = ET.parse(xmlfile)
root = tree.getroot()
print root
list(root)