---
theme: ../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## Launching Wi-Fi DHCP client Zephyr application on top of the the CROSSCON Hypervisor

<center>
    <img src="/../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---
layout: two-cols-header
---

## Who am I?

::left::

<center>

<br>

<img src="/../img/daniil.klimuk.webp" width="45%" />

**Daniil Klimuk**

_Zarhus team leader, embedded and Linux enthusiast_

<daniil.klimuk@3mdeb.com> : [3mdeb.com](https://3mdeb.com)

</center>

::right::

<div class="flex justify-center items-center">
  <img src="/../img/zarhus_logo.png" height="220px" />
</div>

---
layout: two-cols-header
---

## Agenda

::left::

- The CROSSCON Project
- The CROSSCON Hypervisor
- The Zephyr RTOS demo
- Implementation
- The final result
- Cunclusions
- Q&A

::right::

<div class="flex justify-center items-center">
  <img src="/../img/zdm-2-logo-crosscon-hyp-dhcp-demo.png" height="220px" />
</div>

---
layout: two-cols-header
---

### The CROSSCON Project

::left::

- A project that focuses on security for IoT devices
- More information:
    * CROSSCON, its Hypervisor, and Zarhus blog post <blog.3mdeb.com/2025/2025-04-10-crosscon-its-hypervisor-and-zarhus>
    * Linkedin: <www.linkedin.com/company/crosscon-eu>
    * Website: <crosscon.eu>
    * GitHub: <github.com/crosscon>

<br><br><br><br>

::right::

<div class="flex justify-center items-center">
  <img src="/../img/crosscon-logo-2.png" width="200px" align="right">
</div>

---
layout: two-cols-header
---

### The CROSSCON Hypervisor

::left::

Features:
- A static partitioning hypervisor
    * Static CPU cores assignement
    * Static interrupts assignement
    * Static memory and devices assignement
- Has a scheduler for platforms with one CPU
- ARM TrustZone and SGX enclaves TEE emulation
- Multiple TEE support
- Support for multiple architectures, including ARM and RISC-V

GitHub: <github.com/crosscon/CROSSCON-Hypervisor>

<br><br><br><br>

::right::

<div class="flex justify-center items-center">
  <img src="/../img/crosscon-logo-2.png" width="200px" align="right">
</div>

---
layout: two-cols-header
---

## The Zephyr RTOS demo

::left::

The goals:
- To run a Zephyr RTOS application with some network device access inside the
  CROSSCON Hypervisor virtual machine on LPCXpresso55S69 (the VM1 from the
  diagram above).
- To run two CROSSCON Hypervisor virtual machines side-by-side on
  LPCXpresso55S69, where one virtual machine runs some bare-metal application
  (the VM0 from the diagram above) and the second one runs the application from
  the first goal.

<br><br>

::right::

<div class="flex justify-center items-center">
  <img src="/../img/dhcp-crosscon-zdm.png" width="100%" align="right">
</div>

---
layout: two-cols-header
---

## The Zephyr RTOS demo

::left::

Prerequisites:
- LPCXpresso55S69 board with additional UART converters.
- MIKROE-2542 Wi-FI module.
- Zephyr RTOS DHCP client demo.
- Some Zephyr RTOS development experience.

::right::

<div class="flex justify-center items-center">
  <img src="/../img/lpc.jpg" width="350px" align="right">
</div>

<br><br>

---

## VM entry point

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

## VM memory assignment

Two memory address ranges should be reserved, SRAM and FLASH:

```c
(...)
.regions =  (struct vm_mem_region[]) {
    {
        .base = 0x20020000, //SRAM
        .size = 0x10000
    },
    {
        .base = 0x00040000, //FLASH
        .size = 0x10000
    }
},
(...)
```

---

## VM devices assignment

In the Hypervisor config:

```diff
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

Assign the RNG to the VM. No Zephyr RTOS devicetree changes needed.

---

## VM devices assignment

Separate UART interfaces had to be set up for the Wi-Fi module and console logs.

```diff
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

## VM devices assignment

After reassingning the UART in the Zephyr RTOS device tree change the CROSSCON
Hypervisor configuration:

```diff
(...)
.devs =  (struct vm_dev_region[]) {
    {
        /* Flexcomm Interface 2 (USART2) */
            /* AND */
            /* Flexcomm Interface 3 (USART3) */
            .pa = 0x40088000,
            .va = 0x40088000,
            .size = 0x2000,
            .interrupt_num = 2,
            .interrupts = (irqid_t[]) {16+16, 17+16}
        },
(...)
```

---
layout: two-cols-header
---

## Implementation

::left::

- After some problems with the CROSSCON Hypervisor scheduler and ARM
TrustZone SAU component, we managed to run the application!
- Check out <blog.3mdeb.com> page for the blog post that will cover this
topic in depth.

::right::

<center><img src="/../img/hv-wifi-app.png" width="350px"></center>

<br><br>

---
layout: cover
background: /intro.png
class: text-center
---

## Q&A

<center>
  <img src="/../img/zarhus_logo.png" width="150px">
</center>
