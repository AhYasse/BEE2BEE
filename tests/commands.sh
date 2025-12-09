1- Start Coordinator : C:/ProgramData/anaconda3/python.exe -m bee2bee coordinator --host 0.0.0.0 --port 8765
2- Start Node : C:/ProgramData/anaconda3/python.exe -m bee2bee node --coordinator "ws://127.0.0.1:8765" --name windows-node --price 0.01
3-Start Console : C:/ProgramData/anaconda3/python.exe -m bee2bee console
4- Start Test: C:/ProgramData/anaconda3/python.exe -m bee2bee test
