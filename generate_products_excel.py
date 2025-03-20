import openpyxl
import random

# 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Products"

# 헤더 추가
headers = ["제품ID", "제품명", "수량", "가격"]
ws.append(headers)

# 샘플 데이터 생성
product_names = ["TV", "Laptop", "Smartphone", "Tablet", "Headphones", "Camera", "Printer", "Monitor", "Keyboard", "Mouse"]

for i in range(1, 101):  # 100개의 데이터 생성
    product_id = f"P{i:03d}"  # 제품ID (P001, P002, ...)
    product_name = random.choice(product_names)  # 랜덤 제품명
    quantity = random.randint(1, 50)  # 수량 (1~50)
    price = random.randint(100, 1000) * 10  # 가격 (1000~10000 단위)
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")
print("products.xlsx 파일이 생성되었습니다.")