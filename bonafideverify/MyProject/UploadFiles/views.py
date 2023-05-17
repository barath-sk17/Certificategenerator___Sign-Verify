import os
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from pathlib import Path
from django.shortcuts import render, redirect
from .forms import SignatureForm
from .forms import CreateForm
from .models import CreateFile,Signature
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication
from Crypto.PublicKey import RSA

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.
def hello(request):
    myform=SignatureForm()
    context={'form':myform}
    return render(request,"index.html",context)


def uploadfile(request):
    if request.method=="POST":
        check=SignatureForm(request.POST,request.FILES)
        if check.is_valid():
            #forms
            Roll = request.POST.get('studentroll')
            TextFile = request.FILES.get('text_file')
            KeyFile = request.FILES.get('public_file')
            SignatureFile = request.FILES.get('signature_file')

            Signature.objects.create(roll=Roll,text=TextFile,public=KeyFile,signature=SignatureFile).save()

            
            def decrypt():
                
                #read the public key
                with open(os.path.join(BASE_DIR / 'upload',"public.key"),"rb") as file:
                
                    public_key = RSA.import_key(file.read())

                #read the received signature and the received message
                
                with open(os.path.join(BASE_DIR / 'upload',Roll+".txt"),"rb") as file:
                    file_content = file.read()

                # Create a SHA256 hash object for the file content
                hash_obj = SHA256.new(file_content)


                with open(os.path.join(BASE_DIR / 'upload',"signature.pem"),"rb") as file:
                    signature = file.read()
                
                # Verify the signature
                verifier = pkcs1_15.new(public_key)
                try:
                    verifier.verify(hash_obj, signature)
                    messages.success(request,"The signature is valid. The message has not been changed.")
                    
                    file = [Roll+".txt","public.key","signature.pem"]

                    for i in file:
                        location = os.path.join(BASE_DIR / 'upload')
                        path = os.path.join(location, i)    
                        os.remove(path)

                except (ValueError, TypeError):
                    messages.error(request,"Invalid signature. The message may have been tampered with.")

                    file = [Roll+".txt","public.key","signature.pem"]

                    for i in file:
                        location = os.path.join(BASE_DIR / 'upload')
                        path = os.path.join(location, i)    
                        os.remove(path)


            decrypt()            


        else:
            messages.error(request,"Error Occurred!! Please verify the process")



        return redirect("hello")
        
# creating the certificate page
def home(request):
    create_form=CreateForm()
    context={'form':create_form}
    return render(request,"create.html",context)

# creating certificte
def createfile(request):
    if request.method=="POST":
        create_form=CreateForm(request.POST,request.POST)
        if create_form.is_valid():
            #forms
            Name = request.POST.get('name')
            Roll = request.POST.get('roll')
            
            def create():
                f1=open(os.path.join(BASE_DIR / 'sample',"Certificate.txt"),"r")
                line=f1.read()
                if "name" and "roll" in line:
                    l1=[Name,Roll]
                    l2=["name","roll"]
                    f2=open(os.path.join(BASE_DIR / 'certificate_generated',Roll+".txt"),"w")
                    for i in range(len(l1)):
                        line=line.replace(l2[i],l1[i])
                    f2.write(line)
                return Roll+".txt"

            file_created=create()

            #creating private and public key
            def create_key():
                key = RSA.generate(2048)

                # write public and private key to a file

                directory = Roll
                parent_dir = os.path.join(BASE_DIR / 'sample')
                path = os.path.join(parent_dir,directory)

                if os.path.exists(path):
                    print("Folder Already Exists!")
                else:
                    os.makedirs(path)

                private_key = key.export_key()
                parent = os.path.join(BASE_DIR / 'sample')
                folder = Roll
                path1 = os.path.join(parent,folder)

                with open(os.path.join(path1,"private.key"),"wb") as file:
                    file.write(private_key)

                public_key = key.publickey().export_key()
                with open(os.path.join(path1,"public.key"),"wb") as file:
                    file.write(public_key)
            create_key()


            def encrypt():

                parent = os.path.join(BASE_DIR / 'sample')
                folder = Roll
                path = os.path.join(parent,folder)

                #import private key
                with open(os.path.join(path,"private.key")) as file:
                    private_key = RSA.import_key(file.read())

                with open(os.path.join(BASE_DIR / 'certificate_generated',Roll+".txt"),"rb") as file:
                    file_content = file.read()
                
                #create a hash of the message
                hash_obj = SHA256.new(file_content)

                #sign the message
                signer = pkcs1_15.new(private_key)
                signature = signer.sign(hash_obj)
                
                #save signature
                with open(os.path.join(path,"signature.pem"),'wb') as file:
                    file.write(signature)

            encrypt()

            def send_mail(sender,receiver,file):   

                link_text = "Click here to execute the program"
                link_url = "http://127.0.0.1:8000/check/"
                link = f"<a href='{link_url}'>{link_text}</a>"
            
                email_body = f"Please click the following link to execute the program: {link}"

                msg = MIMEMultipart()
                
                m = f"""\
                Subject: Key details
                To: {receiver}
                From: {sender}\n\n"""

                msg.attach(MIMEText(m, 'plain'))
                msg.attach(MIMEText(email_body, "html"))

                parent = os.path.join(BASE_DIR / 'sample')
                folder = Roll
                path1 = os.path.join(parent,folder)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender, 'zpraumqsdfeyfhex')
                
                with open(os.path.join(BASE_DIR / 'certificate_generated',Roll+".txt"), 'rb') as f:
                    attach = MIMEApplication(f.read(), _subtype='txt')
                    attach.add_header('Content-Disposition', 'attachment', filename=file)
                    msg.attach(attach)
                
                with open(os.path.join(path1,"public.key"), 'rb') as f1:
                    attach = MIMEApplication(f1.read(), _subtype='txt')
                    attach.add_header('Content-Disposition', 'attachment', filename="public.key")
                    msg.attach(attach)

                with open(os.path.join(path1,"signature.pem"), 'rb') as f2:
                    attach = MIMEApplication(f2.read(), _subtype='txt')
                    attach.add_header('Content-Disposition', 'attachment', filename="signature.pem")
                    msg.attach(attach)

                text = msg.as_string()
                server.sendmail(sender,receiver, text)

                server.quit()

            sender = 'genztitans.641@gmail.com'
            receiver = '21pc06@psgtech.ac.in'
            send_mail(sender,receiver,file_created)


            CreateFile.objects.create(filename=Name,rollnumber=Roll).save()

            #messages.success(request,"File Created successfully.")

            #context={'some_string':sign1}
            #return render(request,"sign.html",context)
            return render(request,"sign.html")

        else:
            messages.error(request,"Error Occurred!! Please verify the process")



        return redirect("home")