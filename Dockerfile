FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY Users /code/

EXPOSE 80

CMD ["uvicorn", "UsersService:app", "--host", "0.0.0.0", "--port", "8000"]