---
layout: cover
background: /../intro.png
class: text-center

---
## &#x1F44B; Welcome Zarhus Developers Meetup &#9822; &#9816;

<center>
    <img src="/../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---

<center><img src="/../img/zdm_2/banner.jpg" width="650px"></center>

<!--

We would like to give you a heads up about our accomplishments over last 3
months. How we followed our mission and where we are with our vision of Zarhus
OS.

I'm very happy we starting new secular tradition and celebrate our
achievements, train presentation skills and communicate with our community.

-->

---

<center><img src="/../img/0x1/zarhus_logo.png" width="380px"></center>

_**Zarhus** is an embedded **Linux** distribution based on **Yocto**, developed
by 3mdeb. Zarhus simplified provisioning, integration and maintenance of
embedded platforms focused on strong security founded on immutable **Root of
Trust** and  leveraging the **Chain of Trust** up to the target application._

<!--

* If you watch this first time.
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
  - [ZDM#1](https://www.youtube.com/playlist?list=PLuISieMwVBpLr1CMIGmm91ozBsYJaWEjr) are on YouTube.
  - You can get those also through [cfp.3mdeb.com](https://cfp.3mdeb.com/zarhus-developers-meetup-0x1-2025/talk/) and [ZDM#1 page](https://events.dasharo.com/event/4/zarhus-developers-meetup-1) since those are built-in our Pretalx instance.
  - OpenBMC from Mateusz was most viewed
  - Kicksecure's ram-wipe was second
  - Cache timing attacks was third

<!--

If no questions I will try to spin off some discussion and gather some ideas.

-->

---

## <center>&#x1F680; Zarhus Developers Meetup #2 Agenda &#x1F680;</center>

<br>

#### &#x1F44B; 18:00 CEST Welcome Zarhus Developers Meetup, by Piotr &#x1F448; You Are Here
<br>

#### &#x1F512; 18:25 CEST ZarhusBMC: OpenBMC for x11ssh SE, by Mateusz
<br>

#### &#x1F4BB; 18:50 CEST Securing embedded Linux: Secure Boot, encryption and A/B updates with Yocto, by Michał
<br>

#### &#x1F5A5; 19:15 CEST CROSSCON Hypervisor: virtualization on platforms without virtualization support, by Daniil
<br>

#### &#x1F9F1;&#xFE0F; 19:35 CEST Dasharo Tools Suite Status, by Maciej
<br>

#### &#x1F44F; 18:55 CEST Zarhus Developers Meetup Closing Remarks, by Piotr

---

* Zarhus Family/derivatives
* Dasharo Tools Suite in press and popularity
* Zarhus Business Model


<!--

Since I have some time during the intro I would like to touch couple random
topics related to how we plan to realize Zarhus OS mission and vision in
upcoming months.

-->

---
clicks: 5
---

<center><img src="/../img/zdm_2/zarhus_family.excalidraw.png" width="550px"></center>

<!--

[click]

Dasharo Tools Suite (DTS) is a set of tools running in a minimal Linux
environment to deploy, update, and maintain firmware on Dasharo-supported
devices. For example, it can be used to update the firmware on a device or run
the initial deployment, even when no OS is currently installed.

[click]

Remote Testing Environment is a hat designed for Orange Pi Zero board which
runs specially crafted Linux distribution using the Yocto Project it is called
RTE OS and is part of Zarhus OS family.

We developed RTE to enable programmers from around the world in low level
firmware development without hassle of heavy KVM switch interface. As a result
we have a tool which makes firmware debugging tasks easy.

[click]

ProvisioningBox (PBOX) OS  - this is specially crafted reasonably secure and
trustworthy embedded operating system with goal to be run in VM or on hardware
(Odroid-H4+ supported) which simplify Root of Trust and Chain of Trust
provisioning as well as provide CI-in-the-box for selfhosted, airgapped system
that can build firmware for enterprise internal depoloyments. It aims to, if
not solve, to at least mitiage issues of key mismanagment and support firmware
developers in building and signing firmware artifacts as well as mke those
ready for modern RoT and CoT technologies.

[click]

ZarhusBMC - incarnation of Zarhus OS dedicated to BMCs, it consist of set of
tools accelerating OpenBMC porting to proprietary hardware, through set of
tooling it aims to produce skeleton for OpenBMC autoport. With sepcial focus on
Root of Trust and Chain of Trust of BMC, as all Zarhus OS derviatives.

[click]

ZarhusWRT - the same concept but aim for OpenWRT ecosytem of wireless routers.
With aim of target wireless routers and support provionsing and maitaining RoT
and CoT for those chipsetes.

-->

---

<center><img src="/../img/zdm_2/dts_release_downloads.png" width="950px"></center>

<!--

Full status will be on Maciej presentation, but I would like to drop some
numbers and news, which are not there AFAIK

Obviously it does no contain other statics like direct downloads from
boot.3mdeb.com

-->

---

<center><img src="/../img/zdm_2/dts_press01.png" width="850px"></center>

[https://www.linuxtechmore.com/dasharo-firmware-1-0-0-novacustom-linux-laptops](https://www.linuxtechmore.com/dasharo-firmware-1-0-0-novacustom-linux-laptops)

---

<center><img src="/../img/zdm_2/dts_press02.png" width="950px"></center>

[https://www.osnews.com/story/142758/review-the-novacustom-v54-is-an-outstanding-linux-laptop-with-dasharo-coreboot-firmware/](https://www.osnews.com/story/142758/review-the-novacustom-v54-is-an-outstanding-linux-laptop-with-dasharo-coreboot-firmware/)

---

<center><img src="/../img/zdm_2/fum.png" width="650px"></center>

<!--

DTS is part of FUM

-->

---

<center><img src="/../img/zdm_2/rte_release_downloads.png" width="900px"></center>

---

# What all that means?

* "Release early. Release often. And listen to your customers.", Eric S. Raymonds <i>Cathedral and the Bazaar</i>
* Our goal is to publish as many release as possible, assuming similar quality
we have now, to gather interest of relevant communities.
* Testing have to be automated by design.
* We have to rely more on metadata configurable by user than on hard-coded
values.
* Releases have to be made in tiers:
  - LTS - once a year
  - Scoped - release made on top of LTS, with testing limited to added
    functionality,
  - Nightly - only smoke tests executed,
* Average number of releases
  - DTS: 3.34 release/quarter
  - RTE: 0.29 release/quarter (once in 11 months)

---

# ProvisioningBox Vision

* It can run as VM or on bare metal - for VM security is on hosting provider
* Air-Gapped CI which can build open-source firmware like Dasharo, but also
ZarhusBMC, ZarhusWRT and other Zarhus derivative.
* It manage keys for firmware security features provisioning
* It can provision Root of Trust like Intel Boot Guard, Rockchip Secure Boot,
NXP High Assurance Boot etc.
* It can provision Chain of Trust technologies like UEFI Secure Boot including
signing drivers, OS loaders and applications.
* It can deliver security packages building e.g. TrenchBoot components.
* It support Nitrokey HSM.
* On bare-metal it can self-provision itself.

<!--

EU CRA/NIS2/ISO27001 compliance support.

-->

---

# ZarhusBMC Vision

* Assessment tooling included
* Autoport, scaffolding, skeleton building scripts included
  - Acceleration of Yocto/OpenBMC porting/enabling
* Modern BMCs (AST2500, AST2600, AST2700) for AMD and Intel servers
* Open Source Firmware Validation support
* Synergy with Dasharo host CPU firmware
* Business model similar to Dasharo

<!--

ZarhusWRT very similar vision, but it is too early for it.

-->

---

# Pace Enterprise Training (PET)

* Both PET and OST2 courses have its own needs for OS.
* Those OSes can be general purpose as well as very dedicated.
* Courses are executed in three environments:
  - OST2 VM for training environment isolation - Ubuntu 24.04 with customizations.
  - Emulated or simulated environment QEMU/Simics - currently Alpine Linux with
    semi-automated script installing packages.
  - Target hardware OS - Ubuntu 24.04 deployed using autoinstall and further
    customized through sync scripts.
  - DTS - as live distro.
* PET/OST2 ecosystem could benefit from consistent OS management, especially when connected with minimalism (resource saving) and customizability through metadata.

---

<center><img src="/../img/zdm_2/zarhus_business_model.png" width="950px"></center>

<br>

* All DTS, RTE OS release are ZCR
* ProvisioningBox OS will be ZEPR (<i>Zarhus Enterprise Package Release</i>)
with optional revenue sharing through reselling.
  - Most likely one release in a year for ZEPR customers.
* Initial ZarhusBMC most likely would be ZCR with some ideas to transition to
ZPPR/ZEPR.
* Zarhus OS (e.g. ZarhusWRT) for dedicated customers falls in ZSP.

---

# Zarhus Team Events Roadmap

* Preliminary dates for future Zarhus Developers Meetups
  - ZDM#3: **4th November 2025**
  - ZDM#4: **10th February 2026**

---

# Community

* Github still has only activity from Zarhus Team.
  - 14 followers.
  - ZarhusBMC has 8 stars, thanks to Mateusz Discussion idea and hype it created.
* On Matrix we have our small community.
  * https://matrix.to/#/#zarhus:matrix.3mdeb.com
  * Three rooms: General, Support and Random
  * Currently space has 28 (+6) members.

---
layout: cover
background: /intro.png
class: text-center
---

# Questions?

<!--

Comment to satisfy pre-commit

-->
