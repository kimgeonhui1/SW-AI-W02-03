class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 선수과목이 없을 경우 True
        if not prerequisites:
            return True

        # 각 과목(b)을 선수과목으로 요구하는 후속 과목(a) 목록 저장
        pre_subject = {i: [] for i in range(numCourses)}

        # 진입 차수(in-degree) 배열 초기화
        in_degree = [0] * numCourses

        # 그래프 간선 연결 및 선수과목 개수 세기
        for a, b in prerequisites:
            pre_subject[b].append(a)  # b를 끝내면 수강할 수 있는 목록에 a 추가
            in_degree[a] += 1  # a 과목의 필요 선수과목 개수 1 증가

        # 선수과목이 필요 없는(진입 차수가 0인) 과목들을 큐에 담음
        get_one = [i for i in range(numCourses) if in_degree[i] == 0]

        # 수강을 완료 리스트
        visited = []

        while get_one:
            # 큐에서 들을 수 있는 과목 하나를 꺼냄
            current = get_one.pop(0)

            # 해당 과목 수강 완료 처리
            visited.append(current)

            # 방금 들은 과목(current)을 선수과목으로 요구하던 후속 과목들을 확인
            for neighbor in pre_subject[current]:
                # 선수과목 하나를 이수했으므로 요구 조건 개수를 1 줄임
                in_degree[neighbor] -= 1

                # 남은 선수과목이 0개가 되었다면 이제 수강할 수 있으므로 큐에 추가
                if in_degree[neighbor] == 0:
                    get_one.append(neighbor)

        # 이수한 과목 수가 전체 과목 수와 같다면 모든 과목 수강 가능(True)
        return len(visited) == numCourses


# 테스트 케이스
a = Solution()
print(a.canFinish(3, [[1, 0], [1, 2], [0, 1]]))  
print(a.canFinish(3, [[1, 0], [2, 1]]))  