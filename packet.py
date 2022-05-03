NUM_OF_BITS = 8
class Packet:
	def __init__(self, message, seqNo, checksum):
		self.message = message
		self.checksum = checksum
		self.seqNo = seqNo


def calculateChecksum(message):
	# Write code to calculate checksum
  checksum=0
  for ele in message:
    ele=ord(ele)
    checksum=checksum+ele
  checksum=~(int(checksum/256)+(checksum%256))
  return checksum
