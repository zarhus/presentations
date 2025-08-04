---
theme: ../../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

# &#x1F44B; Zarhus Developers Meetup #2 &#x1F389;

## Dasharo Tools Suite Status

### Q3 2025

<center>
    <img src="/../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---
layout: two-cols-header
---

## Agenda

* What is DTS?
* DTS statistics Q3-Q4 2024.
  + Issues
  + Contributions.
  + Features.
  + Hardware support.
* DTS current architecture and tests.
* DTS new architecture and tests.
* Roadmap Q1-Q2 2025
* Q&A

---
layout: two-cols-header
---

# What is DTS?

<center>
  <img src="/../img/solid-and-secure-bridge.png" width="300" style="margin-left:-20px">
</center>

* A set of tools running in a Yocto-based image
* Provide better Dasharo user experience
  - Dasharo deployment
  - Dasharo update
  - DPP access
  - Switching from one Dasharo flavor to another (e.g. UEFI <---> heads)
  - HCL report
* https://docs.dasharo.com/dasharo-tools-suite/overview/  

<!--
Slide taken from:
https://github.com/Dasharo/presentations/blob/main/dug_8/dug_8_dasharo_tools_suite_status.md

- Time for this slide: 50s
- Idea/goal of this slide: Present DTS
- What to say: "What is DTS? DTS states for Dasharo Tools Souite and is a tiny
Linux Kernel built for 64-bit x86with goal to make Dasharo user experience
easier. Actually, it could be thought of as a solid and secure bridge between a
user and Dasharo. It has several Dasharo and Coreboot tools built in, as well
as other, firmware related tools for enhanced debugging and programming. But
most importantly, it has a layer of automation and GUI scripts that make DTS
more user-friendly."
-->

---
layout: two-cols-header
---

# What is DTS?

<center><img src="/../img/zdm_2/dts-gui-2.png" width="500"></center>

---
layout: two-cols-header
---

## DTS components

* Issues
  - [DasharoToolsSuite](https://github.com/Dasharo/dasharo-issues/issues?q=is%3Aissue%20state%3Aopen%20label%3ADasharoToolsSuite)
  label in [dasharo-issues](https://github.com/Dasharo/dasharo-issues) repo 
* Repositories
  - [dts-scripts](https://github.com/Dasharo/dts-scripts)
    + Main DTS logic 
  - [meta-dts](https://github.com/Dasharo/meta-dts/)
    + Yocto meta layer
    + Integration of dts-scripts and tools
  - Tests in [OSFV repo](https://github.com/Dasharo/open-source-firmware-validation/tree/develop/dts)
    + DTS tests placed under `dts` directory

---
layout: two-cols-header
---

## Timeframe

* The last DTS status presentation
  - DUG#8 (December 2024)
  - https://cfp.3mdeb.com/developers-vpub-0xd-2024/talk/QKJYGJ/
* We cover here
  - Q1-Q3 2025 - in terms of status report
  - Q3-Q4 2025 - in terms of plans  

<br><br>
<center><img src="/../img/zdm_2/dts_status_timeframe.png" width="600"></center>

---
layout: two-cols-header
---

## Statistics - issues

<center><img src="/../img/zdm_2/dts_issues.png" width="650"></center>

<!--

- steady growth of open issues
- decreasing number of closed issues my be concerning

Issues statistics retrieved by script from dasharo/presentations repo:
./diagrams/dts_issues.py 

-->

---
layout: two-cols-header
---

## Statistics - dts-scripts PRs

<center><img src="/../img/zdm_2/dasharo_prs_dts_scripts.png" width="650"></center>

<!--

PR statistics retrieved by script from dasharo/presentations repo:
./diagrams/dasharo_forks.py 

(Manually modified date and stopeed generation for other repos to save time,
script might be made more generic to fit both DUG and ZDM).

-->

---
layout: two-cols-header
---

## Statistics - meta-dts PRs

<center><img src="/../img/zdm_2/dasharo_prs_meta_dts.png" width="650"></center>

<!--

PR statistics retrieved by script from dasharo/presentations repo:
./diagrams/dasharo_forks.py 

(Manually modified date and stopeed generation for other repos to save time,
script might be made more generic to fit both DUG and ZDM).

-->

---
layout: two-cols-header
---

## Upstreaming

<br>
<center><img src="/../img/zdm_2/upstreaming_status.jpg" width="400"></center>

* Not much going on
* We can do better
* We certainly do not lack opportunities
  - We often add something to `meta-dts` (not upstream layer) and never go back to it

---
layout: two-cols-header
---

## Recent changes

- 2.1.1 (13/12/2024)
  - Fix for release for NS50 11th Gen NovaCustom series
- 2.1.2 (20/12/2024)
  - HCL report and DPP credentials fixes

<center><img src="/../img/NS51-front-1.png" width="500"></center>

---
layout: two-cols-header
---

## Recent changes

- 2.1.3 (03/01/2025)
  - Fix for logs not being sent after update
- 2.2.0 (30/01/2025)
  - Add support for NovaCustom V56TU heads flavor

<center><img src="/../img/v560tu-front.png" width="500"></center>

---
layout: two-cols-header
---

## Recent changes

- 2.2.1 (05/02/2025)
  - Fix ODROID-H4 firmware update/deployment
- 2.3.0 (20/03/2025)
  - Add support for NovaCustom V54TU heads flavor

<center><img src="/../img/odroid_h4.jpg" width="400"></center>

---
layout: two-cols-header
---

## Recent changes

- 2.4.0 (31/03/2025)
  - Use MinIO for DPP
    + Replaced nextcloud share with S3-compatible object storage
    + Single set of credentials per user for a lifetime (previously: per user **and** per product)
    + Delivered new set of credentials to existing users
    + https://www.min.io/

<br>
<br>
<center><img src="/../img/logo_minio.webp" width="350"></center>

---
layout: two-cols-header
---

## Recent changes
- 2.5.0 (11/06/2025)
  - Add SeaBIOS support (PC Engines APU2/3/4/6)

<center><img src="/../img/apu2.png" width="450"></center>

---
layout: two-cols-header
---

## Ongoing work 

* Current Problem
  - E2E Tests don't match real workflows
  - Some platform-dependent steps not executed in emulation tests right now
* Proposal
  - Modify DTS calls to allow for samples collection
  - Record commands calls and exit codes
  - Run the same commands in emulated environment and compare
  - https://github.com/Dasharo/open-source-firmware-validation/issues/653

---
layout: two-cols-header
---

## Ongoing work 


<div style="display: flex; justify-content: center; align-items: center; height: 100%;">
  <div style="transform: scale(0.7); transform-origin: top left;">

```mermaid
flowchart TD

    M[Collect sample from real hardware workflow]
    M --> N{Hardware workflow successful?}
    
    N -->|Yes| O[Sample is trustworthy]
    N -->|No| P[Discard sample, retry]
    P --> M
    
    O --> Q[Run the same workflow on QEMU E2E test]
    Q --> R[Generate QEMU sample file]
    R --> S[Compare real hardware sample vs QEMU sample]
    
    S --> T{Samples match?}
    T -->|Yes| U[E2E test success ✓]
    T -->|No| V[E2E test failure ✗]
    

    
    style U fill:#ccffcc
    style V fill:#ffcccc
```
  </div>
</div>

---
layout: two-cols-header
---

## Roadmap

<br>

<center><img src="/../img/zdm_2/dts_roadmap_v0.1.png" width="650"></center>

---
layout: cover
background: /intro.png
class: text-center
---

## Q&A

<center>
    <img src="/../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>
