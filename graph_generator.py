from xml.etree import ElementTree as ET

from graph_analyzer import create_graph_from_connection


class Connection:
    def __init__(self,source,target,connection_type):
        self.source = source
        self.target = target
        self.connection_type = connection_type


def generate_graph_from_code(xmi_path):
    parser = ET.iterparse(xmi_path+".xmi")
    connections = []
    for event, element in parser:
        if element.tag == "connector":
            connection_type = element.find("properties").get("ea_type")
            source = element.find("source").find("model").get("name")
            target = element.find("target").find("model").get("name")
            connections += [Connection(source, target, connection_type)]
    create_graph_from_connection(connections,xmi_path)


def main():
    print("*planning modules*")
    generate_graph_from_code("planning")
    print("*control modules*")
    generate_graph_from_code("control")


if __name__ == '__main__':
    main()
