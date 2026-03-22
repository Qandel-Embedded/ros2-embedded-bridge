<div align="center">
  <h1>🤖 ros2-embedded-bridge</h1>

  [![CI](https://github.com/Qandel-Embedded/ros2-embedded-bridge/actions/workflows/ci.yml/badge.svg)](https://github.com/Qandel-Embedded/ros2-embedded-bridge/actions)
  [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow.svg)](https://paypal.me/ahmedqandel)
</div>

A lightweight bridge connecting ROS2 humble/foxy to resource-constrained microcontrollers (Arduino, STM32, PIC) via UART or MQTT, without the overhead of micro-ROS.

## Features
- Zero-config UART bridge to `std_msgs`
- MQTT wrapper for ESP32/ESP8266 IoT nodes
- Publish sensor arrays directly to `/embedded_sensors`
- Subscribe to `/embedded_command` and relay hardware commands

## Quickstart

```bash
pip install ros2-embedded-bridge
ros2 run ros2_embedded_bridge ros2-bridge --ros-args -p port:=/dev/ttyACM0 -p baud:=115200
```

## Support & Contact
If you found this useful, consider buying me a coffee to support further open-source hardware work!

Made by **[Ahmed Qandel](https://ahmedqandel.com)** — Industrial Automation & Embedded Systems Engineer  
Available for freelance contracts via [Upwork](https://www.upwork.com/freelancers/ahmedqandel).
