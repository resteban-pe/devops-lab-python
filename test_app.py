from app import connect_to_redis

def test_redis_connection():
    # Esta prueba llamará a la app y verificará la conexión con el servicio Redis del pipeline
    assert connect_to_redis() is True
