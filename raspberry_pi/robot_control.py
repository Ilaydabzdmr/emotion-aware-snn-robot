from brian2 import*
import serial
import numpy as np
import os
import time
import matplotlib.pyplot as plt

#!!!Check Port
arduino_port = '/dev/ttyUSB0'
#115200(?)
baud_rate = 9600


#Start Serial Connnection
try:
        ser = serial.Serial(arduino_port, baud_rate, timeout=1)
        print("Connection Established")
        time.sleep(1)
except:
        print("Connection Failed")
        exit()


duration = 1000*ms #SNN runtime
input_rate_scale = 5*Hz #Spike rate multiplier
speed_threshold = 10

def getArduino():
        while True:
                value = ser.readline().decode('utf-8').strip()
                try:
                        speed = float(value)
                        print(f"Speed: {speed:.2f}cm/s")
                        return speed
                except ValueError:
                        print(f"incorrect Value: {value}")
                        continue

def RunSNN(SpikeRateHz):
        print(f"Spike Rate: {SpikeRateHz} Hz")

        #Poisson Spike Input:
        p = PoissonGroup(1, rates=SpikeRateHz)

        #OUTPUT Neurons:
        eqs = '''
        dv/dt = -v/(20*ms):1
        '''

        G = NeuronGroup(2, eqs, threshold='v > 1.5', reset='v = 0', method='exact')

        #Connections
        S = Synapses(p,G,on_pre='v += 0.5')
        S.connect(j='i') #Each input is connected to each output

        #Spike Monitors
        M = SpikeMonitor(G)

        run(duration)

        #Spike graph drawing:
        plt.figure(figsize=(10, 4))
        plt.plot(M.t/ms, M.i, '.k') #Dots are spike times and neuron indices
        plt. xlabel('Time (ms)')
        plt.ylabel('Neuron index')
        plt.title('Spike Raster Plot')
        plt.savefig("spike_raster_plot.png")

        #Decision
        spikes = M.count
        print(f"Spikes:{spikes}")
        if spikes[0] > spikes[1]:
                return "MODE_THREAT"
        else:
                return "MODE_LOVE"


#ESpeak:
def speak(decision):
        if decision == "MODE_THREAT":
                os.system("espeak 'Get away from mee'")
        else:
                os.system("espeak 'Helloo,How are you?'")

#Main
while True:
        speed = getArduino()

        #Convert Speed to SpikeRate
        if speed <= 0:
                SpikeRate = 0*Hz
        else:
                SpikeRate = min(speed*input_rate_scale,350*Hz)

        decision = RunSNN(SpikeRate)

        speak(decision)

        print(f"Decision: {decision}")
        ser.write((decision + '\n').encode())
        time.sleep(0.5)
