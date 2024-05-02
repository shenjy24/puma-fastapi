# import redis

# redis_client = redis.Redis(host='localhost', port=6379, db=0)


def subscribe_channel(channel: str):
    pass
    # 订阅频道
    # pubsub = redis_client.pubsub()
    # pubsub.subscribe(channel)
    #
    # for message in pubsub.listen():
    #     if message['type'] == 'message':
    #         print(f"Received message: {message['data'].decode('utf-8')}")


if __name__ == "__main__":
    channel_name = "hello"
    # 启动订阅者
    subscribe_channel(channel_name)
