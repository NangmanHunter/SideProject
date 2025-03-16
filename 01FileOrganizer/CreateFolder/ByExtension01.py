import os
import shutil

def create_folders_by_extension(directory):
    if not os.path.exists(directory):
        print("지정된 디렉터리가 존재하지 않습니다.")
        return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):  # 파일인지 확인
            ext = os.path.splitext(file)[-1]
            if ext:  # 확장자가 있으면 폴더 생성
                ext_folder = os.path.join(directory, ext[1:])  # 확장자명으로 폴더 생성
                os.makedirs(ext_folder, exist_ok=True)  # 폴더가 없으면 생성

                new_path = os.path.join(ext_folder, file)  # 이동할 경로
                shutil.move(file_path, new_path)  
                print(f"파일 이동: {file} → {new_path}")  # 이동된 파일 확인

create_folders_by_extension(r"C:\github-nangmanhunter\test\폴더1")  


