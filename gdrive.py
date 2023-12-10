from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io

# Path to your service account key file
SERVICE_ACCOUNT_FILE = '/home/jackiee/vin/gdrive.json'

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/drive']

# The ID of your file on Google Drive
FILE_ID = '16pM3uJWid1cV7F3crjyYL8mh3pL3vJMTR99A5Q5LCVc'

# The path to save the downloaded file
MIME_TYPE = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
EXPORT_FORMAT = 'docx'  # Change this to the desired export format
OUTPUT_FILE = f'output_file.{EXPORT_FORMAT}'

def main():
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('drive', 'v3', credentials=credentials)

    request = service.files().get_media(fileId=FILE_ID)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f'Download {int(status.progress() * 100)}%.')

    with open(OUTPUT_FILE, 'wb') as f:
        f.write(fh.getvalue())

if __name__ == '__main__':
    main()
