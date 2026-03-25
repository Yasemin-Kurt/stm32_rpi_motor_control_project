# STM32 & Raspberry Pi Motor Control Project

This repository contains a simple motor control project developed as a **3rd-year undergraduate design assignment**. The project demonstrates communication between an STM32F407 Discovery module and a Raspberry Pi 4 using a **USB-TTL converter**. The Raspberry Pi also handles basic image processing with a **1.3 Raspberry Pi Camera** to detect colors and control motor behavior.

---

## Hardware Used
- **STM32F407 Discovery board** – Controls the motors via PWM and GPIO.
- **Raspberry Pi 4** – Handles image acquisition and processing.
- **Raspberry Pi Camera 1.3** – Captures images for color detection.
- **USB-TTL Converter** – Facilitates serial communication between STM32 and Raspberry Pi.
- Motors connected to STM32 for PWM and directional control.

---

## Project Overview
The project workflow is as follows:

1. Raspberry Pi captures an image using the camera.
2. Basic image processing is performed to detect colors (red, yellow, green).
3. The detected color is sent via **USB-TTL** serial communication to the STM32.
4. STM32 adjusts the motor PWM and GPIO pins based on the received color:
  - **Red** → Motors stop for certain channels (base pattern).
  - **Yellow** → Motors run at **slower speeds** compared to green.
  - **Green** → Motors run at **higher speeds** compared to yellow.

The STM32 side uses **HAL libraries** to configure timers (PWM) and GPIOs, while the Raspberry Pi handles Python-based image processing.

---

## Notes and Limitations
- This was my first experience with **STM32, Raspberry Pi, and camera-based image processing**.
- For the given academic context, the project demonstrates the core concepts successfully.
- Image processing currently detects colors; **future improvements** could include shape detection and more advanced algorithms to make the control more robust.
- The STM32 PWM values and GPIO handling are tailored for this prototype setup.

### Note on STM32 Compilation
This project requires the STM32 HAL driver files to compile. The `Drivers/STM32F4xx_HAL_Driver` folder is **not included** in this repository to keep the repo size small. 

To build the STM32 project:
1. Install **STM32CubeIDE** on your computer.
2. Copy or clone the appropriate `Drivers/STM32F4xx_HAL_Driver` folder into the project directory.
3. Open the `.ioc` file in STM32CubeIDE and generate the project code.
4. Compile and flash the project to the STM32F407 Discovery board.

---

## Professional Recommendations
- Implement **shape-based detection** along with color detection for more reliable control.
- Use **interrupt-based UART reception** on STM32 instead of polling for better performance.
- Explore **smoother motor control** using PID or other control algorithms for real-world applications.

---

## License
This project is provided **as-is** for educational purposes.
