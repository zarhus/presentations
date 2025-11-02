---
layout: cover
background: /intro.png
class: text-center

---
## &#x1F44B; Welcome Zarhus Developers Meetup &#9822; &#9816;

<center>
    <img src="/img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---

<center><img src="/img/0x1/banner.jpg" width="650px"></center>

<!--

We would like to give you a heads up about the vision and mission of Zarhus OS.
It is not only about marketing but also about honesty, openness, authenticity,
and accountability, which should be the foundation of every project focusing on
trustworthiness.

-->

---

<center><img src="/img/0x1/zarhus_logo.png" width="380px"></center>

_**Zarhus** is an embedded **Linux** distribution based on **Yocto**, developed
by 3mdeb. Zarhus simplified provisioning, integration and maintenance of
embedded platforms focused on strong security founded on immutable **Root of
Trust** and  leveraging the **Chain of Trust** up to the target application._

<!--

* By no mistake we want to focus on digital sovereignty.
* This is just introduction, we will talk more about our values, mission and
  vision later.

-->

---

## Zarhus Developers Meetup

<br>

- Forum where Zarhus Team and Partners share knowledge and inform about
  Zarhus-related development.
- It would be quarterly event.
- Short presentations (<20min) focused on demo.
- Little time for questions (5min after each presentation).
- Recordings will be published on YouTube.

<!--

At least we hope for event per quarter.

Format.

If no questions I will try to spin off some discussion and gather some ideas.

-->

---

## <center>&#x1F680; Zarhus Developers Meetup 0x1 Agenda &#x1F680;</center>

<br>

#### &#x1F44B; 18:00 CET Welcome Zarhus Developers Meetup, by Piotr &#x1F448;
<br>

#### &#x1F512; 18:25 CET Kicksecure's ram-wipe against RAM attacks, by Daniil
<br>

#### &#x1F4BB; 18:50 CET Cache timing attacks: How do they work?, by Michał
<br>

#### &#x1F5A5; 19:15 CET Zarhus with rootfs on the CROSSCON Hypervisor, by Wiktor
<br>

#### &#x1F9F1;&#xFE0F; 19:40 UTC OpenBMC for Supermicro x11ssh, by Mateusz
<br>

#### &#x1F44F; 18:55 UTC Zarhus Developers Meetup Closing Remarks, by Piotr

---
layout: two-cols
clicks: 8
---

#

Mission and Vision for Zarhus, Trustworthy Embedded Linux Distro.

<v-clicks>

### Mission

- Host vMeetups and F2F training confs to boost embedded systems booting and
security.
- Navigate through growing complexity of boot chain of modern computing.
- Simplifying hardware security enablement.

### Vision

- Systems become secure, trustworthy, and repairable.
- Modern tools enhances creativity and collaboration without replacing human
purpose.
- Communities can thrive with technology that respects freedom, simplicity, and
sovereignty.

</v-clicks>

::right::

<center><img src="/img/0x1/zarhus_slogan.png" width="550px"></center>

<!--
[click]
Let's start with the mission.

[click]

- First, We cannot delude ourselves; AI and LLMs are here and will not go
anywhere especially after consuming whatever data lies in their path.
- Paradigms like vibecoding or vibeopsing are new way of delivering value.
- So, Companies developing embedded software must enhance their resilience to
avoid losing the game, as it was seen in the consumer OS market. Despite that,
there may still be some hope there.
- That resiliency exists in the self-hosted and private models. Zarhus as an
embedded system boot and security-focused team cannot ignore this trend without
addressing it.
- We, definitely, would like to explore questions like:
- Who and what loads models on our shiny new hardware?
- What is the role of peripheral MCUs in the boot chain? How can we make those
components more trustworthy?
- What is the correct way of using new paradigms and tooling, while staying
independent, and keeping our digital sovereignty?
- That's why we would like to keep the discussion open and provide help when
needed via vMeetups and F2F training conferences.
- Without that, we could not attest our creation.
- In the long run, we also hope for live coding streams and sessions
- And, perhaps discussion is not always about embedded systems and software, as
we are also present in ecosystems for fully featured OSes like Qubes OS,
Kicksecure, FreeBSD, OpenWRT, Debian, Fedora, and various others.

