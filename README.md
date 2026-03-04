# LEGO® Education Python API

![LEGO Education logo](./img/LEGOEducation.png)

1. **Introduction and Installation**
2. [Connect and Run](./connect.md)
3. [Single Motor](./singlemotor.md)
4. [Double Motor](./doublemotor.md)
5. [Color Sensor](./colorsensor.md)
6. [Controller](./controller.md)
7. [Combine Single Motor and Color Sensor](combine1.md)
8. [Combine Double Motor and Controller](combine2.md)
9. [Constants](constants.md)

---
# Welcome

Welcome to the LEGO® Education Python API! This library allows users to write Python code to control the LEGO Education Hardware found in the LEGO Education Computer Science & AI kits. Some design choices favor simplicity over strict Python conventions to make the API easier to use in education contexts.

## Supported Hardware

You can use the following motors and sensors with the LEGO Education Python API:

- **Single Motor:** Control and monitor direction, speed, absolute/relative position, power, acceleration, deceleration, and end states.
- **Double Motor:** Synchronized or independent control and monitoring of two connected motors (left and right), including direction, speed, absolute/relative position, power, acceleration, deceleration, and end states. Additionally includes a 6-axis IMU for orientation and motion data.
- **Color Sensor:** Access detected color as LEGO Color Number, RGB raw, HSV, and reflection readings.
- **Controller:** Access dual lever input (left and right) with angle and percentage positional readings.

## Compatibility:

Since the LEGO Education hardware communicates via Bluetooth Low Energy (BLE), you need a device where you can install and run Python, install the LEGO Education Python API, and where Python can access Bluetooth. Note that on Chromebooks, the Linux container used for Python cannot access Bluetooth, so you cannot connect to LEGO Education hardware from Python running on these devices.

## Updating the LEGO Education Hardware:

To update your LEGO Education hardware, visit the [LEGO Education Coding Canvas](https://code.legoeducation.com) and connect each hardware device you plan to code with. If an update is available, the hardware will update automatically when connected to a device with internet connectivity.

---

# Installation

Use of the LEGO Education Python API requires a local installation of Python 3 (min version Python 3.14). If you need to install or upgrade Python on your device, visit [https://python.org/downloads](https://python.org/downloads).

## Installing the API

The LEGO Education Python API is hosted on PyPI (https://pypi.org/project/legoeducation/), a software repository for Python software. To install the LEGO Education Python API on your local device, use the following command:

`pip install legoeducation`

## Running Programs

Open a new program or an example program (see [example.py](./examples/example.py) for Single Motor) in your device’s IDE (local coding environment). For help choosing a coding environment compatible with Python, visit [Python.org’s IDE Wiki](http://wiki.python.org/moin/IntegratedDevelopmentEnvironmentswiki.python.org/moin/IntegratedDevelopmentEnvironments).

To execute a program (e.g. `example.py`), navigate to the folder and run the following command. Make sure the LEGO Education motor(s) and sensor(s) you are using are charged, powered on, and broadcasting.

`python example.py`

## Troubleshooting

- **Firmware errors:** Ensure your LEGO Education hardware’s firmware is on the latest version. See [LEGO Education’s FAQ](https://teach.legoeducation.com/en-us/frequently-asked-questions) for information on updating hardware.

- **Connection issues:** Confirm your Bluetooth setup and verify device compatibility with your OS.

## Updating LEGO Education Python API

To update the LEGO Education Python API to the latest version:

`pip install legoeducation --upgrade`

This will uninstall the previous version and upgrade to the latest version published on PyPI.

## Uninstalling the LEGO Education Python API

To uninstall (remove) the LEGO Education Python API from your device:

`pip uninstall legoeducation`

---

**Next:** [Connect and Run](./connect.md)
