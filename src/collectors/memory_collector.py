import psutil

def get_memory_usage():
    """
    Collects memory usage statistics.

    Returns:
        dict: Dictionary containing memory usage information 
              (total, used, free, available, percent).
    """
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'used': mem.used,
        'free': mem.free,
        'available': mem.available,
        'percent': mem.percent
    }

# Example usage
if __name__ == "__main__":
    memory_usage = get_memory_usage()
    print(memory_usage)