from lxml import etree

def validate_xml(xml_file, xsd_file):
    
    xml_doc = etree.parse(xml_file)
    schema = etree.XMLSchema(file=xsd_file)

   
    is_valid = schema.validate(xml_doc)

    
    if is_valid:
        print("XML document is valid.")
    else:
        print("XML document is not valid. Validation errors:")
        for error in schema.error_log:
            print(f"Line {error.line}, Column {error.column}: {error.message}")

if __name__ == "__main__":
    xml_file = "employees.xml"
    xsd_file = "employee_schema.xsd"
    validate_xml(xml_file, xsd_file)
