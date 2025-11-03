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

<!--
Hello everyone! Today I will talk about virtualization on MCU and how to achieve
it with CROSSCON Hypervisor.
-->

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

<!--
My name is Daniil and I am the 3mdeb's Zarhus Team leader. A a bookworm, a
cycling neerd, Linux kernel and embedded programming enthusiast.
-->

---
layout: two-cols-header
---

## Agenda

::left::

- The CROSSCON Project
- The CROSSCON Hypervisor
- The Zephyr RTOS demo
- Implementation
- The results
- Q&A

::right::

<div class="flex justify-center items-center">
  <img src="/../img/zdm-2-logo-crosscon-hyp-dhcp-demo.png" height="220px" />
</div>

<!--
This talk will cover general information that is needed for you to port and
launch your application on top of the CROSSCON Hypervisor. We will go through
the CROSSCON Project introduction. Then we will discuss the CROSSCON Hypervisor
and its features. After this we will cover the some of the demo and its
implementation details.
-->

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

<!--

The CROSSCON Project focuses on security for IoT devices, providing components
that increase the security (the CROSSCON hypervisor, multi factor
authentication), as well as use cases, that demonstrate the improvements
delivered to real world.

We have already had one presentation and blogpost that cover launching the
CROSSCON Hypervisor on RPi platforms. If you are interested in the security,
virtualization and Linux kernel make sure to check it on the blog.3mdeb.com.

-->

---
layout: two-cols-header
---

### The CROSSCON Hypervisor

::left::

Features:
- A static partitioning hypervisor
  * Static CPU cores assignment
  * Static interrupts assignment
  * Static memory and devices assignment
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

<!--

The CROSSCON Hypervisor is a static partitioning hypervisor, that means you are
responsible for managing all the platform resources at build time. Though it is
a static partitioning hypervisor it can be launched on platforms with only one
core available. For that the hypervisor uses a simple round-robin scheduler.

The CROSSCON Hypervisor does not have a lot of emulation built in. It assign
most of the resources directly to the virtual machines. That means it is not
possible to have two virtual machines assign the same device. The only thing
that is important from the user point of view and the CROSSCON Hypervisor does
emulate is the ARM TrustZone and SGX enclaves technoloogies for Trusted
Execution Environment.

Because the CROSSCON Hypervisor does emulate the ARM TrustZone and SGX
technologies it is now possible to have not only multiple VMs but multiple TEE
on one platform. And the hypervisor does have a lot of freedom when configuring
the TEE access. For example, some virtual machines can have several TEE VM
assigned.

The CROSSCON Hypervisor supports several platforms and architectures, including
the most popular in the embedded world: ARM and RISC-V.

-->

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

<!--

Here is the architecture for our demo. This demo is a preparation for one of the
CROSSCON Projects real world use cases: the two-factor authentication using
Physical unclonable function.

It features two VMs with one VM being a simple bare-metal application that is
needed for testing two VM's configuration and the

-->

---
layout: two-cols-header
---

## The Zephyr RTOS demo

::left::

The things to consider when launching smth. on top of the CROSSCON Hypervisor:
- Set the application entry and load addresses.
- Assign memory to the virtual machine in which the application will be running.
- Assign memory and interrupts to the memory-mapped peripherals.

::right::

<div class="flex justify-center items-center">
  <img src="/../img/dhcp-crosscon-zdm.png" width="100%" align="right">
</div>

<br><br><br><br><br>

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

## The results

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
