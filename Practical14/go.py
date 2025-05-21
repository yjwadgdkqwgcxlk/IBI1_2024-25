from xml.dom import minidom
import xml.sax
from datetime import datetime

# Pseudocode:
# - Parse the go_obo.xml file using both DOM and SAX methods.
# - For each <term> element:
#     - Extract the <id>, <name>, <namespace>, and count <is_a> elements.
#     - Track the term with the highest <is_a> count within each ontology category:
#       biological_process, molecular_function, cellular_component.
# - Print the term ID, name, and is_a count for each ontology.
# - Measure the time taken for both DOM and SAX parsing.
# - Print the execution time for each method.
# - Include a comment (in output and code) stating which method was faster.

file_path = r"D:\vscode\IBI_2024-25\IBI1_2024-25\Practical14\go_obo.xml"


def parse_with_dom(path):
    start_time = datetime.now()
    doc = minidom.parse(path)
    term_list = doc.getElementsByTagName("term")

    max_terms = {
        "biological_process": ["", "", 0],
        "molecular_function": ["", "", 0],
        "cellular_component": ["", "", 0]
    }

    for term in term_list:
        ns = term.getElementsByTagName("namespace")[0].firstChild.data
        term_id = term.getElementsByTagName("id")[0].firstChild.data
        term_name = term.getElementsByTagName("name")[0].firstChild.data
        is_a_list = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_list)

        if ns in max_terms and is_a_count > max_terms[ns][2]:
            max_terms[ns] = [term_id, term_name, is_a_count]

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print("\nDOM results:")
    for category in max_terms:
        t_id, t_name, count = max_terms[category]
        print(f"{category}: {t_name} ({t_id}) has {count} is_a relations.")
    print("DOM time:", elapsed, "seconds")
    return elapsed


class TermHandler(xml.sax.ContentHandler):
    # Handle each <term>: reset on start, track key fields, count <is_a>, update max on end.

    def __init__(self):
        self.results = {
            "biological_process": ["", "", 0],
            "molecular_function": ["", "", 0],
            "cellular_component": ["", "", 0]
        }
        self.reset_term()
        self.current_tag = ""

    def reset_term(self):
        self.term_id = ""
        self.term_name = ""
        self.namespace = ""
        self.is_a_count = 0
        self.in_term = False

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            self.reset_term()
            self.in_term = True

    def characters(self, content):
        if self.in_term:
            if self.current_tag == "id":
                self.term_id += content.strip()
            elif self.current_tag == "name":
                self.term_name += content.strip()
            elif self.current_tag == "namespace":
                self.namespace += content.strip()
            elif self.current_tag == "is_a":
                self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.results:
                if self.is_a_count > self.results[self.namespace][2]:
                    self.results[self.namespace] = [self.term_id, self.term_name, self.is_a_count]
            self.in_term = False


def parse_with_sax(path):
    start_time = datetime.now()
    handler = TermHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(path)
    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print("\nSAX results:")
    for category in handler.results:
        t_id, t_name, count = handler.results[category]
        print(f"{category}: {t_name} ({t_id}) has {count} is_a relations.")
    print("SAX time:", elapsed, "seconds")
    return elapsed


if __name__ == "__main__":
    dom_duration = parse_with_dom(file_path)
    sax_duration = parse_with_sax(file_path)

    # Compare and print faster method
    if sax_duration < dom_duration:
        print("\n# SAX was faster in this run.")
    else:
        print("\n# DOM was faster in this run.")

# Comment:
# In most cases, SAX performs slightly faster than DOM due to its event-driven nature,
# especially when processing large XML files without needing to load the entire tree into memory.
