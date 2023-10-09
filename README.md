# micropython_with_espnow_camera

This project is a quick hack to mainly satisfy my own needs. It is a build of micropython 1.20 firmware for the esp32 with or without psram, and includes the esp32-camera module, and espnow. It autodetects psram but works without it. The camera works without psram by default, so'll need to configure that. The camera module uses lemariva's codebase, so look there on how to do so. For espnow, import espnow and run espnow.help(). If you need other esp32 chips or the source, let me know. I'll expand the project with source & improve the espnow functionality when and if I have time.

The binary is in the releases (look right)

# Known Issues
- gpio_install_isr_service(), called by camera.init(), sporadically displays an error about already being installed. This is caused by the esp32-camera driver mixed with micropython. It seems harmless.
- soft reset without first calling espnow.deinit() will GuruMeditate at the next incoming packet.
- currently, my compiled firmware sporadically GuruMeditates after a while, even if not using camera or espnow or ever having called init(). I'm not sure if it has anything to do with wifi. I'm currently learning to pull and decode a crashdump from flash to determine what's going on. If you can help, let me know.

# Future Plans
- integrate mcpwm as well as various other sensor/actuator (display) drivers & libraries for them, such as lvgl, tft_espi, etc.
