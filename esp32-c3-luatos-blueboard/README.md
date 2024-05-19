# ESP32-C3 LUATOS Blueboard

You will need to change the **IDF_PATH** in the build script, ```mpb_esp32_kaki5.sh```, to point to your esp-idf directory.

You will need to modify the contents of "boards/ESP32_C3_KAKI5/manifest.py" to suit your specific frozen modules.

Please note that this build disables *GIL* (see, "mpconfigport.h-KAKI5") and is not fully tested. It is not guaranteed to work.
