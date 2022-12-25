#!/bin/bash
echo "Updating bot repo"
git pull
. ../env/bin/activate

echo "Updating core repo"
cd ./transmission_remote_core && git pull && cd ..

echo "Running bot"
python3 main.py