[click]

Platforms are increasingly complex boot processes due to a lack of innovation
in operating systems, which is leading to the introduction of new peripheral
MCUs: Microsoft Pluton, Google Titan, Amazon Nitro, Apple T2, AMD Secure
Processor, Intel CSME, and OCP Caliptra.
- That is just the root of trust; there are other components coming: power
management controller, audio controller, sensors, USB-PD, etc.
- The boot process is becoming increasingly complex; this seems inevitable.
- This is not the end of the story because we often face trade-offs, with
vendors cutting corners to deliver as much flash as possible and eye-catching
experiences, often at the cost of modularity. This leads to states that are
unacceptable for upstream projects. Flashy solutions decline as quickly as
vendors lose sales volumes due to new generations of devices, which leads to a
massive amount of bit rot code, e-waste, and undermines the fundamental right
to repair. We are not extremists here, but trying to be reasonable enthusiasts
and pragmatists regarding the right to repair.
- We see it as an opportunity to provide value where we have experience:
Bootstrapping, so open boot chain, reproducible builds, and full source
bootstrapped build systems for long-term stability and the circular economy.

[click]
- Simplify enabling hardware security.
- We focus primarily on Cortex-A class devices, but we have no issue dealing
with x86, RISC-V, when powerful enough, and POWER.
- By hardware security, we mean Root of Trust, especially for measurement
because of our expertise with Trusted Computing,
- Root of Trust for Identity - where we closely look at TCG DICE
- Root of Trust for Updates - with various update schemes we implemented over
ythe ears,
- Root of Trust for Recovery - which is key to resilience of any embedded
system, and with upcoming high assurance Dynamic Root of Trust platforms can
become a reality not only in proprietary x86 world but also in ARM, POWER, and
maybe someday also in RISC-V
- Chain of Trust, often mixed as Secure Boot,
- Trusted Execution Environments and strong hardware isolation instead of
containers (and no question about that, containers also have a place in our
stack)

[click]
- Where it would lead us?

[click]

To the realm where systems become more secure, trustworthy and repairable.

[click]

Where modern tools enhance creativity and collaboration instead of replacing
humans in that.

[click]

Finally communities can thrive thanks to technology which respect freedom,
simplicity and sovereignty.

http://dl.3mdeb.com/dasharo/dug/5/Zarhus_Trustworthy_Embedded_Linux_Distro.pdf
https://youtu.be/17ZImUA0JSw
-->

---

#

Strategy

- Extend core firmware components (U-Boot, ARM Trusted Firmware, Linux Kernel)
towards a fully open, reproducible, and auditable Root and Chain of Trust.
- Integrate cutting-edge hardware security building blocks (secure storage,
secure elements, embedded dTPM solutions, OP-TEE-based firmware TPM, encrypted
root filesystems) for measurable integrity and resilience.
- Develop tooling for RoT and CoT with long term maintainability in mind.
- Collaboratively participate in communities aligned with freedom, sovereignty,
and simplicity, particularly those around Dasharo, OpenXT, Qubes OS,
Kicksecure, FreeBSD, OpenWRT, Debian, Fedora, and similar technology ecosystems
- Adopt an iterative, demo-driven approach to project execution, continuously
communicating progress via derivative products that illustrate real-world
applicability and verify ideas against practical scenarios.
- Project progress reporting using derivative products and demo-driven
approach.

<!--

Last from triad which set ground for Zarhus Team. What those big words from
mission and vision mean in practice?

-->

---

<center><img src="/img/0x1/zarhus_in_ecosystem.png" width="750px"></center>

---

<center><img src="/img/0x1/zarhus-dasharo-relation.png" width="650px"></center>

<!--

What is relation to Dasharo

-->

---

<center><img src="/img/0x1/zarhus_value_prop.svg" width="750px"></center>

<!--

What is value proposition?

-->

---

<center><img src="/img/0x1/zarhus_supported_hw.svg" width="750px"></center>

<!--

What hardware vendors we are working with?

-->

---
zoom: 0.9
---

# How community can use it?

- Prerequisites:
  * At least basic Yocto understanding is required
  * Understanding of kas (setup tool for bitbake based projects) is
      recommended
