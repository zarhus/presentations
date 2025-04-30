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

_member of the **Zarhus** team_

- <wiktor.grzywacz@3mdeb.com>
- [3mdeb.com](https://3mdeb.com)

</div>

<div class="flex justify-center items-center">
  <img src="/img/zarhus_logo.png" height="220px" style="filter: invert(1)"/>
</div>

</div>

<!--
introduce myself:
* hello
* I'm Wiktor
* Thank you for joining my presentation
* etc...
-->

---

## Agenda

<v-clicks>

- CROSSCON Hypervisor Recap
- Why a full rootFS/Zarhus?
- Build Steps & Reference Guide
- Current Status & Demo
- Roadmap & Next Steps
- Q&A

</v-clicks>

<!--
say:
* this is the agenda for today
* we will go over each one of these topics one by one

then:
* first, a quick recap of what CROSSCON and it's Hypervisor are
* why do we need a full rootfs on there
* quickly mention how it's done
* briefly cover what's next
* finally a Q&A
-->

---
layout: two-cols-header
---

## CROSSCON Hypervisor Recap

<center><img src="/img/crosscon-logo-2.png" width="200px"></center>

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

<!--
First the recap:
* CROSSCON stands for Cross-platform Open Security Stack for Connected Devices
* it's a IoT system that focuses on security, that places emphasis on
trusted services offered by trusted execution environments
* it's open-source, and designed to be portable, modular and vendor-independent
* there are demos available for different platforms (mainly QEMU and the RPi4)

constraints:
* the demo for the RPi4 uses a Buildroot initramfs
* this makes working with trusted applications difficult - it would be nice
to be able to make recipes for them instead of cross-compilation
* lack of compilers/tools makes gathering logs/running simple PoC programs
for security tests a lot more tedious than it needs to be
-->

---
layout: two-cols-header
---

## Build Steps & Guide

::left::

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

[Blog post](https://blog.3mdeb.com/2025/2025-04-10-crosscon-its-hypervisor-and-zarhus/)

</v-clicks>

::right::

<center>
  <img src="/img/zarhus_logo.png" width="200" style="filter: invert(1); margin-bottom: 20px;" />
  <img src="/img/yocto-logo.png" width="200" style="filter: invert(1);" />
</center>

<!--
there are a couple of steps that need to be done correctly in order to get our
Zarhus setup to work:
1. first we need to build Zarhus using Yocto
2. then, make sure that the CROSSCON configuration is right:
    * that means assigning, for example the network device
    * tweaking device tree file - bootargs, for serial and rootfs mounting
3. then we need to flash the SD properly, say that we use the bmap and gz files
to flash instead of manually formatting the SD card like in the demo since we
need two partitions
4. then finally we can boot and login

The full guide on how to do all of this can be found here.

I also wrote a blog post about the whole debugging process I went through in
order to get this to work.
-->

---

## Current Status

<v-clicks>

**Working:**

<v-click>

* Zarhus kernel working on the CROSSCON Hypervisor
</v-click>

<v-click>

* `rootfs` mounting properly
</v-click>

<v-click>

* Serial port issues fixed
</v-click>

<v-click>

* Working linux environment
</v-click>

[Blog post](https://blog.3mdeb.com/2025/2025-04-10-crosscon-its-hypervisor-and-zarhus/)

</v-clicks>

<!--
mention how all of these things allow us:
* seamless integration of future tools/apps - just make a recipe and that's it
* easy gathering of logs

If you are interested in the technical aspects of this integration - the
challenges that had to be overcome and the thought processes behind the
approach I took to tackle them, you can visit the blog post - it's about 10
minutes of relatively light reading
-->

---
layout: cover
background: /intro.png
class: text-center
---

##  Demo


<!--
say something like time to now showcase this setup in action (?)
since i assume in this section i will actually switch to the terminal,
open up minicom and show how it boots/works (?)
-->

---

## Roadmap

<v-clicks>

**Next Steps:**
* `xtest` and full `OPTEE-OS` support
> Currently working on it in
[this PR](https://github.com/zarhus/meta-zarhus/pull/54)
* Finding a **fix**, not a workaround to the `magic printk` issue

If you would like to contribute/have some clues/feedback:
* feel free to contribute to the `magic printk` issue
[here](https://github.com/crosscon/CROSSCON-Hypervisor-and-TEE-Isolation-Demos/issues/8#issuecomment-2810046951)
* you can add to the [existing PR](https://github.com/zarhus/meta-zarhus/pull/54)
* or raise an issue in [`meta-zarhus` repo](https://github.com/zarhus/meta-zarhus/issues)
* always a good idea to join the conversation in the [Zarhus Matrix Workspace](https://matrix.to/#/#zarhus:matrix.org)

Finally for the tinkerers:
* the image is available
[here](https://cloud.3mdeb.com/index.php/s/4ogfcMPRrKx5YZ2) and
[here](https://cloud.3mdeb.com/index.php/s/tGkgdawz8rE8m7E)
</v-clicks>

<!--
say that:
* an integral part of the CROSSCON stack is all the stuff related to TEE's.
making sure that `xtest` is working correctly is a good indication that
everything is correctly supported.
* I have done work in this PR so far, I think it's pretty close but right
now running into problems with `OPTEE-OS` VM, TA-dump and crashes
* while the `magic prinkt` issue doesn't alter the functionality of the setup,
it's very annoying. Finding the fix is not really within our scope of
operations though - that's more up to the developers who wrote the Hypervisor.

say that the listeners can also contribute, in the respective issue, PR or
raise general issue in meta-zarhus

tell people about the image, good option if you don't want to build everything
yourself.
-->

---
layout: cover
background: /intro.png
class: text-center
---

## Q&A

Social media links:
* [Zarhus](https://x.com/Zarhus_com)
* [CROSSCON](https://x.com/crosscon_eu)

<center>
  <img src="/img/zarhus_logo.png" width="250px" style="margin-left:-20px;filter: invert(1);">
</center>

[Zarhus docs official guide](https://docs.zarhus.com/guides/rpi4-crosscon-hypervisor/)

[Blog post](https://blog.3mdeb.com/2025/2025-04-10-crosscon-its-hypervisor-and-zarhus/)

<!--
Ask for questions, plug the guide and blog post again
-->
