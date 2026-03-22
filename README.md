# ros2-embedded-bridge

[![CI](https://github.com/Qandel-Embedded/ros2-embedded-bridge/actions/workflows/ci.yml/badge.svg)](https://github.com/Qandel-Embedded/ros2-embedded-bridge/actions)

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
