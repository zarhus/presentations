#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 3mdeb <contact@3mdeb.com>
#
# SPDX-License-Identifier: Apache-2.0
import matplotlib.pyplot as plt

dts = {}

# Dasharo Tools Suite
dts["v1.2.8"] = 45  # wic+iso
dts["v1.2.13"] = 94
dts["v1.2.14"] = 105
dts["v1.2.15"] = 50
dts["v1.2.16"] = 75
dts["v1.2.17"] = 75
dts["v1.2.18"] = 263
dts["v1.2.19"] = 237
dts["v1.2.20"] = 119  # only wic
dts["v1.2.21"] = 403
dts["v1.2.22"] = 25
dts["v1.2.23"] = 260
dts["v2.0.0"] = 422
dts["v2.1.0"] = 68
dts["v2.1.1"] = 115
dts["v2.1.2"] = 53
dts["v2.1.3"] = 1674
dts["v2.2.0"] = 113
dts["v2.2.1"] = 200
dts["v2.3.0"] = 65
dts["v2.4.0"] = 225
dts["v2.5.0"] = 310
dts["v2.6.0"] = 194
dts["v2.6.1"] = 68
dts["v2.7.0"] = 69
dts["v2.7.1"] = 235

releases = list(dts.keys())
dts_values = list(dts.values())

plt.figure(figsize=(12, 7))

bars_dts = plt.bar(
    releases,
    dts_values,
    color="#38d430",
    label="Dasharo Tools Suite Releases",
)

plt.xticks(rotation=30, ha="right")

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
