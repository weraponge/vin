from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io

# Rest of your code...


# Service account key file

SERVICE_ACCOUNT_FILE = '/home/jackiee/vin/gdrive.json'

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# The ID of your Google Doc
FILE_ID = '16pM3uJWid1cV7F3crjyYL8mh3pL3vJMTR99A5Q5LCVc'

# Export URL for Google Docs
MIME_TYPE = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
EXPORT_FORMAT = 'docx'  # Change this to the desired export format
OUTPUT_FILE = f'output_file.{EXPORT_FORMAT}'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)

request = service.files().export_media(fileId=FILE_ID, mimeType=MIME_TYPE)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)

done = False
while not done:
    status, done = downloader.next_chunk()
    print(f"Download {int(status.progress() * 100)}%.")

with open(OUTPUT_FILE, 'wb') as f:
    f.write(fh.getvalue())
