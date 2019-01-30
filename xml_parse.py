import collections
import sys
import xml.etree.ElementTree as ET


def count_prices(root, prices, level):
    color = root.attrib["color"]
    prices[color] += level
    for el in root.findall("cube"):
        count_prices(el, prices, level+1)


def main():
    xml_string = "".join(sys.stdin.readlines())
    prices = collections.Counter()  # "red","green", "blue"
    root = ET.fromstring(xml_string)
    count_prices(root, prices, 1)
    print(f"{prices['red']} {prices['green']} {prices['blue']}")


main()


example_xml = '''
<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
'''


def test_count_prices():
    prices = collections.Counter()  # "red","green", "blue"
    root = ET.fromstring(example_xml)
    count_prices(root, prices, 1)
    print(f"{prices['red']} {prices['green']} {prices['blue']}")
