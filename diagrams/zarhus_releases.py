#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt

dts = {}

# Dasharo Tools Suite
dts["v1.2.8"] = 23 # wic+iso
dts["v1.2.13"] = 50
dts["v1.2.14"] = 49
dts["v1.2.15"] = 23
dts["v1.2.16"] = 37
dts["v1.2.17"] = 37
dts["v1.2.18"] = 158
dts["v1.2.19"] = 132
dts["v1.2.20"] = 46 # only wic
dts["v1.2.21"] = 200
dts["v1.2.22"] = 8
dts["v1.2.23"] = 131
dts["v2.0.0"] = 221
dts["v2.1.0"] = 31
dts["v2.1.1"] = 51
dts["v2.1.2"] = 21
dts["v2.1.3"] = 606
dts["v2.2.0"] = 51
dts["v2.2.1"] = 87
dts["v2.3.0"] = 24
dts["v2.4.0"] = 106
dts["v2.5.0"] = 100

releases = list(dts.keys())
dts_values = list(dts.values())

plt.figure(figsize=(12, 7))

bars_dts = plt.bar(
    releases,
    dts_values,
    color="#38d430",
    label="Dasharo Tools Suite Releases",
)

plt.xticks(rotation=30,ha="right")

plt.title(
    "Number of DTS Public Releases Downloads per version",
    fontsize=18,
    fontweight="bold",
    color="#272727",
)
plt.xlabel("Version", fontsize=16, fontweight="bold", color="#272727")
plt.ylabel("Number of Downloads", fontsize=16, fontweight="bold", color="#272727")

# Add sum on top of stacked bars
for i in range(len(releases)):
    if dts_values[i] != 0:
        total = dts_values[i]
        plt.annotate(
            f"{total}",
            xy=(
                bars_dts[i].get_x() + bars_dts[i].get_width() / 2,
                bars_dts[i].get_y() + bars_dts[i].get_height(),
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

plt.savefig("img/zdm_2/dts_release_downloads.png", dpi=300)

plt.close()
