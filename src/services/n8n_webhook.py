def send_data_to_n8n(data):
    import requests
    import os

    n8n_webhook_url = os.getenv("N8N_WEBHOOK_URL")

    response = requests.post(n8n_webhook_url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error sending data to n8n: {response.status_code}, {response.text}")

def receive_data_from_n8n(request):
    data = request.json()
    # Process the received data as needed
    return {"status": "success", "received_data": data}