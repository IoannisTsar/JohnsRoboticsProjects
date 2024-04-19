import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk
import time

# GPIO pin for servo
servo_pin = 14

# Set GPIO mode and PWM frequency
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms PWM period)

# Duty cycle limits for the servo
min_duty = 2.5  # Duty cycle for 0 degrees
max_duty = 12.5  # Duty cycle for 180 degrees

# Function to convert angle to duty cycle
def angle_to_duty_cycle(angle):
    duty_cycle = (angle / 180.0) * (max_duty - min_duty) + min_duty
    return duty_cycle

# Function to set servo angle
def set_angle(angle):
    duty_cycle = angle_to_duty_cycle(angle)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)  # Adjust as needed for servo response time

def update_servo_position(value):
    angle = int(float(value) * 1.8)
    set_angle(angle)

# Create a Tkinter window
root = tk.Tk()
root.title("Servo Control")

# Create a label
label = ttk.Label(root, text="Move the slider to control the servo:")
label.pack(pady=10)

# Create a scale (slider) widget
slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=update_servo_position)
slider.pack()

# Initialize the slider value to the center
slider.set(50)

# Start PWM
pwm.start(0)  # Initial duty cycle (0 degrees)

# Start the Tkinter event loop
root.mainloop()

# Clean up GPIO
pwm.stop()
GPIO.cleanup()
