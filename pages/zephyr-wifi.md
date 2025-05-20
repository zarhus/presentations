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

<center><img src="/../img/crosscon-logo-2.png" width="200px"></center>

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

- Zephyr OS
- Baremetal Wi-Fi application
- Bao Hypervisor

---

## Implementation

- VM entry point had to be 
- Discovering devices and interfaces that were used by the application and its
libraries

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

- UART conflict

