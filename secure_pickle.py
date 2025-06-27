import json

safe_data = {
    "user": "admin",
    "access_level": "readonly"
}

# Serialize
serialized = json.dumps(safe_data)
print("Serialized:", serialized)

# Deserialize
deserialized = json.loads(serialized)
print("Deserialized:", deserialized)