import os
from redis import Redis

def connect_to_redis():
    # El host 'redis' coincide con el nombre del servicio en el YAML
    redis_uri = os.getenv("DATABASE_URI", "redis://localhost:6379")
    connection = Redis.from_url(redis_uri)
    return connection.ping()

if __name__ == "__main__":
    print(f"Conectado a Redis: {connect_to_redis()}")