- Keep checking progress on:
  * <https://docs.zarhus.com/>
  * <https://github.com/zarhus>
    - we create roadmap under `zarhus-issues` and will track our progress
          there
    - we will inform you during DUGs
- Currently most repositories are still in 3mdeb organization (32) in private
  gitlab (37)
  * <https://github.com/3mdeb> - search for `meta` keyword
  * most of the code is MIT-licensed
- In total it is 87k lines of code of 17k we already contributed upstream.
- Meanwhile for direct business needs we designed, developed and delivered over
  400k lines of code.
  * With Zarhus we want to change this proportions.

---
zoom: 0.9
---

# How to buy it?

- Indirectly through Dasharo Entry Subscription or obtaining RTE (limited to
  product needs):
  * <https://shop.3mdeb.com/product-category/dasharo-entry-subscription/>
  * <https://shop.3mdeb.com/shop/open-source-hardware/rte/>
- Through productised services:
  <https://shop.3mdeb.com/product-category/services/>
  * Secure Boot integration for NXP and Rockchip
  * TPM and UEFI Secure Boot Assessment
  * TXE Secure Boot Assessment
  * Intel Boot Guard Assessment
  * U-Boot Hardening
  * Boot Time Optimization Report
  * Support Package and Workshop
  * and many more
- Through Training:
  * <https://paceenterprisetraining.com>
- Or just contact us: <https://3mdeb.com/contact/#form>

---

<center><img src="/img/0x1/zarhus_on_github.png" width="640px"></center>

### <center>https://github.com/zarhus</center>

<!--

# Slowly building our presence and activity on Github.

-->

---

<center><img src="/img/0x1/meta-dts-12m.png" width="850px"></center>

<center>

<https://github.com/Dasharo/meta-dts>

</center>

---

<center><img src="/img/0x1/meta-rte-12m.png" width="850px"></center>

<center>

<https://github.com/3mdeb/meta-rte>

</center>

---

<center><img src="/img/0x1/dts_status_on_dug8.png" width="650px"></center>

<center>

<https://cfp.3mdeb.com/developers-vpub-0xd-2024/talk/QKJYGJ/>

</center>

---

# Zarhus Team Events Roadmap

- Preliminary dates for future Zarhus Developers Meetups
  * ZDM 0x2: **5th August 2025**
  * ZDM 0x3: **4th November 2025**

---

# Upcoming

- ZarhusBMC.
- OpenWRT for x86.
- Secure Boot for other Rockchip based platforms.
- ML for embedded systems.
- Boot time optimization for Slimbootloader bootstrapped industrial hardware.
- Work on GPU and crypto.
- Improve contribution to embedded Linux related projects
  `17065 insertions(+), 661 deletions(-)`

---

# Community

- Github has only activity from Zarhus Team.
- On Matrix we have our small community.
  * <https://matrix.to/#/#zarhus:matrix.3mdeb.com>
  * Three rooms: General, Support and Random
  * Currently space has 22 members.

---
layout: cover
background: /intro.png
class: text-center
---

# Questions?

<!--

Comment to satisfy pre-commit

-->
---
layout: cover
background: /intro.png
class: text-center
---

# Backup

<!--

# Inevitable side-effect

* Multimedia, quality of life and UX features like fast logo display,
animations during boot-up or hardware video decoding, which are common in
consumer devices like Android phones require more work than usual.

- **Why?**
  Our main priority is security and long-term maintainability over cosmetic or
  typical user features.
  We use official, well-maintained software (upstream kernels, bootloaders, and
  security environments) instead of code provided by hardware vendors that might
  be less secure or harder to keep updated.

- **How does this cause the limitation?**
  By not using vendor-specific short-cuts or binary blobs (which might enable
  early graphics), we don’t get early access to graphics hardware. This means
  users may see a basic boot process instead of a polished animation until Linux
  is running.

- **Can this be improved?**
  Yes, but it would take major effort and cost—as it would require serious
  boot-time optimization and possibly some compromise on our core values for
  security and maintainability.

- **What’s next?**
  We prefer focusing on our original agreement (static images, secure,
  maintainable system). If you need these extra features, we can discuss
  them as new projects or support packages in the future.
-->
