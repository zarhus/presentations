---
layout: cover
background: /intro.png
class: text-center
---

## Cache timing attacks: How do they work?

<center>
    <img src="/img/zarhus_logo.png" width="150px"
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
  <img src="/img/zarhus_logo.png" height="220px" />
</div>

</div>

---

## Agenda

- Cache - what is it, and why do we use it?
- How cache timing attacks work
- Simple attack implementations - can we do it?
- Cache timing attacks in CROSSCON hypervisor
- Current Status & Demo
- Roadmap & Next Steps
- Q&A

---

## Cache - what is it

<v-clicks>

- small, fast memory
- used to store frequently accessed data or instructions
- Access time is much faster than RAM
- Much smaller than RAM
- And also much pricier

</v-clicks>

<!--
- Cache is usually quite small at least compared to RAM. Usually cache size is
maybe up to tens of MB but smaller and faster caches that are closer to the CPU
can be only Kb in size.
- For the best performance it should store frequently accessed data or
instructions in case of instruction cache or data that will be used next so we
don't have to wait for it to load from RAM
- Access time is much quicker that accessing RAM. It is also a lot closer to the
CPU.
- It is much smaller and pricier (per MB).
-->

---

## Cache - important concepts

<v-clicks>

- cache level - there can be multiple caches e.g. L1/L2/L3
  - each next level is slower and bigger
- LLC - Last Level Cache - highest level cache
- cache hit - data was in cache, fast access
- cache miss - data wasn't in cache, slower access
- cache line/block - cache entry of fixed size (usually 32/64 bytes)
- cache set - in _n-way_ caches set contains _n_ cache lines

</v-clicks>

<v-click at="1">
<center>
  <img src="/img/cache.png" width="50%"/>
</center>
</v-click>

<!--
- Usually lower leveled caches are per core while LLC is shared
- For the best performance we want lowest ratio of cache misses
- cache line - when data from memory is loaded into cache it's loading whole
cache line
-->

---
layout: two-cols-header
---

## Cache addressing

::left::

Address is split in 3 parts

- Tag - address identifier
- Index - cache set index
- Offset - offset in cache line

<!--
There are 4 possible addressing schemes: different combinations of
physical/virtual address for index and physical/virtual address for tag.
Offset size depends on cache line size, index depends on number of sets in
cache, tag is the rest of address.
-->

<v-click>

How cache addressing could look in Python

```python {1-4|6-7|8-9}
cache = [
  ((tag1, data), (tag2, data), (tag3, data), (tag4, data)),
  ((tag5, data), (tag6, data), (tag7, data), (tag8, data)),
]

if tag in cache[index]:
  print("cache hit")
else
  print("cache miss")
```

<!--
Cache can be thought of as array containing m sets with each set containing n
tuple/data pairs

If tag can be found in set then we have cache hit, in other words data we are
looking for is in cache (it's more complicated as cache line can be dirty i.e.
can't be used).
if tag can't be found in cache set then we have to get it from RAM (and load it
into cache). Which tag/data pair will be replaced depends on replacement policy,
it can be random, LRU or any other
-->

</v-click>

::right::

<center>
  <img src="/img/cache-address-split.png"/>
</center>

---

Possible 4-way set-associative cache implementation

<center>
  <img src="/img/cache-addressing.png" width="60%"/>
</center>

<!--
A little lower level and more complete look at cache implementation. Here cache
way contains additional bit to denote whether cache line is valid/dirty
(i.e. can be used)
-->

---

## Cache timing attack

<v-clicks>

- a type of side channel attacks
- work by manipulating cache (directly or indirectly) and timing e.g. memory
  access time, program execution time, etc.
- varying granularity
  - more precise - cache line
  - less precise - cache set.

</v-clicks>

<!--
Directly - e.g. CPU instructions, CLFLUSH on x86 to invalidate cache line,
DC CIVAC for ARMv8
Indirectly - exploiting how cache works e.g. accessing a lot of memory to load
it all into cache (and evict anything else that was there)

Granularity - described attacks work with cache line or cache set granularity.
-->

---

## Attack types

<!--
Below are 3 attack I focused on. There are many more.
-->

- `Flush+Reload` - the easiest attack described here. It consists of 2 parts:
  <v-clicks>

  - `Flush` - flush/evict shared memory from the cache
  - `Reload` - measure reload time of evicted memory

  </v-clicks>

  <v-click>

  If no one accessed evicted memory then reload time should indicate cache miss,
  i.e. we had to access it from RAM. Cache hit means that someone accessed this
  memory between `Flush` and `Reload`. This attack works with shared memory and
  allows us to get information with cache line granularity.

  </v-click>

<v-click>

- `Evict+Time` - very similar to the previous one. This time instead of timing
  reload time of evicted memory, we time execution time of program/process.

  The difference in execution time when shared memory line is in the cache and
  when it is evicted can indicate whether it was used or not.

</v-click>

---

