FROM python:3.8.6-buster

RUN apt update
RUN pip install --upgrade pip setuptools wheel six pytest numpy cython pandas==1.2.3

# Copy code files
COPY requirements.txt ./

# Install requirements
RUN pip install -r requirements.txt -t .

# Copy code files
COPY src ./src

# Execute code
ENTRYPOINT ["python", "-m", "src"]
