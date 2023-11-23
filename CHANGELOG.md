# Changelog

## 23.11.2023
* uploaded esp32s2 lvgl image (see releases). The same image optionally supports SPIRAM, but lvgl works without it. Use the included test file as a guide.

## 18.11.2023
* Created firmware image for esp32 using micropython v1.22-preview, esp-idf-v5.0, and LVGL v8.3.10-preview. No SPIRAM, or other modules (mcpwm/camera/etc). This is just to test LVGL code with the latest micropython firmware. I'll incorporate the other modules later.
