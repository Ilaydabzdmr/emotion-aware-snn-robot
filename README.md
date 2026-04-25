# 🧠 Emotion-Aware Robot with Spiking Neural Networks (SNN) 🤖

An intelligent robotic system that reacts to human approach behavior using **Spiking Neural Networks (SNNs)**.

The robot distinguishes between:
- 🐢 Slow / gentle approach → *Friendly response*
- ⚡ Fast / aggressive approach → *Defensive response*

---

## 🚀 PROJECT OVERVIEW

This project combines:
- **Neuromorphic computing**
- **Embedded systems (Arduino + Raspberry Pi)**
- **Real-time sensor processing**

The system uses distance-based speed detection and converts it into spike-based neural activity to make decisions.

---

## 🧩 SYSTEM ARCHITECTURE


Ultrasonic Sensor → Arduino → Raspberry Pi → SNN → Decision → Robot Reaction


- Arduino reads distance data  
- Raspberry Pi calculates approach speed  
- SNN processes input as spike trains  
- Robot reacts accordingly  

---

## ⚙️ TECHNOLOGIES USED

- 🧠 Brian2 (Spiking Neural Networks)
- 🐍 Python
- 🔌 Arduino (C++)
- 📡 Serial Communication

---

## 📂 PROJECT STRUCTURE


├── arduino/

│ └── robot_sensor.ino

├── raspberry_pi/

│ └── robot_control.py

├── README.md

└── requirements.txt


---

## ⚙️ INSTALLATION

Clone the repository:
git clone https://github.com/Ilaydabzdmr/emotion-aware-snn-robot.git
cd emotion-aware-snn-robot

Install dependencies:
pip install -r requirements.txt

---

## ▶️ USAGE
- Upload Arduino code to Arduino Uno

- Connect Raspberry Pi via USB

- Run the Python script:

- python raspberry_pi/robot_control.py

---

## ⚠️ NOTE

This project was developed as an experimental prototype and may require hardware setup (Arduino + Raspberry Pi) to run properly.

---


## 🧠 HOW IT WORKS

- Speed of approach is calculated from sensor data

- Speed is converted into spike rate (Hz)

- SNN processes spike input using:

  - Poisson spike generator

  - Leaky integrate-and-fire neurons

- Output neurons compete:
  - 🟥 Threat neuron → Defensive reaction
  - 🟩 Love neuron → Friendly reaction

🔊 SAMPLE RESPONSES

- “Get away from me!” → Threat detected
- “Hello, how are you?” → Friendly interaction

---

## 🔮 FUTURE IMPROVEMENTS
- Emotion classification expansion

- Camera-based input (computer vision)

- More complex neuron models

---

## 📄 LICENSE
MIT License
