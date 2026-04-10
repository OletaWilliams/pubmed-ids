## Abstract Retrieval Script

### Overview

This script automates the retrieval of article abstracts from PubMed using the NCBI Entrez API. It was developed to support literature searching and evidence synthesis workflows by reducing the need for manual abstract collection.

Given a CSV file containing PubMed IDs (PMIDs) and article titles, the script fetches the corresponding abstracts and writes them to an output file.

### Motivation

In evidence based research and health technology assessment workflows, large volumes of references are often screened and reviewed. Manually retrieving abstracts can be time consuming and error prone.

This script was created as a lightweight solution to:
- Automate abstract retrieval from PubMed
- Support structured review workflows
- Reduce repetitive manual effort

----

### Features
- Fetches abstracts using PubMed PMIDs
- Handles missing or invalid PMIDs gracefully
- Includes basic retry logic for API reliability
- Parses XML responses to extract abstract text
- Outputs results in a readable, structured text format

### Input Format

The script expects a CSV file with at least the following columns:
- pmid — PubMed ID
- title — Article title

_Example_:
```
pmid,title
12345678,Example Article Title
87654321,Another Article Title
```
### Output

The script writes results to a text file in the following format:

_Example_:
```
PMID: 12345678
Title: Example Article Title
Abstract: [abstract text]
```
----

### How to Run
1. Clone the repository
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Update the script with:
- Your email address (required by Entrez)
- Your NCBI API key (optional but recommended)
- Input and output file paths

4. Run the script:
```
python script_name.py
```
----
### Design Considerations

This script was initially developed as a time-constrained utility, with a focus on functionality and reliability.

Key design choices:
	•	Single PMID requests: Simpler implementation, but less efficient for large datasets
	•	Text file output: Chosen for readability and quick inspection
	•	Retry logic: Added to handle intermittent API/network issues
	•	XML parsing: Used to reliably extract abstract content from PubMed responses

Limitations
- Processes one PMID per request (not optimised for large-scale use)
- Output is unstructured text rather than machine readable format
- File paths and configuration are hardcoded
- Limited logging and monitoring

#### Future Improvements

Planned enhancements include:
- Support for batch PMID requests to improve performance
- Output in structured formats (CSV or JSON)
- External configuration (e.g. environment variables or config files)
- Improved logging for better traceability
- Refactoring for greater modularity and reuse

----
#### Tech Stack
- Python
- Biopython (Entrez module)
- XML parsing (xml.etree.ElementTree)

----
#### Author

Created by Oleta Williams with a background in information retrieval and health research.

----

:::

----
