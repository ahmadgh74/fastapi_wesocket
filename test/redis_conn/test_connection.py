from random import randint

import aiounittest

from redis_conn import RedisHandler

class TestRedisHandler(aiounittest.AsyncTestCase):

    async def test_set_and_get(self):
        redis = RedisHandler('redis://localhost')
        key = 'redis_key'
        value = f'redis_value_{randint(1, 1000)}'
        await redis.set(key, value)
        new_value = await redis.get(key)
        self.assertEqual(value, new_value)
        await redis.close()
