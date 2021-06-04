

# import zlib and crc32
import zlib
import struct

linear_x = 0.1
angular_z = 0.1
behaviorId = 11
behaviorMode = 0.8
height = 0.1
lateral = 0.1
GRM_MAGIC = 171

#behaviorCmd = struct.pack('<I14f',
#                          behaviorId,
#                          linear_x, 0.1, 0.1,
#                          0.1, 0.1, angular_z,
#                          0.1, lateral, height, 0.1, 0.1, 0.1, 0.1,
#                          behaviorMode)


behaviorCmd = struct.pack('<If',
                          behaviorId, behaviorMode)


def grmCrc(data):
	# crc32 only works properly on DWORD aligned buffers
	# dataSizeMod4 = (len(data) / 4) * 4    
	return zlib.crc32(data, 0)


dataCrc = grmCrc(behaviorCmd)
print(len(behaviorCmd))
print(dataCrc % (1 << 32))

header = struct.pack('<BBHiBB', GRM_MAGIC, 1, len(behaviorCmd), dataCrc, 16, 1)
Crc2 = grmCrc(header)
# print(Crc2%(1<<32))

""" dataCrc = zlib.crc32(behaviorCmd)
# print(t%(1<<32))

print(dataCrc%(1<<32)) """




