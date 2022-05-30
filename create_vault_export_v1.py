"""
Author: nicolas.trejo@feverup.com
Date: 2022/05/20
"""

import time

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

def create_mail_account_all_data_export(service, matter_id, user_email, query_terms=''):
    """
    Create an email export for the user user_email
    """
    emails_to_search = [user_email]
    mail_query_options = {'excludeDrafts': False}
    mail_query = {
        'corpus': 'MAIL',
        'dataScope': 'ALL_DATA',
        'searchMethod': 'ACCOUNT',
        'accountInfo': {
            'emails': emails_to_search
        },
        'terms': query_terms,
        'mailOptions': mail_query_options,
    }
    mail_export_options = {
        'exportFormat': 'MBOX',
        'showConfidentialModeContent': True,
        'useNewExport': True
    }
    wanted_export = {
        'name': user_email,
        'query': mail_query,
        'exportOptions': {
            'mailOptions': mail_export_options
        }
    }
    return service.matters().exports().create(
        matterId=matter_id, body=wanted_export).execute()


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES,
    subject=ADMIN_ACCOUNT
)

service = build('vault', 'v1', credentials=creds)

########
# MODE 1: users are entered in the code
########

users = ['list',
         'of',
         'users'
        ]

new_exports=[]

for user in users:
    try:
        export = create_mail_account_all_data_export(service, MATTER_ID, user)
        new_exports.append(export)
        print('export:',user)
        time.sleep(20)
    except Exception as e:
        print('ERROR: ', user)
        time.sleep(20)

service.close()


########
# MODE 2: users are during execution by the user
########

service = build('vault', 'v1', credentials=creds)


while True:
    user = input('Enter a user email to create an export: ')  # eg: marisa.bringas@feverup.com
    export = create_mail_account_all_data_export(service, MATTER_ID, user)
    new_exports.append(export)
    time.sleep(20)
    repeat = input('Do you want to continue? (y/n)')
    if repeat.upper() in ['Y', 'YES', 'S', 'SI']:
        continue
    break

service.close()

print('\nTotal exports created:', len(exports))
print('End of program')