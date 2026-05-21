# 플레이어 HP와 몬스터 HP를 입력받아 턴제 전투를 시뮬레이션하세요.
player_hp = int(input())
monster_hp = int(input())
turn = 0

# 공격력 계산을 함수로 분리 → 공식 변경 시 한 곳만 수정하면 됨
def calc_player_damage(turn):
    return 15 + (turn * 7 + 3) % 11

def calc_monster_damage(turn):
    return 10 + (turn * 13 + 5) % 11

print("=== RPG 전투 시작! ===")
print(f"플레이어 HP: {player_hp} | 몬스터 HP: {monster_hp}\n")

while True:
    turn += 1
    print(f"--- {turn}턴 ---")

    # 1. 플레이어 먼저 공격
    p_damage = calc_player_damage(turn)
    monster_hp -= p_damage

    print(f"플레이어 공격! 데미지: {p_damage} | 몬스터 HP: {monster_hp}")

    # 몬스터 HP ≤ 0 이면 즉시 종료 (플레이어 승리)
    if monster_hp <= 0:
        print(f"\n플레이어 승리! ({turn}턴 만에 승리)")
        break

    # 2. 몬스터 공격
    m_damage = calc_monster_damage(turn)
    player_hp -= m_damage

    print(f"몬스터 공격! 데미지: {m_damage} | 플레이어 HP: {player_hp}\n")

    # 플레이어 HP ≤ 0 이면 즉시 종료 (몬스터 승리)
    if player_hp <= 0:
        print("몬스터 승리... (플레이어 패배)")
        break