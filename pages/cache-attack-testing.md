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

---
layout: two-cols-header
---

## Cache addressing

Address is split in 3 parts

- Tag - address identifier
- Index - cache set index
- Offset - data offset in cache line

<!--
There are 4 possible addressing schemes: different combinations of
physical/virtual index and physical/virtual tag.
Offset size depends on cache line size, index depends on number of sets in
cache, tag is the rest of address.
-->

::left::

<v-click>

How cache addressing could look in Python

```python {1-4|6-7|8-9|all}
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

<v-after>

Possible 4-way set-associative cache implementation

<center><img src="/img/cache-addressing.png" width="70%"/></center>

</v-after>

---

## Cache timing attacks

<v-clicks>

- type of side channel attacks
- work by manipulating cache (directly or indirectly) and timing e.g. memory
  access time, program execution time, etc.
- varying granularity
  - more precise - cache line
  - less precise - cache set.

</v-clicks>

<!--
Directly - e.g. CPU instructions
Indirectly - exploiting how cache works

Granularity - described attacks work with cache line or cache set granularity
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

  - `Prime` - Fill cache lines with your own data
  <!-- i.e. make sure cache contains only your data -->
  - `Probe` - TODO

  TODO

  </v-clicks>

---

## Summary

Read more on [Cache attack mitigation testing](TODO-blog-post)

---

## Q&A

<center>
  <img src="/img/zarhus_logo.png" width="150px" style="margin-left:-20px">
</center>
