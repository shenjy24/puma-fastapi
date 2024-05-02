# import redis

# redis_client = redis.Redis(host='localhost', port=6379, db=0)


def publish_message(channel: str, message: str):
    pass
    # 发布消息到指定的频道
    # redis_client.publish(channel, message)


if __name__ == "__main__":
    channel_name = "hello"
    # 发布消息到频道
    publish_message(channel_name, "Hello, subscribers!")
