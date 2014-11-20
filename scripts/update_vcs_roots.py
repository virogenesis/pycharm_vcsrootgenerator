from xml.etree import ElementTree as ET
from lxml import etree
import os

from os.path import exists as path_exists, join as path_join

TYPE_GIT = "Git"
TYPE_MERCURIAL = "hg4idea"
vcs_types = {
    ".git" : TYPE_GIT,
    ".hg": TYPE_MERCURIAL,
}

MODULES_PATH = [".", ".env", "src"]
MODULES_DIRECTORY = path_join(*MODULES_PATH)
MODULES = {}
for dir in os.listdir(MODULES_DIRECTORY):
    module_dir = path_join(MODULES_DIRECTORY, dir)
    if not os.path.isdir(module_dir): continue
    vcs_type = set(os.listdir(module_dir)) & set(vcs_types.keys())
    if vcs_type:
        MODULES["/".join(["$PROJECT_DIR$"] + MODULES_PATH[1:] + [dir])] = {
            "vcs_type": vcs_types[vcs_type.pop()]
        }


def main():
    vcs_xml = path_join(".", ".idea", "vcs.xml")
    tree = etree.parse(vcs_xml)
    vcs_component = tree.xpath("./component")[0]
    vcs_roots = vcs_component.getchildren()

    intersect = set(MODULES.keys()) - set([_.attrib['directory'] for _ in vcs_roots])

    for project_path in intersect:
        module = MODULES[project_path]
        ET.SubElement(vcs_component, "mapping", {
            "directory": project_path,
            "vcs": module['vcs_type']
        })
        print "Added VCS ROOT: %s [%s]"%(project_path, module['vcs_type'])

    fh = open(vcs_xml, "w")
    fh.write(etree.tostring(tree, pretty_print=True))



if __name__ == "__main__":
	main()