# 위 수식 그대로, 플레이어 선공 → 몬스터 사망 확인 → 몬스터 공격 → 플레이어 사망 확인
player_hp = 100
monster_hp = 80
turn = 0

print("=== RPG 전투 시작! ===")
print(f"플레이어 HP: {player_hp} | 몬스터 HP: {monster_hp}")
print()

# 플레이어나 몬스터가 이기면 종료
while True:
    # turn 계산
    turn += 1

    #  --- T턴 --- 출력
    print(f"--- {turn}턴 ---")

    # 플레이어 공격, hp계산하고 출력
    p_damage = 15 + (turn * 7 + 3) % 11
    monster_hp -= p_damage
    print(f"플레이어 공격! 데미지: {p_damage} | 몬스터 HP: {monster_hp}")

    # monster_hp가 0이하면 플레이어 승리 -> 종료
    if monster_hp <= 0:
        print(f"\n플레이어 승리! ({turn}턴 만에 승리)")
        break

    # monster_hp가 남아있으면 몬스터 공격, hp계산하고 출력
    m_damage = 10 + (turn * 11 + 5) % 11
    player_hp -= m_damage
    print(f"몬스터 공격! 데미지: {m_damage} | 플레이어 HP: {player_hp}")
    print()  # 턴 구분 빈 줄을 별도 print()로 분리하여 의도를 명확히 함

    # player_hp가 0이하면 몬스터 승리 -> 종료 (몬스터 공격 직후 확인)
    if player_hp <= 0:
        print("몬스터 승리... (플레이어 패배)")
        break