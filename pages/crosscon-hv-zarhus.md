---
layout: cover
background: /intro.png
class: text-center
---

## Zarhus with rootfs on CROSSCON Hypervisor

<center>
    <img src="/img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---

## Who am I?

<div class="grid grid-cols-2 gap-8">

<div>

**Wiktor Grzywacz**

_Junior Embedded Systems Developer_

- <wiktor.grzywacz@3mdeb.com>
- [3mdeb.com](https://3mdeb.com)

</div>

<div class="flex justify-center items-center">
  <img src="/img/zarhus_logo.png" height="220px" style="filter: invert(1)"/>
</div>

</div>

---

## Agenda

<v-clicks>

- CROSSCON Hypervisor Recap
- Why a full rootFS for Zarhus OS?
- Build Steps & Reference Guide
- Current Status & Demo
- Roadmap & Next Steps
- Q&A

</v-clicks>

---
layout: two-cols-header
---

## CROSSCON Hypervisor Recap

<center><img src="/crosscon-logo.png" height="220px"></center>

<v-clicks>

- Repo with demos available [here](https://github.com/crosscon/CROSSCON-Hypervisor-and-TEE-Isolation-Demos/)
- Based on [Bao Hypervisor](https://github.com/bao-project/bao-hypervisor)

</v-clicks>

::left::

<v-clicks>

### Buildroot initramfs constraints

- Minimal shell/tools
- Dev/debug workflow limited

</v-clicks>

::right::

<v-clicks>

### Zarhus Full RootFS benefits

- Yocto-based: easy to add new recipes
- Compilers, linkers, etc.
- Ability to test easier
- Is a "full" distro on the Hypervisor

</v-clicks>

---

## Build Steps & Guide

<v-clicks>

1. **Yocto Environment Setup**
    - Building Zarhus for `raspberrypi4-64`
2. **CROSSCON Configuration**
   - Assign CPU/mem/devices
   - Tweak device tree file
3. **Putting it all together**
    - Flash SD properly
4. **Deploy & Validate**
   - Boot Zarhus with rootfs VM on RPi4

Full guide [in the Zarhus docs](https://docs.zarhus.com/guides/rpi4-crosscon-hypervisor/)

</v-clicks>

---

## Current Status & Demo

<v-clicks>

**Working:**
- Zarhus kernel working on the CROSSCON Hypervisor
- `rootfs` mounting properly
- Serial port issues fixed
- Working linux environment

</v-clicks>

---

## Roadmap

<v-clicks>

**Next Steps:**
- `xtest` and full `OPTEE-OS` support
> Currently working on it in
[this PR](https://github.com/zarhus/meta-zarhus/pull/54)
- Finding a **fix**, not a workaround to the `magic printk` issue

</v-clicks>

---

## Q&A

<center>
  <img src="/img/zarhus_logo.png" width="300px" style="margin-left:-20px;filter: invert(1);">
</center>
