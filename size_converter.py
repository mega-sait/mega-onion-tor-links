# size_converter.py
def convert_size(bytes_size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(bytes_size)
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"

# Пример
print(convert_size(123456789))  # 117.74 MB