- `Prime+Probe` - This attack doesn't require shared memory. It involves 2
  steps:
  <v-clicks>

  - `Prime` - fill cache lines with your own data
  <!--        ^or cache sets.  ^i.e. make sure cache contains only your data -->
  - `Probe` - reload your data and time it. If it's cache hit then someone
    accessed memory that maps to this cache set.

  </v-clicks>

  <v-click>

  The biggest challenge with `Prime+Probe` type of attack is mapping addresses
  to cache sets. Attacker needs to also know which addresses are used by victim
  process. This attack allows us to detect which set was used (and there can be
  many addresses that map to the same set)

  </v-click>

---

## Tests

- PoC tested on X86 and ARMv8 (RPI4)
- 2 programs
  - victim - uses shared library
  - attacker - tries to find out which cache lines were used by victim
- `Flush+Reload` & `Evict+Time` worked on X86
- `Flush+Reload` on RPI4 failed due to less precise timing (too many false
  positives).
  <!-- On X86 I could use counter register directly on RPI4 I had to use
  perf interface. Test could probably be fine tuned -->
- `Evict+Time` - Evicting cache lines used by victim resulted in function
  running around 150 units (likely CPU cycles) longer.
  <!-- function runtime varies by around 40 units so it was very visible jump -->

---

## CROSSCON hypervisor

Main goal of those tests will be verifying whether the cache coloring
implementation in the CROSSCON hypervisor prevents inter-VM cache attacks.

<center>
  <img src="/img/cache-coloring.png" width="70%"/>
</center>

<!--In short it's cache partitioning scheme where each VM can only use it's own
part of cache -->

---

## Shared memory

Attacks requiring shared memory will use CROSSCON hypervisor shared memory

<center>
  <img src="/img/shared-mem.png" width="70%"/>
</center>

And `ipcshmem` driver

```c
crosscon-ipc@8000000 {
  compatible = "crossconhyp,ipcshmem";
  (...)
};
```

<!--This driver creates /dev/crossconhypipc<ID> file which can be read/written
to or mmaped-->

---

## Evict+Time Implementation

- open and mmap `/dev/crossconhypipc0` created by `ipcshmem` driver
- first VM (victim) will calculate median time it takes to finish function that
  uses shared memory and then run it in an infinite loop and report difference
  from baseline it established earlier.
  - for simplicity’s sake victim program will time itself
- second VM (attacker) will continuously evict requested cache lines.

Without cache coloring there should be noticeable jump in first VM reported time
difference when evicting used cache lines (and no difference when evicting other
non-used shared memory)

---
layout: two-cols-header
---

# Evict+Time test on 1 VM

<!--
Maybe this should be demo if we won't manage to run 2 VMs before
presentation. Or if we don't need to show CROSSCON demo then version with shared
library on X86.
-->

As of now test was only verified on 1 VM as we don't have 2 VM config on RPI4.
Median time is calculated from last _n_ samples (in this case 500) and varies by
around 40 units.

::left::

<div style="padding:0 40px 0 0;margin: -100px 0 0 0">

Function execution time difference when evicting used (0th) cache line

```text {all|7}
$ cache_test time 0 & sleep 2 && cache_test evict 0
Opening /dev/crossconhypipc0
mmaping /dev/crossconhypipc0
Libflush init
Calculating median baseline. Don't evict.
Calculated median time: 498
Median time diff from baseline:  170
```

</div>

::right::

<div style="padding:0 40px 0 0;margin: -100px 0 0 0">

Function execution time difference when evicting unused (1st) cache line

```text {all|7}{at:'1'}
$ cache_test time 0 & sleep 2 && cache_test evict 1
Opening /dev/crossconhypipc0
mmaping /dev/crossconhypipc0
Libflush init
Calculating median baseline. Don't evict.
Calculated median time: 482
Median time diff from baseline:  34
```

</div>

<!--We can clearly see jump of around 140 units when we are evicting memory that
victim is using -->

---

## Next steps

- Run this test on 2 VMs and draw conclusions
- Add another test that checks cache coloring for non-shared memory

---

## References

- <https://blog.3mdeb.com/2025/2025-04-18-cache-attack-mitigation-testing>
- <https://crosscon.eu/library/deliverables> - D2.3 CROSSCON Open Specification
- <https://hwloc.readthedocs.io/en/stable/index.html> - `lstopo`, cache image
  generation
- <https://eprint.iacr.org/2013/448.pdf> - Flush+Reload: a High Resolution, Low
  Noise, L3 Cache Side-Channel Attack
- <https://github.com/isec-tugraz/armageddon> - `libflush` library used in tests
  for eviction, timing and memory barriers
- Patterson, David A., and John L. Hennessy. Computer Organization and Design.
  5th ed., Morgan Kaufmann, 2015

---
layout: cover
---

## Q&A

<center>
  <img src="/img/zarhus_logo.png" width="150px" style="margin-left:-20px">
</center>
