from dapr.ext.fastapi import DaprApp
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
dapr_app = DaprApp(app)


class CloudEvent(BaseModel):
    datacontenttype: str
    source: str
    topic: str
    pubsubname: str
    data: dict
    id: str
    specversion: str
    tracestate: str
    type: str
    traceid: str


@dapr_app.subscribe(pubsub="order_pub_sub", topic="orders")
def orders_subscriber(event: CloudEvent):
    print("Subscriber received : %s" % event.data["product"], flush=True)
    return {"success": True}
