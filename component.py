import xml.etree.ElementTree as ET

def parse_element(element):
    """Parse an XML element and return a dictionary."""
    parsed_element = {}

    # Add element attributes as nested fields
    for name, value in element.attrib.items():
        parsed_element[name] = value

    # Add element text content as a field, if it exists
    if element.text and element.text.strip():
        parsed_element['value'] = element.text.strip()

    # Add child elements to the dictionary
    for child in element:
        # If a child element has the same tag as a previous child element,
        # treat them as a list
        if child.tag in parsed_element:
            if type(parsed_element[child.tag]) is list:
                parsed_element[child.tag].append(parse_element(child))
            else:
                parsed_element[child.tag] = [parsed_element[child.tag], parse_element(child)]
        else:
            parsed_element[child.tag] = parse_element(child)

    return parsed_element





class Component:
    def __init__(self, filename='', data=None, parent=None, tag=None):
        self.p_data = {}
        if filename:
            tree = ET.parse(filename)
            root = tree.getroot()
            self.p_data = parse_element(root)
            data = self.p_data['rocket']
        #print(data)
        self.parent = parent
        self.tag = tag
        if isinstance(data, dict):
            self.data = {k: v for k, v in data.items() if k != 'subcomponents'}
            self.subcomponents = []
            if 'subcomponents' in data:
                for key in data['subcomponents']:
                    child_data = data['subcomponents'][key]
                    if isinstance(child_data, list):
                        for item in child_data:
                            self.subcomponents.append(Component(data=item, parent=self, tag=key))
                    else:
                        self.subcomponents.append(Component(data=child_data, parent=self, tag=key))
        else:
            self.data = {'value': data}
            self.subcomponents = []

            
    def to_xml(self, parent=None,filename=''):
        element = ET.Element(self.tag if self.tag else 'component')

        for key, value in self.data.items():
            if isinstance(value, dict) and 'value' in value:
                subelement = ET.SubElement(element, key)
                subelement.text = value['value']
            else:
                element.set(key, str(value))

        for subcomponent in self.subcomponents:
            subcomponent.to_xml(element)

        if parent is None:
            root = ET.Element('openrocket')
            root.set('version', self.p_data['version'])
            root.set('creator', self.p_data['creator'])
            ET.SubElement(root, 'simulations')
            ET.SubElement(root, 'photostudio')
            root.append(element)
            if filename:
                tree = ET.ElementTree(root)
                tree.write(filename, encoding='utf-8', xml_declaration=True)
            else:
                return ET.tostring(root, encoding='unicode')
        else:
            parent.append(element)

    def __getitem__(self, key):
        if key == 'subcomponents':
            return self.subcomponents
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        yield self
        for subcomponent in self.subcomponents:
            yield from subcomponent

    def __len__(self):
        return len(self.subcomponents)

    def __repr__(self):
        return f"Component({self.data.get('name', {}).get('value', '')})"