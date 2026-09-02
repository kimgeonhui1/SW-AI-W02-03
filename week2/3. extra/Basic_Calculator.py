class Solution():


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 공백 제거 
        string = s.replace(' ', '')

        stack = []
        sign = 1
        current_num = 0
        temp_num = 0 

        for x in range(len(string)):
            if string[x] == "+":
                # stack에 저장(+ 전의 숫자)
                stack.append(current_num * sign)
                
                # 다음 숫자에 1을 곱해서 더하기 (a + (b * 1))
                sign = 1

                # current_num 초기화
                current_num = 0

            elif string[x] == "-":
                
                # stack에 저장(- 전의 숫자)
                stack.append(current_num * sign)

                # 다음 숫자에 -1을 곱해야 빼기가 가능(a + (b * -1)
                sign = -1
                
                # current_num 초기화
                current_num = 0

            elif string[x] == "(":
                
                # 괄호 전 부호 저장
                stack.append(sign)

                # "(" stack에 저장
                stack.append(string[x])
                
                # 괄호 안의 부호 정의
                sign = 1
            elif string[x] == ")":
                # 괄호 종료
                print("괄호 종료")

                stack.append(current_num * sign)

                while True:
                    # 괄호() 종료 조건
                    if stack[-1] == "(":
                        # "(" stack에서 제거
                        stack.pop()

                        sign = stack.pop()

                        # () 안에서 계산한 값 stack에 append
                        stack.append(sign * temp_num)

                        # current_num, temp_num 초기화(다음 괄호를 위함)
                        current_num = 0
                        temp_num = 0

                        # while문 종료(괄호 종료)
                        break

                    else:
                        # 괄호 안의 숫자 더하기
                        temp_stack = stack.pop()
                        temp_num += temp_stack
                
                
            else:
                # 숫자인 경우
                current_num = current_num * 10 + int(string[x])
                
        # 마지막 숫자 append
        stack.append(current_num * sign)
        
        total = sum(stack)
        return total


test = Solution()
print(test.calculate("1 + 1"))