import os
import logging
import ray
import json

from data_concat import Data_Concat
from data_ready import Data_Ready
from data_processing import process_all_pdfs

#log config setting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("This is an info message.")

url = 'https://arxiv.org/pdf/1706.03762'
input_folder = 'C:/Users/Administrator/PycharmProjects/project/'
output_folder = 'C:/Users/Administrator/PycharmProjects/project/'

#data_concat
d = Data_Concat(url , input_folder , output_folder)
d.gather_files()

#data_ready
dd = Data_Ready(input_folder)
dd.data_ready

#data_processing
ray.init()
r = process_all_pdfs(input_folder , output_folder)

print(r)


