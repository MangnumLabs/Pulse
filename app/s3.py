import json
import boto3
from datetime import datetime

BUCKET = "pulse-events-local"

s3 = boto3.client(
    "s3",
    endpoint_url="http://localstack:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

def build_s3_key(event_id: int):
    now = datetime.utcnow()
    return f"pulse/events/{now.year}/{now.month:02}/{now.day:02}/{event_id}.json"

def upload_payload(event_id: int, payload: dict):
    body = json.dumps(payload).encode()
    key = build_s3_key(event_id)

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=body,
        ContentType="application/json",
    )

    return key, len(body)
