FROM tfm:1.0

COPY /app /app

RUN rm /app/.env*

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
