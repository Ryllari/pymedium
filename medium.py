import requests
import xml.etree.ElementTree as ET


page = requests.get("https://medium.com/feed/{blogname}")
xml = ET.fromstring(page.content)

my_list = [item for item in xml[0] if item.tag == 'item'][:5]
tlp = ()
for item in my_list:
    dct = {}
    for child in item:
        if 'creator' in child.tag:
            dct['creator'] = child.text
        if 'encoded' in child.tag:
            dct['content'] = child.text
        else:
            dct[child.tag] = child.text
    tlp += (dct,)


for item in tlp:
    print(item['title'])
    print(item['creator'])
    print(item['pubDate'])
    print(item['link'])
    print(item['content'][:500],"...")
    print('\n----------\n')
