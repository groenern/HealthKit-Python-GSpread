# HealthKit-Python-GSpread
 Uses python's GSpread Library and groenern's HealthKit implementation to upload workout data to google sheets. It is built using Python.
 
## Getting Started
### Prerequisites
- Python 3.x & Libraries (requirements.txt)
- Google Service Account
- JSON Google Credentials

### Google Service Account
Follow the gspread documentation [here](https://docs.gspread.org/en/latest/oauth2.html). You will need to create a project, enable API access, create a service account, and finally download the account's credentials. If you need help downloading the service key, read [here](https://cloud.google.com/iam/docs/keys-create-delete).

### Installation
1. Clone the repository: `git clone https://github.com/groenern/HealthKit-Python-GSpread.git`
2. Install dependencies: `pip install -r requirements.txt`

### Usage
 1. Export your HealthKit data from your iOS device as an XML file (instructions can be found [here](https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios) - Share your health and fitness data in XML format)
 2. Create Google Service Account and download an API Key
 3. Edit the config.ini to fit your information
 4. Place the export.xml and credentials.json file in the same directory as exportHK.py (or use absolute paths)
 5. Run the Python script `python hkExport.py export.xml"

## Sample Output
![SampleOutput](https://user-images.githubusercontent.com/130081417/231248573-fe391dd4-5c11-4c7c-b109-2a847e89b1e9.png)
