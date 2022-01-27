import dropbox

class TransferData:
    def __init__(self,password):
        self.password=password  
    
    def upload_file(self,file_to,file_path):
        dbx=dropbox.Dropbox(self.password)
        file1=open(file_path,'rb')
        readFile=file1.read()
        dbx.files_upload(file1.read(),file_to)

def main():
    password='sl.BAzaODsBZuCCQ5VFD995ohbVdFZrkH8-27cogudOxIEjyyZRFK1VFuWnrI2cerXXBqAekvI7JLCDOwItooLnans7ecTRJzhwhCISH59Z8SYCQIUsffuKWtTnfVQngLpSeqd0wt5zxOFt'
    file_from=input("Enter your file's path")
    file_to=input("Enter your file's path to upload to dropbox")
    object=TransferData(password) 
    object.upload_file(file_to,file_from)
main()
    

        

