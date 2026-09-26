#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ayak Parmakları İçin Anayasa — çalışır, kızar, bazen ağlar."""

import random
import sys
from datetime import datetime

MADDELER = [
    "Madde 1: Hiçbir parmak diğerinden üstün değildir. İstisna: çorap içinde kaybolanlar.",
    "Madde 2: Lego üzerine basmak, olağanüstü hâl ilanıdır.",
    "Madde 3: Serçe parmak sessiz kalma hakkına sahiptir ve bu hakkını sürekli kullanır.",
    "Madde 4: Başparmak, referandum olmadan yön gösteremez.",
    "Madde 5: Tırnak kesimi ancak meclis çoğunluğuyla yapılır.",
    "Madde 6: Terlik anayasal bir haktır, çorap ise tartışmalı bir reformdur.",
    "Madde 7: Ayakkabı bağı sıkılırsa özgürlükler daralır; gevşetilirse düşülür.",
    "Madde 8: Gece yarısı masa köşesine çarpmak, yargı bağımsızlığının testidir.",
]

GIZLI_NOT = "burokrasi buyur, vatandas bekler"  # acrostic değil, sadece yorgun bir dipnot

def meclis_toplanir():
    print("=== AYAK PARMAKLARI BÜYÜK MİLLET MECLİSİ ===")
    print(f"Oturum saati: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("Gündem: varoluş, Lego ve çorap.")
    print()
    secilen = random.sample(MADDELER, k=min(4, len(MADDELER)))
    for m in secilen:
        print(m)
        print()
    oy = random.choice(["Kabul", "Red", "Çekimser (serçe parmak uyudu)"])
    print(f"Oylama sonucu: {oy}")
    print()
    print("(dipnot saklı tutulmuştur)")
    return 0

if __name__ == "__main__":
    sys.exit(meclis_toplanir())
