#!/usr/bin/env python3
"""Render harmonics 1, 3, 5, 7, 9, and 10 as an SVG without dependencies."""

import math
from pathlib import Path


HARMONICS = (1, 3, 5, 7, 9, 10)
COLORS = ("#60a5fa", "#34d399", "#fbbf24", "#f87171", "#a78bfa", "#14b8a6")
WIDTH, HEIGHT = 900, 390
LEFT, RIGHT, CENTER_Y = 80, 860, 190
SCALE = 42
SAMPLES = 720


def point_path(values: list[float]) -> str:
    points = []
    for index, value in enumerate(values):
        x = LEFT + (RIGHT - LEFT) * index / (len(values) - 1)
        y = CENTER_Y - SCALE * value
        points.append(f"{x:.2f},{y:.2f}")
    return "M " + " L ".join(points)


def main() -> None:
    phases = [2 * math.pi * index / SAMPLES for index in range(SAMPLES + 1)]
    components = [
        [math.sin(harmonic * phase) / harmonic for phase in phases]
        for harmonic in HARMONICS
    ]
    combined = [
        sum(component[index] for component in components)
        for index in range(SAMPLES + 1)
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        'role="img" aria-labelledby="title desc">',
        "<title id=\"title\">Penjumlahan harmonisa 1, 3, 5, 7, 9, dan 10</title>",
        "<desc id=\"desc\">Kurva setiap harmonisa dan resultan jumlah sin(n theta) dibagi n selama satu periode.</desc>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>',
        '<text x="450" y="28" text-anchor="middle" font-family="sans-serif" font-size="17" fill="#1f2937">'
        "x(θ) = Σ sin(nθ)/n, n = 1, 3, 5, 7, 9, 10</text>",
        f'<path d="M{LEFT} 55V325 M{LEFT} {CENTER_Y}H{RIGHT}" stroke="#64748b" stroke-width="1"/>',
        f'<path d="M{LEFT} {CENTER_Y - SCALE}H{RIGHT} M{LEFT} {CENTER_Y + SCALE}H{RIGHT}" stroke="#e2e8f0" stroke-width="1"/>',
    ]

    tick_labels = ("0", "π/2", "π", "3π/2", "2π")
    for index, label in enumerate(tick_labels):
        x = LEFT + (RIGHT - LEFT) * index / (len(tick_labels) - 1)
        parts.append(
            f'<path d="M{x:.2f} 55V325" stroke="#f1f5f9" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{x:.2f}" y="349" text-anchor="middle" font-family="sans-serif" '
            f'font-size="12" fill="#475569">{label}</text>'
        )

    for harmonic, color, values in zip(HARMONICS, COLORS, components):
        parts.append(
            f'<path d="{point_path(values)}" fill="none" stroke="{color}" '
            'stroke-width="1.4" opacity="0.75"/>'
        )
        parts.append(
            f'<text x="700" y="{53 + 17 * HARMONICS.index(harmonic)}" '
            f'font-family="sans-serif" font-size="11" fill="{color}">'
            f'harmonis {harmonic}</text>'
        )

    parts.append(
        f'<path d="{point_path(combined)}" fill="none" stroke="#111827" '
        'stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
    )
    parts.extend(
        [
            f'<text x="{LEFT - 8}" y="65" text-anchor="end" font-family="sans-serif" '
            'font-size="12" fill="#475569">x(θ)</text>',
            f'<text x="{RIGHT + 8}" y="{CENTER_Y + 4}" font-family="sans-serif" '
            'font-size="12" fill="#475569">θ</text>',
            '<path d="M700 170H730" stroke="#111827" stroke-width="3"/>',
            '<text x="738" y="174" font-family="sans-serif" font-size="11" fill="#111827">resultan</text>',
            "</svg>",
        ]
    )

    output = Path(__file__).with_name("harmonisa-1-3-5-7-9-10.svg")
    output.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Gambar tersimpan: {output.name}")


if __name__ == "__main__":
    main()
