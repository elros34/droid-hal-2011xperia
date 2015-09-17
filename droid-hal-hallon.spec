# These and other macros are documented in dhd/droid-hal-device.inc

%define device hallon
%define vendor semc

%define vendor_pretty Sony Ericsson
%define device_pretty Xperia Neo

%define installable_zip 1

%define local_hadk_build_project 1

%define android_config \
#define QCOM_BSP 1\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
