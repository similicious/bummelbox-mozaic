# bummelbox-moziac

This repository contains Moziac scripts for integrating my Novation Launchkey 49 MK4 with Loopy Pro:

- Pads (top row) record / start / stop Clips, with full state feedback
- Pads (bottom row) plays drum sampler, mute / unmute via Function button
- Up / down buttons next to the pads select the drum page
- Custom sidechain via MIDI CC messages from any kick note (any octave of C)
- Much more

## pico-midi-loopback

Contains a simple Circuitpython script which returns the MIDI messages sent to it on a channel 1. I use this to work around the limitation that Auv3 MIDI plugins do not receive state feedback via MIDI Messages.
