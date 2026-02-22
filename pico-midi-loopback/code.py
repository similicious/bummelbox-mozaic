"""
MIDI Channel Remapper for Raspberry Pi Pico
Receives MIDI data on any channel and remaps to a single output channel.
No external libraries required - uses only built-in CircuitPython.
"""

import usb_midi

# Get USB MIDI ports
# ports[0] is the input (IN), ports[1] is the output (OUT)
midi_in = usb_midi.ports[0]
midi_out = usb_midi.ports[1]

# Configuration: remap ALL channels to this output channel
# MIDI channels are 1-16 for musicians, but 0-15 in the protocol
OUTPUT_CHANNEL = 1  # Send everything to channel 1

print(f"MIDI Channel Remapper: ALL -> Channel {OUTPUT_CHANNEL}")

def remap_to_channel(data, output_ch):
    """Remap all MIDI channel messages to output_ch (1-16)"""
    if not data:
        return data

    # Convert to bytearray so we can modify it
    output = bytearray(data)
    output_ch_protocol = output_ch - 1  # Convert to 0-15

    i = 0
    while i < len(output):
        status_byte = output[i]

        # Channel voice messages: 0x80-0xEF (Note Off through Pitch Bend)
        if 0x80 <= status_byte <= 0xEF:
            # Extract message type (upper 4 bits)
            msg_type = status_byte & 0xF0
            # Replace with output channel
            output[i] = msg_type | output_ch_protocol

        i += 1

    return bytes(output)

# Main loop
while True:
    # Read incoming MIDI data
    data = midi_in.read(32)  # Read up to 32 bytes at a time

    # If we received data, remap and send it out
    if data:
        remapped = remap_to_channel(data, OUTPUT_CHANNEL)
        midi_out.write(remapped)
