FROM tfm:1.0

COPY /app /app

COPY /config /config

RUN rm /app/.env* && \
    mv /config/config-compose.json /config/config.json

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "30"]
