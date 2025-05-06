from playsound import playsound  # For playing alert sounds (optional)

def send_email_alert(message):
  """
  Sends an email alert with the specified message.

  Args:
      message: The message to include in the email alert.
  """
  # Replace with your email sending logic (e.g., using smtplib or an email API)
  print(f"Sending email alert: {message}")

def play_alert_sound():
  """
  Plays an alert sound to notify the user.

  You can replace this function with your preferred notification method 
  (e.g., system notifications, SMS alerts).
  """
  playsound("alert.wav")  # Replace "alert.wav" with your desired sound file path

def trigger_alert(metric_name, current_value, threshold):
  """
  Triggers an alert if the current value of a metric exceeds the threshold.

  Args:
      metric_name: The name of the metric being monitored.
      current_value: The current value of the metric.
      threshold: The threshold for triggering an alert.
  """
  if current_value > threshold:
    message = f"Alert: {metric_name} ({current_value:.2f}) exceeded threshold ({threshold:.2f})"
    send_email_alert(message)
    play_alert_sound()  # Optional: play an alert sound

# Example usage
if __name__ == "__main__":
  metric_name = "CPU Utilization"
  current_value = 85
  threshold = 80
  trigger_alert(metric_name, current_value, threshold)