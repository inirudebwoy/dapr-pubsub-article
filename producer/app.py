import logging

from dapr.clients import DaprClient
from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)


app = FastAPI()


class Order(BaseModel):
    product: str


@app.post("/orders")
def orders(order: Order):
    logging.info("Received order")
    with DaprClient() as dapr_client:
        dapr_client.publish_event(
            pubsub_name="order_pub_sub",
            topic_name="orders",
            data=order.json(),
            data_content_type="application/json",
        )
    return order


# for i in range(1, 10):
#     order = {'orderId': i}

#     with DaprClient() as client:
#         # Publish an event/message using Dapr PubSub
#         result = client.publish_event(
#             pubsub_name='order_pub_sub',
#             topic_name='orders',
#             data=json.dumps(order),
#             data_content_type='application/json',
#         )

#     logging.info('Published data: ' + json.dumps(order))
#     time.sleep(1)
