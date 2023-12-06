import requests
import json
from get_client_token import get_client_token
dispute_id = 'b1MLXqVgKgTUUgkmPy8q1rTJGXuoRdjDvqzPHCm0ROP'


def post_auto_message(dispute_id):
    headers = {
        'Authorization': f'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIxMzI5Mzk0MCIsInNjb3BlIjpbImFsbGVncm86YXBpOm9yZGVyczpyZWFkIiwiYWxsZWdybzphcGk6ZnVsZmlsbG1lbnQ6cmVhZCIsImFsbGVncm86YXBpOnByb2ZpbGU6d3JpdGUiLCJhbGxlZ3JvOmFwaTpmdWxmaWxsbWVudDp3cml0ZSIsImFsbGVncm86YXBpOnNhbGU6b2ZmZXJzOndyaXRlIiwiYWxsZWdybzphcGk6YmlsbGluZzpyZWFkIiwiYWxsZWdybzphcGk6Y2FtcGFpZ25zIiwiYWxsZWdybzphcGk6ZGlzcHV0ZXMiLCJhbGxlZ3JvOmFwaTpiaWRzIiwiYWxsZWdybzphcGk6c2FsZTpvZmZlcnM6cmVhZCIsImFsbGVncm86YXBpOnNoaXBtZW50czp3cml0ZSIsImFsbGVncm86YXBpOm9yZGVyczp3cml0ZSIsImFsbGVncm86YXBpOmFkcyIsImFsbGVncm86YXBpOnBheW1lbnRzOndyaXRlIiwiYWxsZWdybzphcGk6c2FsZTpzZXR0aW5nczp3cml0ZSIsImFsbGVncm86YXBpOnByb2ZpbGU6cmVhZCIsImFsbGVncm86YXBpOnJhdGluZ3MiLCJhbGxlZ3JvOmFwaTpzYWxlOnNldHRpbmdzOnJlYWQiLCJhbGxlZ3JvOmFwaTpwYXltZW50czpyZWFkIiwiYWxsZWdybzphcGk6c2hpcG1lbnRzOnJlYWQiLCJhbGxlZ3JvOmFwaTptZXNzYWdpbmciXSwiYWxsZWdyb19hcGkiOnRydWUsImlzcyI6Imh0dHBzOi8vYWxsZWdyby5wbCIsImV4cCI6MTcwMTg5MTUwNiwianRpIjoiNWE0NTAzYTQtMzhlMC00NTJiLTg5MmQtZTc0MDQ5YzgxODRlIiwiY2xpZW50X2lkIjoiZDFjMWE1NGEyOTQ4NDAzNDkyOGVlNzVjMjNiMmRiYTgifQ.EKvupp17qvaofwaFn3N7DR7vRQjv64rq82YeALeBLK_GY6EUwFo5ghY1nhXp9lUMcJFSXFlb5o7N2sEMFqdqkZUaBC1-JyuFfoGWff_35yfIw70X8HbEPtlVjSogb0Ll1jeEwHj8wNuWJ5Fj11nOxupXoMHknDsDcmEGNoYv44YlA00qe5VKOzP_4KpknxaDY40G23F95FBe8J6cXBtvq29oW__h6Na_4RZXZmnQcUzEobOzorzFju1v7VPXhGoHZsaP0aYZqp6j2MztL29x4P2MLMzEUD7Nw9WFz_BJ-lxypIynrNKH0hxCLbtGcUPUdji38lF7tUWkCVTv-4YnPg',
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Content-Type': 'application/vnd.allegro.public.v1+json'
    }

    data = {
        "text": 'Hej Mordeczko, nasz asystent odpowie wkrótce',
        "attachments": [],
        "type": "REGULAR"
    }

    url = f'https://api.allegro.pl/messaging/threads/{dispute_id}/messages'

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.ok:
        print("Message posted successfully.")
    else:
        print(
            f"Failed to post the message. Status Code: {response.status_code}")


post_auto_message(dispute_id)
