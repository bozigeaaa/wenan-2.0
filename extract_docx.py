import zipfile
import xml.etree.ElementTree as ET
import os

docx_path = "knowledge/K系列设计文稿.docx"
txt_path = "knowledge/K系列设计文稿_extracted.txt"

if not os.path.exists(docx_path):
    print(f"Error: {docx_path} does not exist.")
    exit(1)

try:
    with zipfile.ZipFile(docx_path) as docx:
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        # XML namespace for Word
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        paragraphs = []
        for para in root.findall('.//w:p', ns):
            text_elems = para.findall('.//w:t', ns)
            if text_elems:
                text = "".join([node.text for node in text_elems])
                paragraphs.append(text)
                
        with open(txt_path, 'w', encoding='utf-8') as f:
            for p in paragraphs:
                f.write(p + '\n')
        print(f"Successfully extracted {len(paragraphs)} paragraphs to {txt_path}.")
except Exception as e:
    print(f"Error: {e}")
