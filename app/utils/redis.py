from redis.asyncio import Redis

from app.config.settings import get_settings

settings = get_settings()

redis_client = None

def create_redis_client():
    redis = Redis.from_url(
        settings.REDIS_URL,
        decode_responses=True,
        max_connections=10,
    )

    return redis


async def get_redis():
    global redis_client

    if redis_client is None:
        redis_client = create_redis_client()
    
    return redis_client


async def close_redis():
    global redis_client

    if redis_client is not None:
        await redis_client.close()
        await redis_client.connection_pool.disconnect()
        redis_client = None
