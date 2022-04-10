# DAPR playground

Code written for the article https://klichx.dev/?p=283

## How to run the code

In one terminal

```bash
cd producer
pipenv install
dapr run --app-id order-processor --components-path ../components/ --app-port 8000 -- uvicorn app:app
```

In another terminal

```bash
cd consumer
pipenv install
dapr run --app-id order-processor --components-path ../components/ --app-port 8001 -- uvicorn app:app --port 8001
```

Then make a call to the producer.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"product": "falafel"}' http://localhost:8000/orders
```
