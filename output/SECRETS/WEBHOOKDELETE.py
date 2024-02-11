import requests

# URL des Webhooks, den du löschen möchtest
webhook_url = "https://chat.openai.com/c/f3d62492-f223-45a3-9a04-67572706af02"

# DELETE-Anfrage senden, um den Webhook zu löschen
response = requests.delete(webhook_url)

# Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
if response.status_code == 204:
    print("Webhook erfolgreich gelöscht.")
    print(response.json())
else:
    print("Fehler beim Löschen des Webhooks. Statuscode:", response.status_code)
    print(response.json())
