from zlib import compress, decompress

def serialize(data):
    packed_data = b''.join(num.to_bytes(4, 'big') for num in data)
    compressed_data = bytearray(compress(packed_data))
    compression_ratio = len(packed_data) / len(compressed_data)
    return compressed_data, compression_ratio

def deserialize(compressed_data):
    decompressed_data = decompress(bytes(compressed_data))
    unpacked_data = [int.from_bytes(decompressed_data[i:i+4], 'big') for i in range(0, len(decompressed_data), 4)]
    return unpacked_data

tests = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    list(range(1, 51)),
    list(range(1, 101)),
    list(range(1, 501)),
    list(range(1, 1001)),
    [1] * 1000,
    [10] * 1000,
    [100] * 1000,
    list(range(1, 301)) * 3
]

for test in tests:
    serialized, compression_ratio = serialize(test)
    deserialized = deserialize(serialized)
    print(f"Исходная строка: {test}")
    print(f"Сжатая строка: {serialized}")
    print(f"Коэффициент сжатия: {compression_ratio:.2f}")
    print(f"Десериализованная строка: {deserialized}")
    print()
