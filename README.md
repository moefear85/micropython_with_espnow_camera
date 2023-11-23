### Update Notice
* esp32s2 now works with lvgl, with or without spiram. see changelog/releases. I can't test the esp32s3/c3 at the moment, as I don't have any broken out modules. But the images are ready, if someone wants to test them.

# micropython_with_espnow_camera_mcpwm_sniffer_lvgl

This project is a quick hack and WIP. It is a build of micropython 1.22 firmware for the esp32 with or without psram, and includes the esp32-camera module, and espnow. It autodetects psram but works without it. The camera works without psram by default, so you'll need to configure that. The camera module uses lemariva's codebase, so look there on how to do so. For espnow, import espnow and run espnow.help(). If you need other esp32 chips or the source, let me know. I'll expand the project with source & improve the espnow functionality.

The motivation behind this is the fact that many useful features/modules that one might want, are compiled by various people separately, so you always have to choose one image/feature or the other. My goal is to integrate them into an AIO image, with GUI, MCPWM, ESPNOW, SNIFFER/PACKET-FREEDOM, other ESP Peripherals not yet in MPY, and Logging (although I recently found out its already in the micropython-libs).

* The UART REPL speed has been bumped to 1152000. Some log messages are printed in 115200 at boot, specifically harmless errors about psram & presumably tinyusb.
* Read the md files for each individual module
* There's no point in building SPIRAM variants, because all targets are compiled with optional SPIRAM, and then it doesn't matter whether you specifically pass BOARD_VARIANT=SPIRAM (which can only be passed to esp32 anyways). They will all use SPIRAM if available. you can test this using the following:
* ```
  import esp32
  esp32.idf_heap_info(esp32.HEAP_DATA)
  ```
  This will print a set of 4-tuples, each tuple represents a different type/area of memory (the 2nd represents SPIRAM if available), and within each tuple, the 1st element represents the total size of that area, the 2nd represents the total free size of that area. Hence if you see anything larger than 1MB there, you know mpy is using SPIRAM.

# Known Issues
* if you set *hybrid=False* when creating the ili9341 Display, it sporadically meditates. *hybrid=True* is not only faster, it's also more reliable. See the test file if you don't know what I'm talking about.
* once the camera has been initialized, it begins to corrupt the outgoing uart repl stream. this is a carry-over from the original project and independent of configured baudrate. I don't know the cause. Input is not affected however.
* gpio_install_isr_service(), called by camera.init(), sporadically displays an error about already being installed. This is caused by the esp32-camera driver mixed with micropython. It seems harmless.
* soft reset without first calling espnow.deinit() will GuruMeditate at the next incoming packet.
* currently, my compiled firmware sporadically GuruMeditates after a while, even if not using camera or espnow or ever having called init(). I'm not sure if it has anything to do with wifi. I'm currently learning to pull and decode a crashdump from flash to determine what's going on. If you can help, let me know.

# Future Plans
- make espnow more configurable
- expose sniffer api to micropython
- make camera config/init options clearer using constants
- integrate mcpwm as well as various other sensor/actuator (display) drivers & libraries for them, such as lvgl, tft_espi (my traditional choice for ILI9341 parallel LCD interface), etc.
