def solution(k, score):
    # 최하점수 리스트
    answer = []
    
    # 명예의 전당에 들어갈 리스트
    st = []
    
    for i in score:
        if len(st) < k:
            st.append(i)
        else:
            if i > min(st) :
                st.remove(min(st))
                st.append(i)
        st.sort()
        answer.append(st[0])
    return answer