---
theme: ../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## Dasharo Tools Suite: development and testing insights, roadmap

<center>
    <img src="../../img/zarhus_logo.png" width="150px"
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

<img src="../../img/daniil.klimuk.webp" width="45%" />

**Daniil Klimuk**

_Zarhus team leader, embedded and Linux enthusiast_

<daniil.klimuk@3mdeb.com> : [3mdeb.com](https://3mdeb.com)

</center>

::right::

<div class="flex justify-center items-center">
  <img src="../../img/zarhus_logo.png" height="220px" />
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

- What is DTS?
- DTS in Dasharo Universe
- DTS status
- DTS development and testing insights
- DTS roadmap

::right::

<center>
  <img src="/slides/img/0x3/maintaining-and-testing-dts.png" width="600" style="margin-left:-20px">
</center>

---
layout: two-cols-header
---

### What is DTS?

<center>
  <img src="/slides/img/solid-and-secure-bridge.png" width="600" style="margin-left:-20px">
</center>

Initial goals:
* Support end-users while deploying Dasharo firmware.
* Support Dasharo firmware developers during firmware development.

---
layout: two-cols-header
---

### What is DTS?

::left::

<center>
  <img src="/slides/img/0x3/dts-main-menu-screen.png" width="450" style="margin-left:-20px">
</center>

::right::

* A set of tools running in a Yocto-based image.
* Dasharo Zero Touch Initial Deployment (i.e. DZTID), that is, a list of
  automated workflows:
  * Initial deployment for Dasharo firmware.
  * Update for Dasharo firmware.
  * Transition for Dasharo firmware.
* Dasharo Hardware Compatibility List Report (i.e. Dasharo HCL or DTS HCL; you
  can find more about it [here][dasharo-hcl-docs]).
* Fusing workflow for some Dasharo firmware (for more information about
  fusing check [Dasharo documentation][fusing-docs].
* Firmware recovery workflow.

---

## DTS in Dasharo Universe

<center>
  <img src="/slides/img/0x3/dts-in-dasharo-universe.png" width="700" style="margin-left:-20px">
</center>

<br>

<center>DTS is a key component in Dasharo Universe!</center>

---
layout: two-cols-header
---

## DTS status: releases vs key features implemented

::left::

TODO

::right::

TODO

---
layout: two-cols-header
---

## DTS status: issues

::left::

TODO

::right::

TODO

---

## DTS status: contributions

TODO

---

## DTS development and testing insights: challenges

<center>
  <img src="/slides/img/0x3/dts-mess-diagram.svg" width="700" style="margin-left:-20px">
</center>

---

## DTS development and testing insights: challenges

<center>
  <img src="/slides/img/0x3/dts-not-mess.svg" width="700" style="margin-left:-20px">
</center>

---

## DTS development and testing insights: black box testing

<br>

<center>
  <img src="/slides/img/0x3/dts-e2e-black-box.svg" width="700" style="margin-left:-20px">
</center>

---

## DTS development and testing insights: use case testing

<br>

<center>
  <img src="/slides/img/0x3/dts-e2e-success-and-error-paths.svg" width="600" style="margin-left:-20px">
</center>

---

## DTS development and testing insights: testing architectures

<br>
<br>
<br>

<center>
  <img src="/slides/img/0x3/dts-testing-architecture.svg" width="700" style="margin-left:-20px">
</center>

<br>
<br>

<center>Two new fully automatic testing architectures: "Testing on QEMU" and
"Testing in CI/CD workflows".</center>

---
layout: two-cols-header
---

## DTS development and testing insights: testing workflows

::left::

<center>"Testing on real hardware"</center>

<center>
  <img src="/slides/img/0x3/dts-testing-on-hardware-workflow.svg" width="370" style="margin-left:-20px">
</center>

::right::

<center>"Testing on QEMU" and "Testing in CI/CD workflows"</center>

<center>
  <img src="/slides/img/0x3/dts-testing-on-qemu-workflow.svg" width="250" style="margin-left:-20px">
</center>

---

## DTS roadmap: v2.7.2

TODO

---

## DTS roadmap: future releases

TODO

---
layout: cover
background: /intro.png
class: text-center
---

## Q&A

<center>
  <img src="../../img/zarhus_logo.png" width="150px">
</center>
