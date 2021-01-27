import redis

redis_conn = redis.Redis()  # b'Vinay'
redis_conn = redis.Redis(decode_responses=True)  # 'Vinay'
print(redis_conn)
redis_conn.set("name", "Vinay")
print(redis_conn.get("name"))
