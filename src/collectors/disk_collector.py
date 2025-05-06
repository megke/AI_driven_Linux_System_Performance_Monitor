import psutil

def get_disk_usage(path="/"):
    """
    Collects disk usage statistics for the specified path.

    Args:
        path: Path to the disk to monitor (default: "/").

    Returns:
        dict: Dictionary containing disk usage information 
              (total, used, free, percent).
    """
    disk = psutil.disk_usage(path)
    return {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }

# Example usage
if __name__ == "__main__":
    disk_usage = get_disk_usage()
    print(disk_usage)