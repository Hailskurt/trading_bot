FROM Python:3.7
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip install poetry
RUN poetry install
CMD ["python", "main.py"]