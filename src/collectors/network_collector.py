import psutil

def get_network_io_counters():
    """
    Collects network I/O counters (bytes sent and received).

    Returns:
        dict: Dictionary containing bytes sent and received.
    """
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv
    }

# Example usage
if __name__ == "__main__":
    network_io = get_network_io_counters()
    print(network_io)