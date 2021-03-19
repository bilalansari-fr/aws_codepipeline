FROM public.ecr.aws/lambda/python:3.8

RUN yum install -y python3 python3-pip

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/scraper

WORKDIR /tmp/scraper

# You can overwrite command in `serverless.yml` template
CMD ["app.handler"]
