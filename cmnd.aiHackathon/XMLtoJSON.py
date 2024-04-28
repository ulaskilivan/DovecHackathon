import requests
import xmltodict
import json

def convert_xml_to_json(url, output_file):
    # Fetch the XML content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    # Convert the XML to a dictionary
    xml_data = xmltodict.parse(response.content)

    # Convert the dictionary to JSON
    json_data = json.dumps(xml_data, indent=4)

    # Save the JSON to a file
    with open(output_file, 'w') as file:
        file.write(json_data)

# URL of the XML file
url = 'https://dovecconstruction.com/emlak.xml'

# Output JSON file name
output_file = 'output.json'

# Convert and save the XML to JSON
convert_xml_to_json(url, output_file)
