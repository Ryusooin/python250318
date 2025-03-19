import os
import shutil

# 다운로드 폴더 경로
download_folder = r"C:\Users\trueb\Downloads"

# 파일 이동 대상 폴더
folders = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

# 각 폴더에 대해 작업 수행
for folder_name, patterns in folders.items():
    # 대상 폴더 경로
    target_folder = os.path.join(download_folder, folder_name)
    
    # 폴더가 없으면 생성
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    # 각 패턴에 대해 파일 이동
    for pattern in patterns:
        for file_path in glob.glob(os.path.join(download_folder, pattern)):
            try:
                shutil.move(file_path, target_folder)
                print(f"Moved: {file_path} -> {target_folder}")
            except Exception as e:
                print(f"Error moving {file_path}: {e}")