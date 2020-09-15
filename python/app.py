import os
from azure.storage.blob import BlobClient

connection_string = os.getenv("STORAGE_CONNECTION_STRING")

client1 = BlobClient.from_connection_string(connection_string, "test", "test")
print("BlobClient.upload_blob #1")
client1.upload_blob([], overwrite=True)

client2 = BlobClient.from_connection_string(connection_string, "test", "test")
print("BlobClient.upload_blob #2")
client2.upload_blob([], overwrite=True)

# Wireshark shows two HTTPS connections were used
# 
# TCP	65375 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM=1
# TCP	443 → 65375 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1440 WS=256 SACK_PERM=1
# TCP	65375 → 443 [ACK] Seq=1 Ack=1 Win=263424 Len=0
# TLSv1.2	Client Hello
# TCP	443 → 65375 [ACK] Seq=1 Ack=518 Win=262656 Len=1460 [TCP segment of a reassembled PDU]
# TCP	443 → 65375 [ACK] Seq=1461 Ack=518 Win=262656 Len=1460 [TCP segment of a reassembled PDU]
# TCP	65375 → 443 [ACK] Seq=518 Ack=2921 Win=263424 Len=0
# TCP	443 → 65375 [ACK] Seq=2921 Ack=518 Win=262656 Len=1460 [TCP segment of a reassembled PDU]
# TLSv1.2	Server Hello, Certificate, Server Key Exchange, Server Hello Done
# TCP	65375 → 443 [ACK] Seq=518 Ack=5544 Win=263424 Len=0
# TLSv1.2	Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message
# TCP	443 → 65375 [ACK] Seq=5544 Ack=644 Win=262656 Len=0
# TCP	[TCP Dup ACK 252#1] 443 → 65375 [ACK] Seq=5544 Ack=644 Win=262656 Len=0
# TLSv1.2	Change Cipher Spec, Encrypted Handshake Message
# TLSv1.2	Application Data
# TLSv1.2	Application Data
# TCP	65376 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 WS=256 SACK_PERM=1
# TCP	443 → 65376 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1440 WS=256 SACK_PERM=1
# TCP	65376 → 443 [ACK] Seq=1 Ack=1 Win=263424 Len=0
# TLSv1.2	Client Hello
# TCP	443 → 65376 [ACK] Seq=1 Ack=518 Win=262656 Len=1460 [TCP segment of a reassembled PDU]
# TCP	443 → 65376 [ACK] Seq=1461 Ack=518 Win=262656 Len=1460 [TCP segment of a reassembled PDU]
# TCP	65376 → 443 [ACK] Seq=518 Ack=2921 Win=263424 Len=0
# TCP	443 → 65376 [ACK] Seq=2921 Ack=518 Win=262656 Len=1460 [TCP segment of a reassembled PDU]
# TLSv1.2	Server Hello, Certificate, Server Key Exchange, Server Hello Done
# TCP	65376 → 443 [ACK] Seq=518 Ack=5544 Win=263424 Len=0
# TLSv1.2	Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message
# TCP	65375 → 443 [ACK] Seq=1202 Ack=6084 Win=262912 Len=0
# TCP	443 → 65376 [ACK] Seq=5544 Ack=644 Win=262656 Len=0
# TCP	[TCP Dup ACK 276#1] 443 → 65376 [ACK] Seq=5544 Ack=644 Win=262656 Len=0
# TLSv1.2	Change Cipher Spec, Encrypted Handshake Message
# TLSv1.2	Application Data
# TLSv1.2	Application Data
# TCP	65375 → 443 [FIN, ACK] Seq=1202 Ack=6084 Win=262912 Len=0
# TCP	65376 → 443 [FIN, ACK] Seq=1202 Ack=6084 Win=262912 Len=0
# TCP	443 → 65375 [FIN, ACK] Seq=6084 Ack=1203 Win=261888 Len=0
# TCP	65375 → 443 [ACK] Seq=1203 Ack=6085 Win=262912 Len=0
# TCP	443 → 65376 [FIN, ACK] Seq=6084 Ack=1203 Win=261888 Len=0
# TCP	65376 → 443 [ACK] Seq=1203 Ack=6085 Win=262912 Len=0
