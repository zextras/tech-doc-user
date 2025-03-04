#!/bin/bash

# SPDX-FileCopyrightText: 2022 Zextras <https://www.zextras.com/>
#
# SPDX-License-Identifier: CC-BY-NC-SA-4.0

#
# Simple script to build all products at once

# to wipe out the old build and write a fresh one, use
# make -C source/$i clean gettext html

locales=('en' 'fr' 'it')

for locale in "${locales[@]}"; do
  echo "Building $locale for"
  LOCALE=$locale SPHINXOPTS="-D language=$locale" \
    make -C source/carbonio  html
done

echo""
echo "Script finished"
