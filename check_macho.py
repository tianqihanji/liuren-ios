import struct, sys, os

path = sys.argv[1]
data = open(path, 'rb').read()
print("size", len(data))

magic = struct.unpack('<I', data[:4])[0]
print("magic(LE)", hex(magic))
if magic != 0xFEEDFACF:
    print("NOT a 64-bit Mach-O")
    sys.exit()

cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags, _ = struct.unpack('<i i I I I I I', data[4:32])
print("cputype", cputype, "filetype", filetype, "ncmds", ncmds, "flags", hex(flags))

off = 32
found = {}
for i in range(ncmds):
    cmd, cmdsize = struct.unpack('<I I', data[off:off+8])
    # LC_CODE_SIGNATURE = 0x1d
    if cmd == 0x1d:
        dataoff, datasize = struct.unpack('<I I', data[off+8:off+16])
        found['code_signature'] = (dataoff, datasize)
    # LC_BUILD_VERSION = 0x32
    if cmd == 0x32:
        platform, minos, sdk = struct.unpack('<I I I', data[off+8:off+20])
        found['build_version'] = (platform, "%d.%d.%d" % ((minos>>16)&0xff,(minos>>8)&0xff,minos&0xff), "%d.%d.%d" % ((sdk>>16)&0xff,(sdk>>8)&0xff,sdk&0xff))
    # LC_VERSION_MIN_IPHONEOS = 0x25
    if cmd == 0x25:
        version, sdk = struct.unpack('<I I', data[off+8:off+16])
        found['version_min_ios'] = ("%d.%d.%d" % ((version>>16)&0xff,(version>>8)&0xff,version&0xff), "%d.%d.%d" % ((sdk>>16)&0xff,(sdk>>8)&0xff,sdk&0xff))
    # LC_ENCRYPTION_INFO = 0x21 / _64 = 0x2c
    if cmd == 0x2c:
        cryptoff, cryptsize, cryptid = struct.unpack('<I I I', data[off+8:off+20])
        found['encryption_info64'] = (cryptoff, cryptsize, cryptid)
    # LC_LOAD_DYLIB = 0xc
    off += cmdsize

print("found:", found)

if 'code_signature' in found:
    o, s = found['code_signature']
    print("code signature blob at", o, "size", s)
else:
    print("NO LC_CODE_SIGNATURE -> binary is fully unsigned")
