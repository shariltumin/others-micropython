You can find firmware for Wemos-Mini board here

To flash the firmware plese use this shell script

```sh
#!/bin/sh
esptool.py --port $1 \
 --baud 460800 --before default_reset --after hard_reset \
 --chip esp32s2  write_flash --flash_mode dio --flash_size detect \
 --flash_freq 80m 0x1000 firmware.bin

```

For example,
```
./esp32s2_flash /dev/ttyACM0
```

Test run
```
MPY: soft reboot
MicroPython v1.20.0-396-g1dedb65e6 on 2023-08-29; ESP32 S2_MINI WEMOS (KAKI5) with ESP32-S2FN4R2
Type "help()" for more information.
>>> import micropython as mp
>>> mp.mem_info()
stack: 704 out of 15360
GC: total: 64000, used: 1888, free: 62112, max new split: 1998848
 No. of 1-blocks: 31, 2-blocks: 6, max blk sz: 18, max free sz: 3846
>>> a = 'a'*1900000
>>> mp.mem_info()
stack: 704 out of 15360
GC: total: 1967552, used: 1901520, free: 66032, max new split: 131072
 No. of 1-blocks: 25, 2-blocks: 5, max blk sz: 118751, max free sz: 3846
>>> del a
>>> gc.collect()
>>> mp.mem_info()
stack: 704 out of 15360
GC: total: 64000, used: 1536, free: 62464, max new split: 1998848
 No. of 1-blocks: 27, 2-blocks: 5, max blk sz: 18, max free sz: 3846
>>> 
```

The firmware was compile with this sdkconfig.board

```
CONFIG_IDF_TARGET="esp32s2"
CONFIG_IDF_TARGET_ESP32S2=y

# MicroPython on ESP32S2, ESP IDF configuration with 240MHz CPU
# -CONFIG_ESP32_DEFAULT_CPU_FREQ_240=y
# -CONFIG_ESP32_DEFAULT_CPU_FREQ_MHZ=240
CONFIG_ESP32S2_DEFAULT_CPU_FREQ_240=y
CONFIG_ESP32S2_DEFAULT_CPU_FREQ_MHZ=240

# SPI RAM config for S2/S3 but not working with camera
CONFIG_ESP32S2_SPIRAM_SUPPORT=y
# QUAD or OCT S2 uses SPI-QUAD S3 uses SPI-OCT for PSRAM
CONFIG_SPIRAM_MODE_QUAD=y
# -CONFIG_SPIRAM_MODE_OCT=y
CONFIG_SPIRAM_TYPE_AUTO=y
CONFIG_DEFAULT_PSRAM_CLK_IO=30
CONFIG_DEFAULT_PSRAM_CS_IO=26
CONFIG_SPIRAM_SPEED_80M=y
CONFIG_SPIRAM=y
CONFIG_SPIRAM_BOOT_INIT=y
CONFIG_SPIRAM_IGNORE_NOTFOUND=y
# -CONFIG_SPIRAM_USE_MEMMAP=y <-- not working not all RAM map use default malloc
CONFIG_SPIRAM_USE_MALLOC=y
# This is the threshold for preferring small allocations from internal memory
# first, before failing over to PSRAM.
CONFIG_SPIRAM_MALLOC_ALWAYSINTERNAL=8192
CONFIG_SPIRAM_MEMTEST=y

# DEBUGGING
# CONFIG_LOG_DEFAULT_LEVEL_INFO=y
# CONFIG_LOG_DEFAULT_LEVEL_ERROR=n
CONFIG_LOG_DEFAULT_LEVEL_DEBUG=y
# CONFIG_LOG_DEFAULT_LEVEL_VERBOSE=y
# CONFIG_LOG_MAXIMUM_LEVEL_VERBOSE=y

#
# PARTITION
#
CONFIG_ESPTOOLPY_FLASHSIZE_4MB=y
CONFIG_PARTITION_TABLE_CUSTOM=y
CONFIG_PARTITION_TABLE_CUSTOM_FILENAME="boards/WEMOS_S2_MINI/partitions-4MiB.csv"

# SPIRAM increases the size of the firmware, use -Os to reduce it again to fit in iram
CONFIG_COMPILER_OPTIMIZATION_SIZE=y

# USB
# -CONFIG_USB_OTG_SUPPORTED=y
CONFIG_TINYUSB_CDC_ENABLED=y
CONFIG_TINYUSB_CDC_RX_BUFSIZE=256
CONFIG_TINYUSB_CDC_TX_BUFSIZE=256
CONFIG_USB_AND_UART=y
# CONFIG_ESP_CONSOLE_USB_CDC=y  <--- [no REPL!!]

# Other setting
CONFIG_FLASHMODE_QIO=y
CONFIG_ESPTOOLPY_FLASHFREQ_80M=y

# LWIP
CONFIG_LWIP_LOCAL_HOSTNAME="WEMOS_S2_MINI"
CONFIG_LWIP_TCP_SYNMAXRTX=6
# end of LWIP

# SSL
CONFIG_MBEDTLS_PSK_MODES=y
CONFIG_MBEDTLS_KEY_EXCHANGE_PSK=y
CONFIG_MBEDTLS_SSL_PROTO_DTLS=y

```
