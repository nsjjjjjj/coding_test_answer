def solution(rank, attendance):
    # 출석 가능한 학생의 (등수, 번호)를 담을 빈 리스트
    candidates = []
    
    # 1. 학생 수만큼 반복하면서 출석 가능한 학생만 필터링
    for i in range(len(rank)):
        if attendance[i] == True:
            # 리스트 안에 [등수, 번호] 형태로 묶어서 추가
            candidates.append([rank[i], i])
            
    # 2. 등수(첫 번째 값)를 기준으로 오름차순 정렬
    candidates.sort()
    
    # 3. 1, 2, 3등 학생의 '번호(인덱스 1)'만 쏙쏙 뽑아내기
    # candidates은 1등의 [등수, 번호] 뭉치입니다.
    a = candidates [0][1]
    b = candidates [1][1]
    c = candidates [2][1]
    
    # 4. 정답 공식대로 계산
    return (10000 * a) + (100 * b) + c