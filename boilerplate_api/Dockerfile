FROM python

WORKDIR /boilerplate_api

# Pip install
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]