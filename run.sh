nohup python -m gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8888 main:app &
