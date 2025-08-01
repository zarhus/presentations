---
theme: ../../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## ZarhusBMC: The Second Encounter - Porting OpenBMC to x11ssh part II

<center>
    <img src="/../../img/zarhus_logo.png" width="150px"
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
- [Personal site](https://danceswithmachines.github.io/)

</div>

<div class="flex justify-center items-center">
  <img src="/../../img/zarhus_logo.png" height="220px" style="filter: invert(1)"/>
</div>

</div>

---

## Agenda

<v-clicks>

- Previously on ZarhusBMC (Recap)
- Issues
- Progress
- Demo
- Next Steps and Ideas
- Q&A

</v-clicks>

---
layout: two-cols-header
---

## Previously on ZarhusBMC

::left::

<v-clicks>

- During last developer meetup:
    + Discussed what OpenBMC is and it's role in proprietary world of computing
    + Built and showcased OpenBMC running on a hardware
    + Got UART, couldn't log in to Web UI
- Rebuilt the image with user mngmt support, ditched logging
- Was able to log in via WebUI
- ...but this revealed issues.

</v-clicks>

::right::

<center>
  <img src="/../../img/0x2/x11ssh_mobo.jpg"/>
</center>

<!--
Points to make:
 * What is a BMC
 * Why could not I log in to WebUI
 * Got to remove some functionality so the image fitted in the flash
 * What was the issue when logged to WebUI
-->

---

## Issues

<v-clicks>

- Two major issues have revealed themselves.

  ```log
  root@x11ssh:~# systemctl list-units --type=service | grep failed
  * obmc-led-group-start@bmc_booted.service                                     loaded failed failed  Assert bmc_booted LED
  * phosphor-ipmi-kcs@ipmi-kcs3.service                                         loaded failed failed  Phosphor IPMI KCS DBus Bridge
  * xyz.openbmc_project.Chassis.Control.Power@0.service                         loaded failed failed  Intel Power Control for the Host 0
  ```

- KCS issue: Lacking KCS interfaces definitions in DTS. No communication with
  the host.

  ```log
  root@x11ssh:~# /usr/libexec/kcsbridged -c ipmi-kcs3
  FAILED: open `/dev/ipmi-kcs3`: No such file or directory
  ```

- Power state managers issue: Lacking GPIO definitions. No control over host
  power states.

  ```log
  root@x11ssh:~# /usr/bin/power-control 0
  <6> Start Chassis power control service for host : 0
  <3> BiosMux is not a recognized power-control signal name
  <3> Host0: Error in Parsing...
  <6> SIO control GPIOs not defined, disable SIO support.
  <3> PowerOk name should be configured from json config file
  ```

</v-clicks>

<!--
Points to make:
* Two major services failing.
* KCS is an interface, IPMI is a protocol.
* DTS - describes platforms hardware.
* DTSes can be vendor supplied, made according to docs. or reverse engineered.
* DTS is not something one should create by themsleves.
* We've got docs for AST2400, the addresses for KCS should be common between
  various models, it just an effort of testing it out.
* The SoC has GPIOs that probe or drive various endpoints on the motherboard.
* Unlike with KCS addresses, each vendor can wirte the SoC to their liking.
* The GPIO definitions cannot be found in docs.
* The GPIO definitions shall also be a part of DTS.
* The definitons we currently have were made by Keno Fisher as a part of u-bmc
  porting, they're insufficient.
-->

---
layout: two-cols-header
---

## Progress

::left::

<v-clicks class="text-sm">

- Community efforts: great positive feedback, opened up ZarhusBMC GH discussions
- Performed stock firmware scoping:
    + Method: `binwalk` disassembly, `QEMU` emulation
    + Expectations: DTBs, GPIO defs., interface scoping 🫠
- Obtained UART access for stock FW:
    + Method: Following Keno Fisher's work, tracing back the connections (Thanks
    to Tim Ansell), finding `RX` pin to pair (with docs).
    + Expectations: Stock FW UART access 💯
- Scoping on a real HW:
    + Method: check binaries, `sysfs`, platform states
    + Expectations: Confirm suspicions, assess possibilities 🔍

</v-clicks>

::right::

<div class="h-full flex flex-col items-center gap-1">
  <img src="/../../img/0x2/x11ssh_grbr.gif" class="max-h-[25%] w-auto object-contain"/>
  <img src="/../../img/0x2/x11ssh_hackjob.jpg" class="max-h-[25%] w-auto object-contain"/>
</div>

<!--
Points to make:
* Running image under QEMU: It was debatable how trustworthy are since many
  services were failing due to the lack of hardware.

* Accessing UART was done in the past by Keno Fisher author of U-BMC port.
* Keno managed to find UART TX pin only.
* Tracing was possible thank's to the Tim Ansell who provided Gerber files.
* UART: We had UART access on our OpenBMC port because we redirected UART in
  u-boot configuration, stock firmware has stock UART.

* All services started properly
* Only binaries marked as tool were usable, other gave segfaults
* Did not find obvious way to drive or probe UART, but devs left devmem binary
* By changing platform states we could peek the GPIO registers.
* In case of backtracing, we've reduced GPIO number from 216 to under 15.
-->

---
layout: cover
background: /intro.png
class: text-center
---

## Demo

---

## Next steps and Ideas

<v-clicks>

- Attempt configuring KCS in device tree
- Perform probing from the host side
- Address the GPIO
- (Maybe) develop some tooling for easier porting 😉
- More platforms await

</v-clicks>

---

## References

Special thanks:
- Keno Fisher
- Tim Ansell

References:
- [Blogpost](#FIX ME)
- [ZarhusBMC discussions pane](https://github.com/zarhus/zarhusbmc/discussions)
- [Keno's blog post](https://github.com/Keno/bmcnonsense/blob/master/blog/03-serial2.md)
- [x11ssh Gerbers (Tim Ansell)](https://github.com/mithro/x11ssh-f-pcb)

---
layout: cover
---

## Q&A

<!-- markdownlint-disable MD013 -->

<center>
  <img src="/../../img/zarhus_logo.png" width="300px" style="margin-left:-20px;filter: invert(1);">
</center>

<!-- markdownlint-enable MD013 -->
