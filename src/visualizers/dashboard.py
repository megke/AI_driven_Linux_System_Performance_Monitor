from bokeh.plotting import figure, show

class Dashboard:
    """
    Class for creating a basic dashboard to visualize system performance metrics.
    """

    def __init__(self):
        self.cpu_utilization_plot = None
        self.memory_usage_plot = None

    def create_cpu_utilization_plot(self, data):
        """
        Creates a Bokeh plot for CPU utilization.

        Args:
            data: CPU utilization data (list of floats).
        """
        p = figure(title="CPU Utilization (%)", x_axis_label="Time", y_axis_label="CPU (%)")
        p.line(x=range(len(data)), y=data, line_width=2)
        self.cpu_utilization_plot = p

    def create_memory_usage_plot(self, data):
        """
        Creates a Bokeh plot for memory usage.

        Args:
            data: Memory usage data (list of floats).
        """
        p = figure(title="Memory Usage (%)", x_axis_label="Time", y_axis_label="Memory (%)")
        p.line(x=range(len(data)), y=data, line_width=2)
        self.memory_usage_plot = p

    def show_dashboard(self):
        """
        Displays the dashboard with CPU utilization and memory usage plots.
        """
        show(column=self.cpu_utilization_plot, row=self.memory_usage_plot)

# Example usage
if __name__ == "__main__":
    # Replace with actual data
    cpu_data = [50, 60, 70, 65, 68, 72]
    memory_data = [75, 80, 82, 81, 78, 79]

    dashboard = Dashboard()
    dashboard.create_cpu_utilization_plot(cpu_data)
    dashboard.create_memory_usage_plot(memory_data)
    dashboard.show_dashboard()