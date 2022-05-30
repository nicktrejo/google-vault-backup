# google-vault-backup
Backup process for user emails in Google Workspace using Vault


The process is as follows:

1. `create_vault_export_v1.py` : creates the Vault exports for each offboarding user.
2. `generate_download_script_v1.py` : generates a bash file with the commands to organise and download all the files (info is extracted from the COMPLETED exports). There is an example of the bash file `example_download_exports.sh`


Beware that you need to set up permissions on Google Workspace and your GCP project


Some documentation that may be worth reading:

- [Google Vault API - reference](https://developers.google.com/vault/reference/rest)
- [google-api-python-client](https://github.com/googleapis/google-api-python-client)
