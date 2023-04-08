FROM python:3.10.0-alpine 


CMD echo "Welcome to ATLAS"

COPY main.py app/main.py
run pip install flask
CMD python app/main.py