FROM python

WORKDIR /boilerplate_api

# Pip install
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy project files
COPY . .

#CMD ["python", "manage.py", "run"]
#CMD ["uwsgi", "--socket", "0.0.0.0:9090", --protocol=http -w manage:app]
CMD ["uwsgi", "--ini", "uwsgi.ini"]