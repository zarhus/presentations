#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt

rte = {}

# RTE OS
rte["v0.7.1"] = 19
rte["v0.7.3"] = 35
rte["v0.7.4"] = 11
rte["v0.7.5"] = 33
rte["v0.8.0-rc1"] = 10

releases = list(rte.keys())
rte_values = list(rte.values())

plt.figure(figsize=(12, 7))

bars_rte = plt.bar(
    releases,
    rte_values,
    color="#38d430",
    label="RTE OS Releases",
)

plt.xticks(rotation=30, ha="right")

plt.title(
    "Number of rte Public Releases Downloads per version",
    fontsize=18,
    fontweight="bold",
    color="#272727",
)
plt.xlabel("Version", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of Downloads", fontsize=16, fontweight="bold", color="#272727")

# Add sum on top of stacked bars
for i in range(len(releases)):
    if rte_values[i] != 0:
        total = rte_values[i]
        plt.annotate(
            f"{total}",
            xy=(
                bars_rte[i].get_x() + bars_rte[i].get_width() / 2,
                bars_rte[i].get_y() + bars_rte[i].get_height(),
            ),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            color="black",
            fontsize=14,
            fontweight="bold",
        )

plt.legend(fontsize=12)

plt.gca().set_facecolor("#f5f5f5")

plt.savefig("img/zdm_2/rte_release_downloads.png", dpi=300)

plt.close()
