FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN mkdir /backend
#WORKDIR /backend
COPY ./app /app/app
COPY requirements.txt /app/requirements.txt
#COPY requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt
#COPY . .
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]