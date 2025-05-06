import psutil

def get_cpu_utilization():
    """
    Collects CPU utilization.

    Returns:
        float: CPU utilization percentage.
    """
    return psutil.cpu_percent(interval=1)

def get_cpu_load_average():
    """
    Collects CPU load average.

    Returns:
        tuple: 1-minute, 5-minute, and 15-minute load averages.
    """
    return os.getloadavg()

# Example usage
if __name__ == "__main__":
    cpu_utilization = get_cpu_utilization()
    load_avg = get_cpu_load_average()
    print(f"CPU Utilization: {cpu_utilization}%")
    print(f"Load Average: {load_avg}")