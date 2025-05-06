---
layout: cover
background: /intro.png
class: text-center
---

## ZarhusBMC: The Beginning - Porting OpenBMC to the X11SSH Platform

<center>
    <img src="/img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---

## Who am I?

<div class="grid grid-cols-2 gap-8">

<div>

**Mateusz Kusiak**

_Former System Software Development Engineer at Intel_

_Currently a Junior Embedded Systems Developer at 3mdeb_

_Member of the **Zarhus** team_

- <mateusz.kusiak@3mdeb.com>
- [3mdeb.com](https://3mdeb.com)

</div>

<div class="flex justify-center items-center">
  <img src="/img/zarhus_logo.png" height="220px" style="filter: invert(1)"/>
</div>

</div>

<!--
Key points to make:
* Used to develop Intel VROC,as a part of the job developed mdadm
* Newest member of Zarhus team
-->

---

## Agenda

<v-clicks>

- What's BMC/OpenBMC?
- Current state of the upstream
- Building x11ssh configuration
- Demo
- Next Steps
- Q&A

</v-clicks>

---

## Key factors

<v-clicks>

- BMC - A small system within a computer system for managing the main system.
    > A Baseboard Management Controller, or BMC, is a specialized
    microcontroller embedded on the motherboard of servers and high-end
    computers. Its primary function is to provide out-of-band remote management
    capabilities for the system, meaning it allows administrators to monitor and
    manage servers remotely, regardless of the server's operating system or
    whether the server is turned on.

    _Source: [Supermicro](https://www.supermicro.com/en/glossary/baseboard-management-controller)_
- OpenBMC - an alternative firmware for BMCs.
    > OpenBMC is a Linux distribution for management controllers used in devices
    such as servers, top of rack switches or RAID appliances.

    _Source: [OpenBMC](https://github.com/openbmc/openbmc)_
- Can one trust unauditable code?

</v-clicks>

<!--
Key points to make:
* BMC
  * Let's get up to speed on BMCs
  * Came up with the definition myself.
  * [DO THE ANALOGY TO TWO SYSTEMS ON A SINGLE MOTHERBOARD]
  * It's kinda ironic I quoted the definition from the ventor whose firmware
  we'll be replacing.
  * The BMC does not have to be a microcontroller, it much be much proper to
  replace "microcontroller" with SoC
  * Make analogy to more advanced, and tightly integrated KVM.
* OpenBMC:
  * Various components have various licenses: GPL, Apache, MIT
  * Publicly available code
  * Features:
   * Remote Management and Monitoring (Power control, health monitoring)
   * KVM (Keyboard, Video, Mouse) and Serial over IP
   * System Firmware updates
   * etc.
   * After all, the auditability of the code.
* Unauditable code:
  * Stock firmware are:
    * black boxes, no one knows what's running inside.
    * might be a security vulnerable.
    * might not get patched when support ends.
    * might require subscription or  additional license to run, despite hardware
    being there
  * OpenBMC:
    * give control of your machine back to you,
    * is auditable,
    * can be kept up to date,
    * free as in free will.
-->

---

## OpenBMC upstream status

<v-clicks>

- Yocto based project
- Last release `2.14.0` dated at 16/05/2023 (almost 2 years ago)
- Actively developed
- [Public CI](https://jenkins.openbmc.org/job/ci-openbmc/) set up
    ![OpenBMC CI](/img/openbmc_ci.png)
- *Claims* to support many platforms already, including the X11SPI
- Does it tho?
- Honorable mention: Pionieers:
[Hardened Vault](https://hardenedvault.net/blog/2024-03-15-openbmc-x11ssh-port/)

</v-clicks>

<!--
Key points to make:
* Only some of the targets/platforms are being CI tested.
* The folks at OpenBMC have a different definition of "supported".
If a platform is not regularly tested in CI, you can't be certain that it
actually works, thus it's hard to call it supported.
* That indeed was an issue, but I'll talk about on the next slide.
* HardenedVault were first to run run OpenBMC on x11ssh on a real hardware.
* I learned very late in development about their blogpost, but thanks to them
figuring out console redirection was a breeze.
-->

---

## Building X11SSH configuration

<pre class="font-mono bg-black text-white rounded max-w-full max-h-[45vh] text-sm leading-none">
  <v-clicks>
    <span>
      [<span class="text-red-500 font-bold">FAILED</span>] Built X11SPI base configuration
    </span>
    <span>
      [<span class="text-green-400 font-bold">  OK  </span>] Prepared X11SSH config
    </span>
    <span>
      [<span class="text-red-500 font-bold">FAILED</span>] Built X11SSH config
    </span>
    <span>
      [<span class="text-green-400 font-bold">  OK  </span>] Removed features for X11SSH, built X11SSH config
    </span>
    <span>
      [<span class="text-red-500 font-bold">FAILED</span>] Booted built image under QEMU
    </span>
    <span>
      [<span class="text-green-400 font-bold">  OK  </span>] Fixed bmcweb.service watchdog issue
    </span>
    <span>
      [<span class="text-green-400 font-bold">  OK  </span>] Fixed system manager issue
    </span>
    <span>
      [<span class="text-green-400 font-bold">  OK  </span>] Booted built image under QEMU
    </span>
    <span>
      [<span class="text-green-400 font-bold">  OK  </span>] Redirect the console
    </span>
    <span>
      [<span class="text-green-400 font-bold">  OK  </span>] 🎉 Run built image on HW 🎉
    </span>
  </v-clicks>
</pre>

<!--
Key points to make:
* Attempted to build "supported" X11SPI configuration:
  * Had issues with running out of ram on 12th gen i7 system with 16G of RAM
  * Created a docker container for reproducibility and attempted to build on
  "Builder"
  * Build was failing at one of final steps. The issue squashfs was too big to
  fit within declared flash memory size
* Preparing x11ssh config:
  * Decided not to waste time fixing what should have been a "supported"
  platform configuration
  * Had it easier, we run it a few years ago, but the configuration got OUT of
  DATe. Had x11spi config to compare to.
  * Had to make config up to date and fix deprecated: variables, names, syntax,
  configuration and redo some patches.
* Building x11ssh:
  * faced same error as for x11spi, which was a success
* Removing features:
  * Removed features like: telemetry, devtools, debug and user management
  * Was able to successfully build the image.
* QEMU booting:
  * It was time to check if the image boots under QEMU
  * Flashing to the platform would be dumb at that moment
  * QEMU has support for Aspeed family boards, including AST2400 which the
  x11ssh platform uses.
  * That failed
* bmcweb.service issue:
  * responsible for web-based interface.
  * systemd was complaining about WatchdogSec variable not being set properly.
  * the issue was simple, the code set up the variable named "watchdog timeout
  seconds" while the service file expected just "watchdog timeout".
  * Strange this was merged with upstream, just as if it wasn't tested.
  * That can make one doubt product quality.
  * Worth noting that the service would probably omit that param and start
  anyway but got no way of checking that because the execution was frozen
* System manager issue:
  * major issue, made the execution freeze.
  * Found solution by looking up closed issues on github.
  * The two managers: phosphor-state-manager and x86-power-control cannot be
  embedded into a single image as they are mutually exclusive.
  * Both control low level stuff like power states.
  * Disabling x86-power-control was the solution.
  * The configuration for two managers was inherited from the common layer for
  supermicro platforms, which would mean that x11spi would suffer from the
  same issue (did not test that)
-->

---
layout: cover
background: /intro.png
class: text-center
---

##  Demo

---

## Next steps

<v-clicks>

- Exploring new fields: only natural for Yocto developers
- Expanding expertise
- Tightly integrating our solutions: Dasharo + ZarhusBMC

</v-clicks>

<!--
Key points to make:
 * Why do this? How does a custom BMC fit within our ecosystem?
-->

---

## References

References:
- [Blog post](https://blog.3mdeb.com/2025/2025-04-28-zarhusbmc/)
- [Hardened Vault blog post](https://hardenedvault.net/blog/2024-03-15-openbmc-x11ssh-port/)
- [Yocto project developer day 2023](https://www.youtube.com/watch?v=ljQg8dnyhLU)
- [OpenBMC presentation](https://3mdeb.com/events/#_yocto-project-dev-days)
- [3mdeb at FOSDEM](https://fosdem.org/2025/schedule/track/bmc/)

Resources:
- [X11SSH Gerber files](https://github.com/mithro/x11ssh-f-pcb) (Thanks to Tim Ansell)
- [OpenBMC developer docs](https://github.com/openbmc/docs/blob/master/development/README.md)
- [Flashing image via SPI](https://github.com/Keno/bmcnonsense/blob/master/blog/05-flashing3.md)
- [supermicro-x11-bmc on QEMU](https://www.qemu.org/docs/master/system/arm/aspeed.html)

---
layout: cover
---

## Q&A

<center>
  <img src="/img/zarhus_logo.png" width="300px" style="margin-left:-20px;filter: invert(1);">
</center>
