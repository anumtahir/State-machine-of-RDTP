from packet import *
import random

sq_received=0
ACK_MESSAGE = "ACK"
# Declare any global variables here (It may help to store the latest sequence number received)


def sender(array_of_messages):
        global RECEIVED_ACKS
        seqNo=0
        for message in array_of_messages:
                checksum = calculateChecksum(message)
                sPkt = Packet(message, seqNo, checksum) # Creation of a packet (read packet.py to see members)
                sent = True
                while sent==True:
                        ACK = receiver(sPkt) #receiver() is used to sent a packet to the receiver. In return, you receive an ACK packet.
                        if(ACK.seqNo==seqNo and ACK.checksum == calculateChecksum(ACK.message)):
                                RECEIVED_ACKS.append(ACK.message)
                                seqNo = 1-seqNo
                                sent = False
                        
	
                        
	# Hint: Create a way to resend packets if the ACK signifies a corrupt packet was sent (hint: read up on alternating bit protocol)


def receiver(sPkt):
	global RECEIVED_MESSAGES # DO NOT EDIT THIS LINE
	global sq_received
	received_packet = corruptPkt(sPkt)
	if(sq_received==received_packet.seqNo and received_packet.checksum == calculateChecksum(received_packet.message)):
                rPkt=Packet(ACK_MESSAGE,received_packet.seqNo,calculateChecksum(ACK_MESSAGE))
                sq_received=1-sq_received
                RECEIVED_MESSAGES.append(received_packet.message)
	else:
                rPkt=Packet(ACK_MESSAGE,1-received_packet.seqNo,calculateChecksum(ACK_MESSAGE))
                
	return corruptPkt(rPkt) #DO NOT EDIT THIS LINE 
# Write your code 
# Check if the checksum is correct. If it is correct, append the message to the global RECEIVED_MESSAGES array. Else, request a new Packet (hint: read up on rdt2.2)

# Create the correct ACK packet and return it

        


## DO NOT EDIT BELOW
def corruptPkt(packet):
	corruptPkt = Packet(packet.message, packet.seqNo, packet.checksum)
	corruption_indicator = random.random()
	if corruption_indicator > 0.5:
		corruptPkt.checksum = corruptPkt.checksum + random.randint(1,50)
		corruptPkt.message = corruptPkt.message[::-1]
		print("!!!!!!!!! PACKET CORRUPTED !!!!!!!!!")
	return corruptPkt
print("************************************")
print("          RDT 2.2 Protocol          ")
print("************************************")
user_input = ""
while True:
	RECEIVED_MESSAGES = []
	RECEIVED_ACKS = []
	user_input = input("\nEnter message to send (or enter q to quit): ")
	if user_input.upper() == "Q":
		break
	array_of_messages = user_input.split()
	print("************************************\n")
	sender(array_of_messages)
	print("\nReceiver received the following message: " + " ".join(RECEIVED_MESSAGES))
	print("Sender received the following ACKs: " + " ".join(RECEIVED_ACKS))
print("****************EXIT****************\n")
