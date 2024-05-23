#!/bin/bash

# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com/>
#
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

#
# Simple script to generate en locale

BUILDDIR=locales \
  make -C source/carbonio gettext
sphinx-intl update \
  --locale-dir source/carbonio/locales \
  --pot-dir source/carbonio/locales/gettext

echo""
echo "Script finished"
