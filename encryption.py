import os
os.chdir('C:\\Users\\Taru Sharma\\Documents\\Python\\CodVeda Intern')
file_name=input("Enter the file name to encrypt: ")
encrypted_sentence=''
with open(file_name,'r') as f:
    content=f.read()
with open(file_name,'r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        for ch in line:
            if ch=='z':
                encrypted_ch='a'
            elif ch=='Z':
                encrypted_ch='A'
            elif (not ch.isalpha()):
                encrypted_ch=ch
            else:
                encrypted_ch=chr(ord(ch)+1)
            encrypted_sentence+=encrypted_ch
with open('encrypted_file.txt','w') as f:
    f.write(encrypted_sentence)     
choice=input("Do you want to decrypt it back? (yes/no):")
if choice.lower()=='yes':
    with open('encrypted_file.txt','w') as f:
        f.write(content)          