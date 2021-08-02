FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
COPY . /app
EXPOSE 5001
ENTRYPOINT ["uvicorn", "Serve:app","--host", "0.0.0.0" , "--port", "5001", "--reload"]
