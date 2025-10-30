---
theme: ./theme
background: /intro.png
# some information about your slides (markdown enabled)
title: 'Context Based Authentication: Identifying host by environment'
info: false
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
---

## Context Based Auth.: Identifying host by environment

<center>
    <img src="../../img/0x3/tnc.jpg" width="70%" style="margin-left:-20px;">
</center>

---

## echo $(whoami)

<div class="grid grid-cols-2 gap-8">

<div>

**Mateusz Kusiak**

_Former System Software Development Engineer at Intel_

_Currently a Junior Embedded Systems Developer at 3mdeb_

_Member of the **Zarhus** team_

- <mateusz.kusiak@3mdeb.com>
- [3mdeb.com](https://3mdeb.com)
- [Personal site](https://danceswithmachines.github.io/)

</div>
<div class="flex justify-center items-center">
<img src="../../img/zarhus_logo.png" height="220px" style="filter: invert(1)"/>
</div>

</div>

---

## Location based authentication

<v-clicks>

- Issues with classic geofencing
- Classic CBA
- RFF (Radio Frequency Fingerprinting)
- D2D CBA
- My concerns:
  + Probing resolution
  + Why not use classic identifiers: MAC, IP, etc.

</v-clicks>

---

## Crosscon and the stack

<v-clicks>

- CROSSCON (Cross-Platform Open Security Stack for Connected Devices)
- Main product: [CROSSCON Hypervisor](https://github.com/crosscon/CROSSCON-Hypervisor)
- Stack...
    <div class="flex justify-center items-center">
        <img src="../../img/0x3/tls-uc1-2-cba-integration.png"
        width=73% style="filter: invert(1)"/>
    </div>

</v-clicks>

---

## **HARD**ware

<div class="flex justify-center items-center">
    <img src="../../img/0x3/crscn_cba.jpg" width=52%/>
</div>

---
layout: cover
class: text-center
---

## Demo

---

## References

References:
- [Crosscon CBA approach](https://crosscon.eu/sites/crosscon/files/public/content-files/2025-03/D3.1%20CROSSCON%20Open%20Security%20Stack%20Documentation%20%E2%80%90%20Draft_v1.0.pdf)
- [Crosscon](https://crosscon.eu/)
- [Crosscon Build system for RPI](https://github.com/crosscon/crosscon-demos-uc12)
- [Crosscon TLS application](https://github.com/crosscon/uc1-2-integration)
- [Reproduction manual](https://github.com/crosscon/uc1-2-integration/blob/main/README.md)
---
layout: cover
---

## Q&A

<center>
  <img src="../../img/zarhus_logo.png" width="300px"
   style="margin-left:-20px;filter: invert(1);">
</center>

---
src: <SRC>
---
