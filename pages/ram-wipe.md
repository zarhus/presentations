---
layout: cover
background: /intro.png
class: text-center
---

## Kicksecure's ram-wipe against RAM attacks

<center>
    <img src="/img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---
layout: two-cols-header
---

## Who am I?

::left::

<center>

<br>

<img src="/img/daniil.klimuk.webp" width="45%" />

**Daniil Klimuk**

_Zarhus team leader, embedded and Linux enthusiast_

<daniil.klimuk@3mdeb.com> : [3mdeb.com](https://3mdeb.com)

</center>

::right::

<div class="flex justify-center items-center">
  <img src="/img/zarhus_logo.png" height="220px" />
</div>

---

## Agenda

- The `ram-wipe`, a solution against RAM attacks
- RAM attacks: warm boot attack vs cold boot attack
- `ram-wipe` - structure and workflow
- `ram-wipe` - testing environment and methodology
- `ram-wipe` - testing results
- Conclusions
- Q&A

---
layout: two-cols-header
---

## The `ram-wipe`: a solution against RAM attacks

::left::

<center>

What is the `ram-wipe`?

</center>

- Is the Kicksecure's solution (<www.kicksecure.com>)
- Is a fully software solution based on Linux executables, shell scripts, dracut
  and its modules
- Is open source: `github.com/kicksecure/ram-wipe`
- Is under AGPL-3+ license
- Is in testing stage

<center>

The goal: <b> to protect from cold boot attacks </b>

</center>

<!-- Tails Memory Erasure -->

::right::

<center><img src="/img/ram-wipe-logo.svg" width="80%" /></center>

<br>
<br>

---

## RAM attacks: warm boot attack vs cold boot attack

<center><img src="/img/warm-vs-cold-boot-attack.svg" width="65%" /></center>

<br>
<center>The key difference: malware boot process.</center>

---
layout: two-cols-header
---

## `ram-wipe`: booting up

::left::

<center><img src="/img/ram-wipe-flowchart-1.svg" width="70%" /></center>

::right::

<br>
<br>
<br>
<br>
<br>

<center>
<b>Important note here:</b>
<br>

`ram-wipe` depends on boot-time services

</center>

---
layout: two-cols-header
---

## `ram-wipe`: inside rootfs

::left::

<center><img src="/img/ram-wipe-flowchart-2.svg" width="80%" /></center>

::right::

<br>
<br>
<br>
<br>
<br>

<center>
<b>Important note here:</b>
<br>

`ram-wipe` depends on shutdown/reboot/halt -time services as well

</center>

---
layout: two-cols-header
---

## `ram-wipe`: first stage

::left::

<center><img src="/img/ram-wipe-flowchart-3.svg" width="90%" /></center>

::right::

<br>
<br>
<br>
<br>

<center>
<b>Important notes here:</b>
<br>

`ram-wipe` checks Linux kernel command line parameters

`sdmem -l -l -v` is being used for wiping

The `kexec` starts the second stage

</center>

---
layout: two-cols-header
---

## `ram-wipe`: second stage

::left::

<center><img src="/img/ram-wipe-flowchart-4.svg" width="60%" /></center>

::right::

<br>
<br>
<br>
<br>

<center>
<b>Important notes here:</b>
<br>

`ram-wipe` executes during second kernel boot up

`ram-wipe` checks Linux kernel command line parameters

`sdmem -l -l -v` is being used for wiping

</center>

---
layout: two-cols-header
---

## `ram-wipe`: testing environment and methodology

::left::

<center><img src="/img/ram-wipe-testing-env.svg" width="90%" /></center>

<br>
<br>
<br>
<br>

::right::

<b>The test cases:</b>
- Checking what memory are being wiped
- Trying to dump LUKS keys

<br>

<b>The methodology:</b>
1. Make sure, that dumped RAM will not contain any firmware data
2. Launch the Debian Trixie with `ram-wipe`
3. Do an attack
4. Dump the RAM

<br>

---

## `ram-wipe`: testing results

Warm boot attacks:
- <b>Not zeroed</b> privileged memory: Linux kernel and GRUB address spaces
- <b>Not zeroed</b> unprivileged memory: currently executed processes address
  space
- Zeroed: memory not used by processes or system code
- LUKS keys were not dumped

Cold boot attacks:
- Memory <b>was not</b> zeroed completely
- LUKS keys <b>were dumped</b>

<center>

More results and detailed step-by-step explanation on 3mdeb's
(<www.linkedin.com/company/3mdeb>) and my
(<www.linkedin.com/in/daniil-klimuk-9358a1271>) Linkedin pages soon!

</center>

---

## Conclusions

Warm boot attacks:
- `ram-wipe` cannot wipe RAM used by kernel, because it is an application that
  is not allowed to modify Linux kernel address space.
- `ram-wipe` wipes memory previously used by processes, but it cannot wipe RAM
  of currently executed processes.

<center>

The problem: <b>make sure that your secrets are wiped!</b>

</center>

Cold boot attacks:

<center>

The problem: <b>the entire solution relies on software execution flow that is
being interrupted during cold attacks!</b>

</center>

---
layout: cover
background: /intro.png
class: text-center
---

## Q&A

<center>
  <img src="/img/zarhus_logo.png" width="150px" style="margin-left:-20px">
</center>
