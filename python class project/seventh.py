import dropbox
class TransferData:
 def __init__(self, access_token):
        self.access_token = access_token

 def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
def main():
    access_token = 'sl.BJiqSd_JdtE19KdOU6qPbMYQOWIKLII6QslfZm9kGsPAkcoqSbrCMFVnF9ROHpGQRLC7gGZIrfKAt2QJTrIiFOzP80A2d9nopbntMuJS8cPUoe1XmDVVr-_TH9Iq341fxzf8q6M76-k'
    transferData = TransferData(access_token)

    file_from = input('enter the file path to transfer')
    file_to = input('eter the full path to dropbox')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('file has been moved')

main()
