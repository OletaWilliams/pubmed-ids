#Necessary imports
import pandas as pd
import csv 
from Bio import Entrez
import xml.etree.ElementTree as ET
import time
import os

def fetch_abstract(pmid):
    Entrez.email = 'EMAIL_ADDRESS'
    Entrez.api_key = 'NCBI_API_KEY'
    
    retry_count = 3  # Number of attempts
    delay = 3  # Delay between attempts in seconds
    
    for attempt in range(retry_count):
        try:
            if pd.isna(pmid) or pmid == '':
                return 'PMID is NaN or empty'

            handle = Entrez.efetch(db='PubMed', id=pmid, rettype='xml', retmode='xml')
            xml_data = handle.read()
            handle.close()

            # parsing XML data
            root = ET.fromstring(xml_data)

            # Extract abstracts - loop through abstract text element
            abstract = ''
            for abstract_text in root.findall(".//AbstractText"):
                if abstract_text.text:
                    abstract += abstract_text.text

            return abstract if abstract else 'abstract not available'
        
        except Exception as e:
            print(f"Error fetching abstract for {pmid} on attempt {attempt + 1}: {e}")
            if attempt < retry_count - 1:  # If not the last attempt
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                return f"Error fetching abstract for {pmid}: {e}"

#Function to write to text.
def write_to_textfile(output_file, pmid, title, abstract_data):
    """Appends the PMID, title, and abstract to a text file."""
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(f"PMID: {pmid}\n")
        file.write(f"Title: {title}\n")
        file.write(f"Abstract: {abstract_data}\n")
        file.write("="*50 + "\n")  # Divider between records

def pubmed_abstracts(input_csv):
    output_file = 'CSV_FILE_PATH' #File that you want to write to.
    
    # Read the input CSV
    with open(input_csv, mode='r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
    
    for row in data:
        if row['pmid']:
            pmid = str(int(row['pmid']))  # Convert the PMID to a string
            title = row['title']          # Get the title (adjust column name if necessary)
            
            # Fetch the abstract data
            abstract_data = fetch_abstract(pmid)
            
            # Write the data to the text file
            write_to_textfile(output_file, pmid, title, abstract_data)
    
    print(f"Abstracts fetched and saved to {output_file}")