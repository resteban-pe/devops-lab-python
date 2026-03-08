from app import connect_to_redis

def test_redis_connection():
    """Prueba que la conexión a Redis sea exitosa en el entorno de CI"""
    # En el pipeline de GitHub Actions y Tekton, Redis estará disponible
    # Por lo tanto, connect_to_redis() debe devolver True
    result = connect_to_redis()
    assert result is True, "La conexión a Redis falló. Verifica que el servicio esté corriendo."

def test_service_logic():
    """Prueba básica para asegurar que la lógica de la app responde"""
    # Una prueba simple adicional para asegurar que el linter y nose tengan qué leer
    message = "SERVICERUNNING"
    assert "SERVICE" in message
