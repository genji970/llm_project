# llm_project
project covers from data_preparation ~ inference

## used language, tool .. ##
python , ray , spark , 

## sample used ##
In this project, I used pdf named "attention is all you need". This paper is famous in ai field.
authors : "Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin"

## Data_stage ##
1) pdf foldes in local + url -> data_processing -> input

2) Data_stage consists of makerfile(not yet) , requirements.txt(not yet) , data_ready.py , data_concat.py, data_processing.py

3) sample result :
"Page 2:
1
Introduction
Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks
in particular, have been firmly established as state of the art approaches in sequence modeling and"

program returns json file from pdf file without no errors. 

## Models build ##

## inference ##
