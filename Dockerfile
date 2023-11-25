#
FROM python:3.10

#
WORKDIR /infra_project_api


#
COPY ./requirements.txt /infra_project_api/requirements.txt
COPY ./routers/* /infra_project_api/routers/
COPY ./models/* /infra_project_api/models/
COPY ./services/* /infra_project_api/services/
COPY ./database.py  /infra_project_api/
COPY ./main.py /infra_project_api/

#
RUN pip install --no-cache-dir --upgrade -r /infra_project_api/requirements.txt

#
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]