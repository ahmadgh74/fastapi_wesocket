import aioredis


class RedisHandler:

    def __init__(self, address, db=None, password=None,
                 ssl=None, encoding=None, parser=None,
                 loop=None, timeout=None, connection_cls=None):
        self.redis = None

        self.address = address
        self.db = db
        self.password = password
        self.ssl = ssl
        self.encoding = encoding
        self.parser = parser
        self.loop = loop
        self.timeout = timeout
        self.connection_cls = connection_cls

    async def __init_redis(self):
        if not self.redis:
            self.redis = await aioredis.create_redis(
                address=self.address,
                db=self.db,
                password=self.password,
                ssl=self.ssl,
                encoding=self.encoding,
                parser=self.parser,
                loop=self.loop,
                timeout=self.timeout,
                connection_cls=self.connection_cls)

    async def set(self, key, value):
        await self.__init_redis()
        await self.redis.set(key, value)

    async def get(self, key):
        await self.__init_redis()
        return await self.redis.get(key, encoding='utf-8')

    async def close(self):
        if self.redis:
            self.redis.close()
            await self.redis.wait_closed()
            self.redis = None
