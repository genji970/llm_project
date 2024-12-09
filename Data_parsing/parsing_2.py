import os
import logging
from parsing_1 import *

folder_name3 = '/content/parsing_output/'
os.makedirs(folder_name3, exist_ok=True)

if os.path.exists(folder_name3):
    logging.info(f"Output directory exists: {folder_name3}")
else:
    logging.error(f"Failed to create output directory: {folder_name3}")

# DataParsing Actor 생성
data_parsing = DataParsing.remote(folder_name2, folder_name3)

try:
    # PDF 파일 검색 및 개수 확인
    pdf_files = ray.get(data_parsing.pdf_search.remote())
    file_num = len(pdf_files)
    if file_num == 0:
        raise ValueError("No PDF files available for processing.")

    # 병렬 작업 수 결정
    task_count = min(file_num, 4)  # 최대 4개의 병렬 작업
    tasks = [data_parsing.pdf_parsing.remote() for _ in range(task_count)]

    # 결과 가져오기
    results = ray.get(tasks)
    print("Processing completed. Files saved:")

except ValueError as e:
    logging.error(f"Error during processing: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")