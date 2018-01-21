FROM vovatest/bottlesimple

COPY ./ /app

cmd python login.py 2>/root/log
