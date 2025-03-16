import os
import shutil

def create_folders_by_extension(directory):
    if not os.path.exists(directory):
        print("지정된 디렉터리가 존재하지 않습니다.")
        return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):  
            ext = os.path.splitext(file)[-1].lower()  
            if ext:  
                ext_folder = os.path.join(directory, ext[1:])  
                os.makedirs(ext_folder, exist_ok=True)  

                new_path = os.path.join(ext_folder, file)  
                shutil.move(file_path, new_path)  
                print(f"파일 이동: {file} → {new_path}")  

create_folders_by_extension(r"C:\github-nangmanhunter\test\폴더1")  

'''
대소문자
ㄴ비구분
ㄴ.lower()
'''