import glob
#print(glob.glob("*.py")) #현재 디렉토리의 모든 .py 파일
for item in glob.glob("*.py"):
    print(item)

