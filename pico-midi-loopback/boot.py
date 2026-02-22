"""
Boot configuration for USB MIDI device
This file runs before code.py and configures the USB device name
"""
import usb_midi
import supervisor

# Set custom MIDI port names
usb_midi.set_names(
    streaming_interface_name="MIDI Loopback",
    audio_control_interface_name="MIDI Loopback Control",
    in_jack_name="MIDI Loopback In",
    out_jack_name="MIDI Loopback Out"
)

# Optionally, you can also customize the USB device name that appears in the system
supervisor.set_usb_identification(
    manufacturer="Custom Devices",
    product="MIDI Loopback"
)
