FROM vovatest/bottlesimple

COPY ./ /app

cmd python login.py
