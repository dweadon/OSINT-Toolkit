# OSINT Toolkit

A lightweight OSINT toolkit written in Python for gathering publicly available information from multiple online platforms.

## Features

 GitHub username enumeration
 Instagram profile checking
 Multi-platform scanning
 HTTP status analysis
 Simple CLI interface
 Modular architecture for future expansion

## Technologies

 Python
 HTTPX

## Supported Platforms

 GitHub
 Instagram
 X 
 TikTok 
 YouTube 

## Before installation:
```bash
sudo apt install python3-venv

python3 -m venv venv
source venv/bin/activate

pip install httpx
```


## Project Goals

This project focuses on:

 Username enumeration
 Public profile discovery
 OSINT workflow automation
 Multi-source intelligence gathering

## Installation

 1. Clone repository
Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
 2. Run the tool
python main.py
```bash
git clone git@github.com:dweadon/osint-toolkit.git
cd OSINT-Toolkit
python3 main.py
```
or if ssh doesn't work try:
```bash
git clone https://github.com/dweadon/OSINT-Toolkit.git
cd OSINT-Toolkit
pyhton3 main.py
```


## if an error like this appears:
```bash
Traceback (most recent call last):
  File "/home/deads/osint-toolkit/osint-toolkit/main.py", line 134, in <module>
    user = input("Enter username: ")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd1 in position 2: invalid continuation byte
```
try using:
```bash
PYTHONIOENCODING=utf-8 python3 main.py
```
or
```bash
export PYTHONIOENCODING=utf-8
python3 main.py
```
### MADE BY DWEADON
