---
layout: cover
background: /../intro.png
class: text-center

---
## &#x1F44B; Welcome Zarhus Developers Meetup &#9822; &#9816;

<center>
    <img src="/slides/img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---

<center><img src="/slides/img/zdm_3/banner.jpg" width="650px"></center>

<!--

We would like to give you a heads up about our accomplishments over last 3
months. How we followed our mission and where we are with our vision of Zarhus
OS.

Also how this vision and mission evolve through feedback from customers and
market observation.

-->

---

<center><img src="/slides/img/0x1/zarhus_logo.png" width="380px"></center>

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
  + [ZDM#1](https://www.youtube.com/playlist?list=PLuISieMwVBpLr1CMIGmm91ozBsYJaWEjr) and [ZDM#2](https://www.youtube.com/playlist?list=PLuISieMwVBpJcqCZVB99ndctQpbeOD_bf)
    are on YouTube.
  + You can get those also through [cfp.3mdeb.com](https://cfp.3mdeb.com/zarhus-developers-meetup-0x1-2025/talk/) and [ZDM#1 page](https://events.dasharo.com/event/4/zarhus-developers-meetup-1) and [ZDM#2](https://events.dasharo.com/event/6/zarhus-developers-meetup-2) since those are built-in our Pretalx instance.
  + Securing emebedded Linux by Michał was most viewed
  + CROSSCON was second
  + OpenBMC was third

<!--

If no questions I will try to spin off some discussion and gather some ideas.

-->

---

## <center>&#x1F680; Zarhus Developers Meetup #3 Agenda &#x1F680;</center>

<br>

#### &#x1F44B; 18:00 CET Welcome Zarhus Developers Meetup, by Piotr &#x1F448; You Are Here
<br>

#### &#x1F512; 18:25 CET Context Based Authentication: Identifying host by environment, by Mateusz
<br>

#### &#x1F4BB; 18:50 CET Dasharo Tools Suite: development nad testing insights, roadmap, by Daniil
<br>

#### &#x1F5A5; 19:15 CET Hardware-Backed Security in Android, by Maciej
<br>

#### &#x1F9F1;&#xFE0F; 19:40 CET Stop dreading NIS2: Unlock your firmware digital sovereignty with Zarhus, by Maciej
<br>

#### &#x1F44F; 20:00 CET Zarhus Developers Meetup Closing Remarks, by Piotr

---

- Dasharo and Zarhus Ecosystem
- Dasharo and Zarhus Release Process vision and execution
- Qubes Air motivation recap and Zarhus role in it
- Zarhus Hardware Certification Program and related products
- Zarhus Business Model v0.2

<!--

- Productized services based on 3mdeb and Zarhus Team established _modus operandi_

Since I have some time during the intro I would like to touch couple random
topics related to how we plan to realize Zarhus OS mission and vision in
upcoming months.

-->
---

<figure>
  <img src="/slides/img/zdm_3/dasharo_and_zarhus_ecosystem.excalidraw.svg" width="500px">
</figure>

---

<figure>
  <img src="/slides/img/zdm_3/zarhus_in_ecosystem_v2.excalidraw.svg" width="800px">
</figure>

---

<figure>
  <img src="/slides/img/zdm_3/zarhus_in_ecosystem_v2_extended.excalidraw.svg" width="800px">
</figure>

---
transition: fade
---

<figure>
  <img src="/slides/img/zdm_3/dasharo_and_zarhus_release_process.excalidraw.png" width="900px">
</figure>

---
transition: fade
---

<figure>
  <img src="/slides/img/zdm_3/dasharo_and_zarhus_release_process_status.excalidraw.svg" width="900px">
</figure>

---

<figure>
  <img src="/slides/img/zdm_3/qubes_air_motivation_today.excalidraw.png" width="900px">
</figure>

<!--

We discussing Zarhus and Dasharo Release Process, but let's not forget about
its place in higher level vision. The goal of those processes is to improve
trustworthiness of every computing device. Obviously according to our
abilities.

We have to think about development of Zarhus Provisioning Box in a way that it
would allow Mandatory Access Control and Policy-based decision making,
especially when that policy would be based on SRTM and DRTM measurements in TPM
PCRs.

-->

---

<center><img src="/slides/img/zdm_3/zarhus_cooperation_model_v0.2.png" width="950px"></center>

<br>

- v0.2 of cooperation model
- Zarhus Hardware Certification (ZHC) - not on slide, but it is essential
delivery of every segment process, we already complying to it by executing our
_modus operandi_, but we used that term only in Dasharo so far
- Zarhus Ecosystem Alignment (ZEA) - one of the goals is to drive development
of Zarhus Ecosystem into Zarhus Hardware Certification

<!--

- Why we need that semantics?
  - The goal is to improve communication with customers, but also slightly bigger
    strategy of contributing to reference architectures, narrow promise and
    business value and deliver.
  - Correct and more systematic approach would also help us fulfil compliance 
    requirements.
  - It is not always clear that some Zarhus Hardware Certification need early
    analysis of Root of Trust (aka TrustRoot assessment) or figuring out assembling
    as well as writing down procedures how to accomplish it (aka Lab Assembly
    Guide). To improve communication we introduce those two terms for existing 
    processes, tooling and Background IP.

-->

---

<figure>
  <img src="/slides/img/zdm_3/30Q-zarhus-ecosystem-alignment.svg" width="500px">
</figure>

<!--

* Quarterly coordination program for Zarhus OS ecosystem component alignment.
Selects Yocto/U-Boot/kernel/userspace products and features from existing
portfolio to maximize value within budget constraints, tracked via Stack
Alignment Manifest (SAM) - a mutually agreed-upon (signed-off-by) record of OS
component versions used for business and project management decisions.
* SAM tracks versions of Yocto layers, U-Boot, Linux kernel, systemd,
security hardening features (UEFI Secure Boot, TPM, encrypted rootfs), OTA
update mechanisms, and embedded application frameworks, enabling monitoring of
new releases and changelog review to determine implementation priorities. This
is a business decision tool, not a technical build manifest.
* Coordination happens through monthly 90min customer calls reviewing priorities,
issues, and plans, with final quarterly product selection via spreadsheet-based
workflow. Execution is git/PR-driven across public GitHub (Zarhus forks of
upstream Yocto/kernel/U-Boot), issue trackers (zarhus-issues), milestones, and
documentation repositories (docs.zarhus.com).
* Optional multi-year strategic planning (<20% of scope) identifies trends and
upstream opportunities based on 3mdeb team preparation materials.

-->
---

# Community

- Github still has only activity from Zarhus Team.
  + 14 (=) followers.
  + ZarhusBMC has 11 (+3) stars
- On Matrix we have our small community.
  + <https://matrix.to/#/#zarhus:matrix.3mdeb.com>
  + Three rooms: General, Support and Random
  + Currently space has 30 (+2) members.

---
layout: cover
background: /intro.png
class: text-center
---

# Questions?

---
layout: cover
background: /intro.png
class: text-center
---

# Backup

---

# Zarhus Ecosystem Alignment deep dive

* **Monthly Coordination Calls**: 90min customer-facing calls reviewing current
  quarter progress, priorities, issues, and plans for next quarter.
* **Stack Alignment Manifest (SAM)**: Mutually agreed-upon (signed-off-by)
  record tracking Zarhus OS component versions (Yocto layers, U-Boot, kernel,
  systemd, security features, OTA) to monitor new releases, review changelogs,
  and make business/PM decisions about implementation priorities. Not a
  technical build manifest.
* **Spreadsheet-based Product Selection**: Quarterly selection from existing
  Zarhus product portfolio (features, subprojects) within budget constraints to
  maximize value.
* **Git/PR-Driven Execution**: Coordination via GitHub/Gitea repos (Zarhus
  forks), zarhus-issues tracker, milestones, PRs, and documentation sites
  (docs.zarhus.com).
* **Existing Product Integration Focus**: Maximizes leverage of existing Zarhus
  products and components (80% of effort), with 20% buffer for bug fixes and
  ad-hoc support.

