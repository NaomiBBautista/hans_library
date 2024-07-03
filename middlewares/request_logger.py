from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import csv
import os
from datetime import datetime

class RequestLogger(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        root = os.path.join(os.getcwd(), 'request_logger.csv')
        
        data = [[request.method, request.url, response.status_code, datetime.now()]]
        if not os.path.exists(root):
            with open(root, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows([['Method', 'URL', 'Status Code', 'Date']])
        
        with open(root, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        return response