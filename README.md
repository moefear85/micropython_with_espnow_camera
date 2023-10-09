# micropython_with_espnow_camera

This project is a quick hack and WIP. It is a build of micropython 1.20 firmware for the esp32 with or without psram, and includes the esp32-camera module, and espnow. It autodetects psram but works without it. The camera works without psram by default, so you'll need to configure that. The camera module uses lemariva's codebase, so look there on how to do so. For espnow, import espnow and run espnow.help(). If you need other esp32 chips or the source, let me know. I'll expand the project with source & improve the espnow functionality.

The UART REPL speed has been bumped to 1152000.

## Receive Callback
You can block or do lengthy operations in the espnow receive callback for as long as you want, but if the wifi rx buffers fill up due to slow processing, packets will be dropped at the receiver after having been already acknowledged to the sender as having been successfully received. There is no easy fix for this, it would require rewriting the closed-source espnow subsystem in esp-idf so that the user-specified receive callback (ISR context) doesn't remove packets from the wifi rx buffers unless it returns with a specific status code, and allow the user to pop off packets later manually, and avoid acknowledging any further packets until there is space in the wifi rx buffers again.

# Known Issues
- once the camera has been initialized, it begins to corrupt the outgoing uart repl stream. this is a carry-over from the original project and independent of configured baudrate. I don't know the cause. Input is not affected however.
- gpio_install_isr_service(), called by camera.init(), sporadically displays an error about already being installed. This is caused by the esp32-camera driver mixed with micropython. It seems harmless.
- soft reset without first calling espnow.deinit() will GuruMeditate at the next incoming packet.
- currently, my compiled firmware sporadically GuruMeditates after a while, even if not using camera or espnow or ever having called init(). I'm not sure if it has anything to do with wifi. I'm currently learning to pull and decode a crashdump from flash to determine what's going on. If you can help, let me know.

# Future Plans
- make espnow more configurable
- expose sniffer api to micropython
- make camera config/init options clearer using constants
- integrate mcpwm as well as various other sensor/actuator (display) drivers & libraries for them, such as lvgl, tft_espi (my traditional choice for ILI9341 parallel LCD interface), etc.
