import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# 겹치는 면적 계산 함수
def overlap_area(d, r1, r2):
    if d >= r1 + r2:
        return 0
    if d <= abs(r1 - r2):
        return np.pi * min(r1, r2)**2

    # 겹치는 면적 계산 공식
    part1 = r1**2 * np.arccos((d**2 + r1**2 - r2**2) / (2 * d * r1))
    part2 = r2**2 * np.arccos((d**2 + r2**2 - r1**2) / (2 * d * r2))
    part3 = 0.5 * np.sqrt((-d + r1 + r2)*(d + r1 - r2)*(d - r1 + r2)*(d + r1 + r2))
    return part1 + part2 - part3

# ✅ 사용자 입력
r1 = float(input("첫 번째 원의 반지름을 입력하세요: "))
r2 = float(input("두 번째 원의 반지름을 입력하세요: "))
ratio = float(input("첫 번째 원의 면적 중 몇 퍼센트를 겹치게 할까요? (예: 50 입력 시 50%): "))

# 계산
A1 = np.pi * r1**2
target_area = (ratio / 100) * A1
max_overlap = np.pi * min(r1, r2)**2

if target_area > max_overlap:
    print("❌ 목표 겹치는 면적이 최대 겹치는 면적보다 큽니다. 계산 불가능.")
else:
    d_values = np.linspace(0, r1 + r2, 500)
    areas = [overlap_area(d, r1, r2) for d in d_values]
    d_optimal = d_values[np.argmin(np.abs(np.array(areas) - target_area))]

    print(f"✅ 중심 거리 d = {d_optimal:.2f} 에서 겹치는 면적이 목표치와 가장 가까움")

    # 시각화
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-r1-1, r1+r2+1)
    ax.set_ylim(-max(r1, r2)-1, max(r1, r2)+1)

    center1 = (0, 0)
    center2 = (d_optimal, 0)

    def plot_circle(ax, center, radius, color):
        circle = plt.Circle(center, radius, color=color, alpha=0.5)
        ax.add_patch(circle)

    plot_circle(ax, center1, r1, 'magenta')
    plot_circle(ax, center2, r2, 'yellow')

    plt.title(f"Center-to-center distance d = {d_optimal:.2f},\nOverlapping area ≈ {ratio:.1f}% of Circle 1's area")
    plt.grid(True)
    plt.show()
