class Formatter():
    def format_byte(self, bytes_num):
        suffixes = ['B', 'KB', 'MB', 'GB']
        index = 0

        while bytes_num >= 1024 and index < len(suffixes) - 1:
            bytes_num /= 1024
            index += 1

        return f"{bytes_num:.3g} {suffixes[index]}"
