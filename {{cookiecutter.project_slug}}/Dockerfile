FROM python:3.10.6 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10.6
WORKDIR /{{cookiecutter.project_slug}}
COPY --from=requirements-stage /tmp/requirements.txt /{{cookiecutter.project_slug}}/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /{{cookiecutter.project_slug}}/requirements.txt
COPY {{cookiecutter.project_slug}} /{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}
CMD ["python", "-m", "{{cookiecutter.project_slug}}"]
