---
theme: ../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

##  Running demo Wi-Fi Zephyr application inside the CROSSCON Hypervisor

<center>
    <img src="/../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---

## Who am I?

<div class="grid grid-cols-2 gap-8">

<div>

**Paweł Langowski**

_Junior Embedded Systems Engineer_

_member of the **Zarhus** team_

- <pawel.langowski@3mdeb.com>
- [3mdeb.com](https://3mdeb.com)

</div>

<div class="flex justify-center items-center">
  <img src="/../img/zarhus_logo.png" height="220px" style="filter: invert(1)"/>
</div>

</div>

---

## Agenda

<v-clicks>

- Introduction
- Prerequisites
- Implementation
- Demo
- Conclusion

</v-clicks>

<!--
* The agenda of the presentation
* First I will introduce the topic and explain the goal of the task
* Then I will talk about the hardware and software used to achieve this goal
* Next I will explain how the task was implemented
* Afterwards, I will show you a quick demo
* I will end the presentation with conclusions
-->

---

## Introduction

### What is crosscon?

- A project that focuses on security for IoT devices
- The [CROSSCON Hypervisor](https://github.com/crosscon/CROSSCON-Hypervisor)
runs software inside isolated virtual machines
- The Hypervisor is responsible for distributing access to hardware resources
between VMs
- More information: [Blog post](https://blog.3mdeb.com/2025/2025-04-10-crosscon-its-hypervisor-and-zarhus)

<img src="/../img/crosscon-logo-2.png" width="200px" align="right">

<!--
The central idea of the project is the CROSSCON Hypervisor, which runs software
inside isolated virtual machines.
The HV is responsible for managing access to hardware resources for
virtual machines, in which software is executed.
-->

---

## Introduction

### Goal of the task

- Run a Zephyr application inside a VM on the CROSSCON Hypervisor
- The Zephyr application connects to a Wi-Fi network

<!--
* The goal of our task was to run a Zephyr app inside a virtual machine within
the CROSSCON Hypervisor
* The Zephyr application scans for available Wi-Fi access points and connects to
a specified hotspot.
-->

---

## Prerequisites

### [LPCXPRESSO55S69](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html)

<img src="/../img/lpc.jpg" width="350px" align="right">

- LPC55S69 dual core Arm Cortex-M33 microcontroller
- MikroEletronika Click expansion

---

## Prerequisites

### [MikroElektronika WIFI and BLE Shield](https://docs.zephyrproject.org/latest/boards/shields/mikroe_wifi_bt_click/doc/index.html)

<img src="/../img/wifi_click.jpg" width="300px" align="right">

- Wi-Fi and Bluetooth
- Uses the standard MikroBus interface with UART pins


### Software

- [Zephyr OS](https://www.zephyrproject.org/)
- Zephyr `Hello, world` application that worked in the Hypervisor
- Baremetal Wi-Fi application
- [Bao Hypervisor](https://github.com/bao-project/bao-hypervisor)

<!--
Before we got around to the task, much of the environment had already been
prepared. We had a working `Hello, world` Zephyr application that could be
deployed inside the Hypervisor. The Wi-Fi application had also been developed as
a baremetal application. Our task was to run it in the HV. We initially used the
Bao Hypervisor, which serves as the base for the CROSSCON HV.
-->

---

## Implementation

- VM entry point had to be modified to fit the application's entry

The binary's entry point can be read using `readelf`:

```bash
readelf -aW zephyr.elf  | grep __start
  4942: 00045b15     0 FUNC    GLOBAL DEFAULT    2 __start
```

It has to be equal to the VM's entry point plus 1.

```c
/* ZEPHYR VM */
.image = VM_IMAGE_LOADED(0x00040000, 0x00040000, 0x30000),
.entry = 0x00045b14,
```

---

## Implementation

- Discovering devices and interfaces that were used by the application and its
libraries

`prj.conf`:

```text
CONFIG_NETWORKING=y
CONFIG_NET_IPV6=n
CONFIG_NET_IPV4=y
CONFIG_NET_ARP=y
CONFIG_NET_UDP=y
CONFIG_NET_DHCPV4=y
CONFIG_NET_DHCPV4_OPTION_CALLBACKS=y
CONFIG_DNS_RESOLVER=y
(...)
```

<!--
A Zephyr application can define its own Kconfig options. They are defined in
`prj.conf`. Those values are then merged with other settings to produce the
final configuration.
-->

---

## Implementation

After enabling `CONFIG_NETWORKING`:

```diff
1301a1505,1506
> CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR=y
> # CONFIG_XOSHIRO_RANDOM_GENERATOR is not set
1302a1508,1510
> CONFIG_CSPRNG_ENABLED=y
> CONFIG_HARDWARE_DEVICE_CS_GENERATOR=y
> # CONFIG_CTR_DRBG_CSPRNG_GENERATOR is not set
```

Access to the random number generator had to be granted to the VM.

<!--
After enabling `CONFIG_NETWORKING`, we can see that options related to the RNG
were enabled.
-->

---

## Implementation

Hypervisor config:

```c
@@ -102,6 +102,12 @@ struct config config = {
+                    {
+                        /* RNG */
+                        .pa = 0x4003a000,
+                        .va = 0x4003a000,
+                        .size = 0x1000,
+                    },
                 },
                 .ipc_num = 1,
                 .ipcs = (struct ipc[]) {
```

- Granting access to required flash regions

The program failed to call the `memset` function. It turned out that the flash
memory region, where `memset` was defined was outside the scope assigned to the
VM. The flash size had to be increased.

---

## Implementation

- UART conflict

Separate UART interfaces had to be set up for the Wi-Fi module and console logs.

```diff
--- a/boards/nxp/lpcxpresso55s69/lpcxpresso55s69_lpc55s69_cpu0_ns.dts
+++ b/boards/nxp/lpcxpresso55s69/lpcxpresso55s69_lpc55s69_cpu0_ns.dts
@@ -30,9 +30,9 @@
-               zephyr,uart-mcumgr = &flexcomm2;
-               zephyr,console = &flexcomm2;
-               zephyr,shell-uart = &flexcomm2;
+               zephyr,uart-mcumgr = &flexcomm3;
+               zephyr,console = &flexcomm3;
+               zephyr,shell-uart = &flexcomm3;
                zephyr,entropy = &rng;
        };

@@ -84,6 +84,10 @@
+&flexcomm3 {
+       status = "okay";
+};
+
```

---

## Implementation

```diff
--- a/boards/nxp/lpcxpresso55s69/lpcxpresso55s69.dtsi
+++ b/boards/nxp/lpcxpresso55s69/lpcxpresso55s69.dtsi
@@ -12,7 +12,7 @@
-               usart-0 = &flexcomm2;
+               usart-0 = &flexcomm3;
        };
@@ -104,7 +104,7 @@
-&flexcomm2 {
+&flexcomm3 {
        compatible = "nxp,lpc-usart";
        current-speed = <115200>;
 };
@@ -188,6 +188,11 @@ mikrobus_spi: &hs_lspi {
+&flexcomm3 {
+       pinctrl-0 = <&pinmux_flexcomm3_usart>;
+       pinctrl-names = "default";
+};
```

---

## Implementation

```diff
--- a/boards/nxp/lpcxpresso55s69/lpcxpresso55s69-pinctrl.dtsi
+++ b/boards/nxp/lpcxpresso55s69/lpcxpresso55s69-pinctrl.dtsi
@@ -27,6 +27,14 @@
                };
        };

+       pinmux_flexcomm3_usart: pinmux_flexcomm3_usart {
+               group0 {
+                       pinmux = <FC3_TXD_SCL_MISO_WS_PIO0_2>,
+                               <FC3_RXD_SDA_MOSI_DATA_PIO0_3>;
+                       slew-rate = "standard";
+               };
+       };
+
        pinmux_flexcomm4_i2c: pinmux_flexcomm4_i2c {
                group0 {
                        pinmux = <FC4_TXD_SCL_MISO_WS_PIO1_20>,
```

---

## Implementation

- More problems: check out the blog post

After fixing several other problems and bugs, we managed to run the application.

<center><img src="/../img/hv-wifi-app.png" width="350px"></center>

---

## Demo

---

## Conclusion

Challenges:

- Discovering the devices and interfaces used by the application
- Assigning resources to the virtual machine
- Fixing bugs related to the Hypervisor/Zephyr

---
layout: cover
background: /intro.png
class: text-center
---

## Q&A

<center>
  <img src="/../img/zarhus_logo.png" width="150px">
</center>


