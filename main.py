from thinkdsp import SinSignal, CosSignal
import thinkplot

signal = SinSignal(freq=400, amp=1.0) + SinSignal(freq=800, amp=0.4) + SinSignal(freq=1600, amp=0.8)
signal += SinSignal(freq=356)

wave = signal.make_wave(duration=3)
wave.normalize()
wave.apodize()

wave.write()