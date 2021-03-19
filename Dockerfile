FROM public.ecr.aws/lambda/python:3.8

RUN pip3 install --upgrade awscli

RUN pip install pandas

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/scraper

# You can overwrite command in `serverless.yml` template
CMD ["app.handler"]
