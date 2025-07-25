---
theme: ../slidev-template/theme
layout: cover
background: /intro.png
class: text-center
---

## Cache timing attacks: How do they work?

<center>
    <img src="/../img/zarhus_logo.png" width="150px"
         style="margin-left:-20px;filter: invert(1);">
</center>

---

## Who am I?

<div class="grid grid-cols-2 gap-8">

<div>

**Michał Iwanicki**

_Junior Embedded Systems Engineer_

- <michal.iwanicki@3mdeb.com>
- [3mdeb.com](https://3mdeb.com)

</div>

<div class="flex justify-center items-center">
  <img src="/../img/zarhus_logo.png" height="220px" />
</div>

</div>

---

## Agenda

- Overview of current meta-zarhus layer layout
- Generating Unified Kernel Image (UKI)
- Rootfs encryption
- A/B update
- Current Status & Demo
- Q&A

<!--
- Overview - short description on different layers (e.g. bsp, features) and what
do they contain
- UKI - how UKI was added to meta-zarhus
- Rootfs encryption -
- A/B update - what is it, how it works
-->

---

## meta-zarhus layer overview

Current layout of `meta-zarhus` repository (on `develop` branch) along with
sublayers

```text {all|3-6|7|8|9-17|10,17|18|19|20}
meta-zarhus
├── kas
├── meta-zarhus-bsp
│   ├── meta-zarhus-bsp-common
│   ├── meta-zarhus-bsp-rockchip
│   └── meta-zarhus-bsp-x86_64
├── meta-zarhus-distro
├── meta-zarhus-features
│   ├── meta-otab
│   │   ├── meta-otab-common
│   │   ├── meta-otab-encryption
│   │   ├── meta-otab-grub
│   │   ├── meta-otab-https
│   │   ├── meta-otab-rorootfs
│   │   ├── meta-otab-signed
│   │   ├── meta-otab-uboot
│   │   └── meta-otab-uki
│   ├── meta-zarhus-encryption
│   └── meta-zarhus-hardening
├── meta-zarhus-webkit
└── scripts
```

<!--
Shown here are only root level directories and all meta sublayers \
[click] Layers that add support for different platforms, e.g. Radxa (rockchip)
or for generic x86-64 architecture (tested on ODROID-H4) \
[click] Main distro configuration, recipes for zarhus image, etc. \
[click] Contains sublayers adding support for different features. Each feature
will be expanded upon in later slides \
[click] Layer adding support for Over The Air updates. \
[click] Layers used for x86-64 architectures. \
[click] Adds support for encrypting/decrypting rootfs in initramfs \
[click] Adds system hardening features \
[click] Adds support for e.g. Weston graphical environment
-->

---
transition: fade
---

## Boot flow

<center>
  After flashing image on disk
  <img src="/../img/partition-layout-1.svg"/>
</center>

---
transition: fade
---

## Boot flow

<center>
  After booting from default partition
  <img src="/../img/partition-layout-2.svg"/>
</center>

<!-- We are in initramfs right now -->

---
transition: fade
---

## Boot flow

<center>
  Create rwoverlay partition
  <img src="/../img/partition-layout-3.svg"/>
</center>

<!-- Use all allowed space on disk -->

---
transition: fade
---

## Boot flow

<center>
  Encrypt <code>rootfs_a</code>, <code>rootfs_b</code> and <code>rwoverlay</code>
  <img src="/../img/partition-layout-4.svg"/>
</center>

---

## Boot flow

<center>
  Mount overlayfs on <code>/</code> with lowerdir being <code>rootfs_a</code>
  and upperdir being <code>rwoverlay</code>
  <img src="/../img/partition-layout-5.svg"/>
</center>

<!-- This set of partitions is Zarhus A -->

---

## Unified Kernel Image (UKI)

What is UKI file and why do we use it:

> A Unified Kernel Image (UKI) is a combination of an UEFI boot stub program, a
> Linux kernel image, an optional initrd, and further resources in a single UEFI
> PE file. This file can either be directly invoked by the UEFI firmware \[...\]
> or through a boot loader \[...\].
>
> Source: <https://uapi-group.org/specifications/specs/unified_kernel_image/>

This quote mostly explains what is UKI and why we have decided to use UKI file
for x86-64 booting:

- One file can contain everything we need e.g. kernel, initramfs, kernel
  command line
- We can boot it directly from UEFI BIOS
- Smaller attack surface, no need for additional bootloader
- UEFI Secure Boot - we only need to sign and verify one file

---

## Generating UKI

- Manually (minimal example)

  ```sh
  ukify build --linux "<path/to/kernel>" --output uki.efi
  ```

  Building for other platforms might require more arguments e.g. `--os-release`
  and `--sbat`, otherwise `ukify` will take them from host system

<v-click>

- In Yocto you can use `uki.bbclass` that's available in `walnascar` and
  newer versions. In older ones you can backport this class to your own layer.
  That's what we've done in `meta-zarhus`. To use it:

  ```sh
  inherit uki
  INIT_MANAGER = "systemd"
  EFI_PROVIDER = "systemd-boot"
  IMAGE_BOOT_FILES = "${UKI_FILENAME};EFI/BOOT/bootx64.efi"
  UKI_CMDLINE = "root=LABEL=${ROOTFS_LABEL} console=ttyS0,115200 quiet"
  ```

    * `INIT_MANAGER` and `EFI_PROVIDER` is required by `uki.bbclass` while
    `UKI_CMDLINE` contains kernel command-line that'll be embedded inside UKI.
    * `IMAGE_BOOT_FILES` - list of files to put on boot partition.

</v-click>

<!--
[click] IMAGE_BOOT_FILES is used by bootimg-partition Wic plugin, you might have
to different variable if you are using different plugin.
-->

---

## Encrypting rootfs

Partition can only be encrypted when it's unused and unmounted, which in case of
rootfs requires us to do it before booting into OS. In `meta-zarhus` we are
doing it during first boot, in initramfs.

Encryption itself is done via `cryptsetup reencrypt --encrypt` command, which
allows us to encrypt partition in-place and keep our data.

There is one caveat that has to be taken under consideration, encrypted LUKS
partition needs LUKS header, which can be embedded inside partition itself or
created and used as a detached file. To embed header we need to shrink rootfs
filesystem by around 16-32 MB, so remember to keep some free space when creating
rootfs

---

## Closing encrypted rootfs

After implementing encrypted rootfs I noticed some warnings during shutdown and
reboot, that `systemd` wasn't able to close `rootfs` and `rwoverlay` partitions:

```text
systemd-shutdown[1]: Could not detach DM /dev/dm-2: Device or resource busy
systemd-shutdown[1]: Could not detach DM /dev/dm-0: Device or resource busy
systemd-shutdown[1]: Unable to finalize remaining DM devices, ignoring.
```

That happened because we can only close decrypted partition if it isn't busy,
e.g. by being mounted, and it can't be unmounted because it's in use.

<v-click>

To fix that, I had to go back to initramfs during shutdown and add shutdown
hooks that unmount and close everything. As we use `systemd`, going back to
initramfs is quite simple. If `/run/initramfs/shutdown` executable exists then
`systemd` will `pivot_root` to `/run/initramfs` and run `shutdown` executable.

So I had to do 2 things:

- Unpack initramfs to `/run/initramfs` during shutdown
- Add `shutdown` executable script

</v-click>

---

I added `shutdown` script directly to initramfs so we only have to unpack it in
correct place. It's lightly modified `init` script that's used by
`initramfs-framework` and allows us to easily add more shutdown hooks by just
putting them inside `/shutdown.d` folder inside initramfs, instead of `/init.d`
which are scripts run during booting. As of now we have a couple of different
shutdown hooks:

- `01-udev` - the same script is used in `/init.d` - Start `udevd`, needed by
  cryptsetup to close partitions
- `90-umount` - unmount `/oldroot` under which is old rootfs
- `93-luks_close` - close all open LUKS partitions
- `99-finish` - shutdown/halt/reboot/kexec

<v-click>

When implementing shutdown hook that closes LUKS partitions I encountered an
issue, `cryptsetup` dependency on `udevd`. Without it gets stuck, waiting
forever for event that'll never come, that's why first shutdown hook that runs
is `01-udev`. I also had problem with `udevd` itself in that it fails to start
when `WATCHDOG_USEC` environment variable is set to 0, which it is but only
during shutdown.

</v-click>

<v-click>

Unpacking initramfs is done by service that is stopped during shutdown. When
it's stopped it extracts initramfs from `.initrd` section of `UKI` file:

```sh
objcopy --dump-section .initrd=/tmp/initrd /boot/efi/boot/bootx64.efi
gunzip -c /tmp/initrd | cpio -id --no-absolute-filenames
```

</v-click>

<!--
[click] To debug that I had to read through udev code and add debug
prints to find out where and why does it fail.
-->

---

## A/B Update

An A/B update allows us to perform reliable updates that won't brick our device,
even if the update fails. It works by updating inactive partitions, B in the
case of using A, or A in the case of using B.

After the update, we can boot into
the newly updated partition. If the update fails and the system cannot boot,
then on the next boot, we will revert to the previous, working system.

---
transition: fade
---

## A/B Update flow

<center>
  Active slot: Zarhus A
  <img src="/../img/partition-layout-5.svg"/>
</center>

---
transition: fade
---

## A/B Update flow

<center>
  Update Zarhus B (inactive slot)
  <img src="/../img/partition-layout-6.svg"/>
</center>

<!--
Done with `otab update`
Change `BootNext` EFI variable to Zarhus B
-->

---
transition: fade
---

## A/B Update flow

<center>
  Boot updated slot (Zarhus B)
  <img src="/../img/partition-layout-7.svg"/>
</center>

<!--
If booting succeeds, change BootOrder so Zarhus B is boots by default
-->

---

## A/B Update flow

<center>
  In case booting fails, go back to Zarhus A
  <img src="/../img/partition-layout-5.svg"/>
</center>

<!--
If Zarhus B didn't boot correctly then BootOrder is unchanged and BootNext
was deleted by boot manager when we tried to boot Zarhus B
-->

---
layout: center
---

## Demo

---

## Demo - first boot (backup)

<video controls width="90%">
  <source src="/../img/first-boot.webm" type="video/webm">
</video>

<!--
Don't start in presenter mode, doesn't start in other window!

This is after flashing Zarhus image on disk

0:11 - Before first boot we have only those options, no Zarhus A or B to choose
After first boot in addition to those boot options there will also be Zarhus A
and Zarhus B <br/>
0:13 - Reboot <br/>
0:19 - Creating rwoverlay partition. It's will have around 500 GB <br/>
0:22 - Encrypting rootfs_b <br/>
0:40 - Encrypting rwoverlay - we don't encrypt in-place as it's faster and this
partition doesn't contain anything yet. <br/>
0:54 - Encrypting rootfs_a <br/>
1:22 - First boot requires us to change password

-->

---

## Demo - update (backup)

<video controls width="90%">
  <source src="/../img/update.webm" type="video/webm">
</video>

<!--
Don't start in presenter mode, doesn't start in other window!

We start just after first boot.

0:12 - show partitions, we are using Zarhus A. rootfs_a, rootfs_b and rwoverlay
are encrypted <br/>
0:16 - We can see that after first boot new Zarhus A and Zarhus B boot options
were added. BootOrder - Zarhus A is first (Boot0005), then Zarhus B (Boot0004).
<br/>
0:24 - I'm using debug image which allowed me to scp `.swu` update image to
ODROID which I'll use to update <br/>
0:32 - Use otab to update inactive partitions <br/>
1:02 - As you can see on second boot we don't create rwoverlay or encrypt
anything again. <br/>
1:12 - We can also login with password we set previously, thanks to rwoverlay.
Same with e.g. reverse searching used commands <br/>
1:19 - As we can see, we booted from Zarhus B slot (`boot_b` and `roofs_b`)
<br/>
1:40 - BootOrder changed, now Zarhus B boots first by default
-->

---

## References

- <https://blog.3mdeb.com/2025/2025-07-18-securing-embedded-linux>

---
layout: cover
---

<center>
  <h2>Q&A</h2>
  <img src="/../img/zarhus_logo.png" width="150px" style="margin-left:-5px">
</center>
