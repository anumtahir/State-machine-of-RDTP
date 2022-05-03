# State-machine-of-RDTP
This assignment focuses on implementing the state machines at the sender and receiver side of a reliable data transfer protocol. For simplicity, we will consider:
1. The protocol does not pipeline packets (i.e., no sliding window is used). The sequence numbers are 0 and 1 (alternating-bit protocol)
2. A channel that does not lose packets
3. Only the sent packet and/or the acknowledgment packet can get corrupted.
4. The protocol is NACK-free and the ACKs are numbered
