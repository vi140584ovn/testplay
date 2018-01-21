FROM vovatest/bottlesimple

COPY ./ /app

cmd python /app/login.py
