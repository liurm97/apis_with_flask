# import python3:11
FROM python:3.11

# define connection port
EXPOSE 5000

# define working directory = /app (app.py)
WORKDIR /app

# copy requirements.txt to the
COPY requirements.txt .

# run pip install command
RUN pip install -r requirements.txt

# copy all files from <src folder> to <dest folder = relative to WORKDIR>
COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]