FROM python:3.11.2-slim-bullseye
# FROM python:3.7.16-slim-bullseye
COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /uvx /bin/
# see: https://docs.astral.sh/uv/guides/integration/docker/
ENV UV_LINK_MODE=copy
WORKDIR /workspace
COPY . /workspace
RUN uv sync --locked --no-cache
ENTRYPOINT [ "uv", "run", "--locked" ]
CMD ["invoke", "test.all"]
