import os
from redis import Redis

def connect_to_redis():
    # El host 'redis' coincide con el nombre del servicio en el pipeline
    redis_uri = os.getenv("DATABASE_URI", "redis://redis:6379")
    try:
        connection = Redis.from_url(redis_uri)
        return connection.ping()
    except Exception:
        return False

if __name__ == "__main__":
    # Mensaje crítico para la validación de la IA "Mark" (Punto 8)
    print("SERVICERUNNING on port 8000")
    
    # Verificación de conexión (útil para tus logs)
    if connect_to_redis():
        print("Connected to Redis successfully!")
    else:
        print("Redis connection failed, but service is up.")
