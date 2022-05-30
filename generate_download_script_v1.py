"""
Author: nicolas.trejo@feverup.com
Date: 2022/05/20
"""

from google.oauth2 import service_account
from googleapiclient.discovery import build

ADMIN_ACCOUNT = 'admin-accoutn-email'  # NEED TO BE REPLACED TO YOUR OWN
MATTER_ID = 'mater-id-identificator'  # NEED TO BE REPLACED TO YOUR OWN
SERVICE_ACCOUNT_FILE = 'json-with-service-account-credentials'  # NEED TO BE REPLACED TO YOUR OWN
SCOPES = [
    'https://www.googleapis.com/auth/ediscovery',
    'https://www.googleapis.com/auth/ediscovery.readonly'
]

# Service account has to be granted permissions

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES,
    subject=ADMIN_ACCOUNT
)

service = build('vault', 'v1', credentials=creds)

# List 50 exports
exports = service.matters().exports().list(matterId=MATTER_ID).execute()
service.close()

commands = []
users = []

for export in exports['exports']:
    if export['status'] != 'COMPLETED':
        print('Unfinished', export['name'])
        continue
    # we will compose the linux command
    print('\t\t\t', export['name'])
    command = 'echo "############################################################"'
    command += '\n'
    command += 'echo "##  Starting with user: "'
    command += export['name']
    command += '\n'
    command += 'echo'
    command += '\n'
    command += "mkdir ~/bucket/"
    command += export['name']
    command += '\n'
    command += 'cd ~/bucket/'
    command += export['name']
    command += '\n'
    for bucket in export['cloudStorageSink']['files']:
        command += 'gsutil cp gs://' + bucket['bucketName'] + '/' + bucket['objectName'] + ' .'
        command += '\n'
        command += 'sleep 3'
        command += '\n'
    command += 'cd ~'
    command += '\n'
    command += 'sleep 10'
    command += '\n'
    command += '\n'
    commands.append(command)
    users.append(export['name'])

"""
for elem in commands:
    print('\n')
    print(elem)

for export in exports['exports']:
    print(export['stats']['sizeInBytes'])
"""

command_file = open("download_exports.sh", "w")
n = command_file.write('\n'.join(commands))
command_file.close()

# Execute with bash using:
# nohup ./download_exports.sh >> /home/fever/result_download_exports.txt 2>&1&
