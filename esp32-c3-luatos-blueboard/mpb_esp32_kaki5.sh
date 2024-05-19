#!/bin/bash

export PATH="$HOME/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

echo "=========================================================="
echo "Setting up for esp32c3 build"
echo "Using esp-idf-521"
export IDF_PATH="$HOME/disk/esp/esp-idf-521"
export IDF_TARGET="esp32c3"
source $IDF_PATH/export.sh

# Make sure to save esp32_common.cmake and mpconfigport.h 
# cp esp32_common.cmake esp32_common.cmake-ORIG
# cp mpconfigport.h mpconfigport.h-ORIG
# No no GIL
cp esp32_common.cmake-KAKI5 esp32_common.cmake
cp mpconfigport.h-KAKI5 mpconfigport.h
# ESP32C3 - MPV2
make V=1 BOARD=ESP32_C3_KAKI5 MICROPY_PREVIEW_VERSION_2=1 MICROPY_PY_OS=1 MICROPY_VFS_LFS2=1

echo "=========================================================="

