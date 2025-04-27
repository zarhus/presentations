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
It is not only about marketing but also about honest openness, authenticity,
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

- Forum where Zarhus Team and Partners share knowledge and inform about
  Zarhus-related development.
- It would be quarterly event.
- Short presentations (<20min) focused on demo.
- Little time for questions (5min after each presentation).
- Recordings will be published on YouTube.

<!--

Format.

If no questions I will try to spin off some discussion and gather some ideas.

-->

---

## <center>&#x1F680; Zarhus Developers Meetup 0x1 Agenda &#x1F680;</center>

<br>

#### &#x1F44B; 18:00 CET Welcome Zarhus Developers Meetup, by Piotr
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
---

#

Mission and Vision for Zarhus, Trustworthy Embedded Linux Distro.

### Mission

- Simplify enabling advanced hardware security and performance in embedded systems.
- Deliver a trustworthy embedded Linux distribution based on Yocto.
- Ensure honest openness, authenticity, and accountability as core values.

### Vision

- Become the leading embedded Linux distribution for secure and trusted hardware platforms.
- Set a benchmark for trustworthiness in embedded systems through transparency and innovation.

::right::

<center><img src="/img/0x1/zarhus_slogan.png" width="550px"></center>


<!--

Application level-wise.

http://dl.3mdeb.com/dasharo/dug/5/Zarhus_Trustworthy_Embedded_Linux_Distro.pdf
https://youtu.be/17ZImUA0JSw

-->

---

#

Strategy

- Extend core firmware (U-Boot, ARM Trusted Firmware, Linux Kernel) to build a robust Root and Chain of Trust.
- Integrate advanced hardware security features: secure storage, secure elements, dTPM, OP-TEE-based fTPM, and encrypted rootfs.
- Develop tooling for RoT and CoT with long term maintainability in mind.
- Collaborate closely with the Dasharo ecosystem for advanced testing and certification. Maximize synergy across the stack (more about that later).
- Draw inspiration from projects like OpenXT and Qubes OS.
- Project progress reporting using derivative products and demo-driven approach.

---

<center><img src="/img/0x1/zarhus_in_ecosystem.png" width="800px"></center>

---

# Inevitable side-effect

* Multimedia, quality of life and UX features like fast logo display,
animations during boot-up or hardware video decoding, which are common in
consumer devices like Android phones require more work than usual.

- **Why?**  
  Our main priority is security and long-term maintainability over cosmetic or typical user features.  
  We use official, well-maintained software (upstream kernels, bootloaders, and security environments) instead of code provided by hardware vendors that might be less secure or harder to keep updated.

- **How does this cause the limitation?**  
  By not using vendor-specific short-cuts or binary blobs (which might enable early graphics), we don’t get early access to graphics hardware. This means users may see a basic boot process instead of a polished animation until Linux is running.

- **Can this be improved?**  
  Yes, but it would take major effort and cost—as it would require serious boot-time optimization and possibly some compromise on our core values for security and maintainability.

- **What’s next?**  
  We prefer focusing on our original agreement (static images, secure, maintainable system). If you need these extra features, we can discuss them as new projects or support packages in the future.

---

# Zarhus Team Events presence over last year

---

# Zarhus Team Events Roadmap

---

# Zarhus Issues repo stats

---

# Contribution

---

# Community

---

layout: cover
background: /intro.png
class: text-center

---

# Questions?

<!--

Comment to satisfy pre-commit

-->
