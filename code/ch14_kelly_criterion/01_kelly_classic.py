import numpy as np


def kelly_classic(p, b):
    q = 1 - p
    f = (b * p - q) / b
    return max(f, 0)


def kelly_continuous(mu, sigma):
    return mu / (sigma ** 2)


def kelly_fractional(p, b, fraction=0.5):
    return kelly_classic(p, b) * fraction


if __name__ == '__main__':
    print("=== 经典凯利公式 ===")
    print(f"胜率60%, 赔率1:1 → f* = {kelly_classic(0.6, 1.0):.2%}")
    print(f"胜率55%, 赔率2:1 → f* = {kelly_classic(0.55, 2.0):.2%}")
    print(f"胜率30%, 赔率3:1 → f* = {kelly_classic(0.30, 3.0):.2%}")
    print(f"胜率40%, 赔率1:1 → f* = {kelly_classic(0.40, 1.0):.2%} (负值→不下注)")

    print("\n=== 连续凯利公式 ===")
    print(f"μ=10%, σ=20% → f* = {kelly_continuous(0.10, 0.20):.2%}")
    print(f"μ=8%, σ=15% → f* = {kelly_continuous(0.08, 0.15):.2%}")

    print("\n=== 分数凯利 ===")
    f_full = kelly_classic(0.6, 1.0)
    print(f"全凯利: {f_full:.2%}")
    print(f"半凯利: {kelly_fractional(0.6, 1.0, 0.5):.2%}")
    print(f"1/4凯利: {kelly_fractional(0.6, 1.0, 0.25):.2%}")
