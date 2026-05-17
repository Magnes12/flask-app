FROM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

COPY . /code


FROM python:3.10-alpine AS runner

WORKDIR /home/appadmin

RUN addgroup -g 1001 appgroup && \
    adduser -u 1001 -G appgroup -h /home/appadmin -s /bin/sh -D appadmin

COPY --from=builder --chown=appadmin:appgroup /root/.local /home/appadmin/.local
COPY --chown=appadmin:appgroup . .

ENV PATH=/home/appadmin/.local/bin:$PATH

USER appadmin

EXPOSE 5000
CMD ["python", "app.py"]