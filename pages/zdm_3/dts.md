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

<br>

For the dipper dive into tech details and reports check out the blog post that
will be published soon on <https://blog.3mdeb.com/>.

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
theme: ../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## Dasharo Tools Suite status: releases and statistics

<center>
    <img src="../../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---
layout: two-cols-header
---

## DTS status: releases vs key features implemented

<br>

<center>
  <img src="/slides/img/0x3/dts-releases.svg" width="700" style="margin-left:-20px">
</center>

The key features: news firmware support (for several platforms, including:
**MSI PRO Z690-A**, **MSI PRO Z790-A**, **NovaCustom V540TU**, **Novacustom
V560TU**, etc.), a **fusing workflow** for NovaCustom V540TU and Novacustom
V560TU, and a DTS End To End testing methodology.

For more information check <https://github.com/Dasharo/meta-dts/releases>

---

## DTS status: issues

<center>
  <img src="/slides/img/0x3/dts-issues.png" width="700" style="margin-left:-20px">
</center>

---

## DTS status: Dasharo/meta-dts PRs

<center>
  <img src="/slides/img/0x3/meta-dts-prs.png" width="700" style="margin-left:-20px">
</center>

---

## DTS status: Dasharo/dts-scripts PRs

<center>
  <img src="/slides/img/0x3/dts-scripts-prs.png" width="700" style="margin-left:-20px">
</center>

---

## DTS status: Dasharo/dts-configss PRs

<center>
  <img src="/slides/img/0x3/dts-configs-prs.png" width="700" style="margin-left:-20px">
</center>

---

## DTS status: contributions

<br>

<center>A contribution to flashrom project from Zarhus Team!</center>

<br>

<center>
  <img src="/slides/img/0x3/dts-contribution.png" width="700" style="margin-left:-20px">
</center>

For more information check <https://review.coreboot.org/c/flashrom/+/89222> and
<https://github.com/Dasharo/dasharo-issues/issues/952>.

---
theme: ../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## Dasharo Tools Suite development and testing insights: a new DTS End to End testing methodology

<center>
    <img src="../../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

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
theme: ../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## Dasharo Tools Suite roadmap: What is next?

<center>
    <img src="../../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---
layout: two-cols-header
---

## DTS roadmap: v2.7.2

::left::

The key features:
* Fully separated UI that will be shared between other Dasharo and Zarhus
  projects.
* Full platforms metadata migratoin to `Dasharo/dts-configs`.
* Publishing DTS E2E test results on OSFV Dashboard.
* Some minor fixes.

For more information check
<https://github.com/Dasharo/dasharo-issues/milestone/85>.

::right::

<center>
  <img src="/slides/img/0x3/dts-zpb-ui-sharing.png" width="300" style="margin-left:-20px">
</center>

---
layout: two-cols-header
---

## DTS roadmap: future releases

::left::

<br>
<br>
<br>
<br>

<center>
  <img src="/slides/img/0x3/dts-in-dasharo-universe.png" width="500" style="margin-left:-20px">
</center>

::right::

* Further integrate DTS with other members of Dasharo Universe:
  - fwupd?
  - Further integration with Zarhus Provisioning Box for Root of Trust and Chain
    of Trust verification and atteststion.
  - HCL and other atteststion procedures developed alongise ZarhusBMC.
* New platforms and firmware support:
  - Servers: Gigabyte MZ33-AR1, ASRock Rack SPC741D8-2L2T/BCM, and others.
  - Others: NovaCustom laptops, NovaCustom NUC Box, MSI PRO Z690-A and MSI PRO
    Z790-P, and others.

---
layout: cover
background: /intro.png
class: text-center
---

## Q&A

<center>
  <img src="../../img/zarhus_logo.png" width="150px">
</center>
