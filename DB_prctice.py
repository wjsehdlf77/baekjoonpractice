#다이나믹 프로그래밍

#큰 문제를 작은 문제로 나누어 푸는 문제를 일컫는 말

#DP는 다음 조건을 만족해야지만 사용할 수 있다
#1. 최적 부분 구조
#   큰문제를 작은 문재로 나눌 수 있고, 작은 문제의 답을 모아 큰 문제를 해결할 수 있는 경우

#2. 중복되는 부분 문제
#   동일한 작은 문제를 반복적으로 해결해야 하는 경우


#대표적인 DB는  피보나치 수열

#메모이제이션(Memoization)
#   DP를 구현하는 방법중 한 종류
#   한 번 구한 결과를 메모리 공간에 메모해두고 --> 같은 식을 호출하면 메모한 결과를 그대로 가져오는 기법
                                                #(값을 기록해 높는다는 점에서 캐싱이라고도 한다.)

#메모이제이션하기 위한 리스트초기화
memoization = [0] * 100

#피보나치 함수를 재귀함수로 구현(Top-down DP)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    #이미 계산한 적 있으면 그대로 반환
    if memoization[x] != 0 :
        return memoization[x]

    #계산한 적이 없으면 점화식에 따라 피보나치 결과를 반환
    memoization[x] = fibo(x-1) + fibo(x-2)
    return memoization[x]

print(fibo(6))

print(memoization)


#Top-Down
    # 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
    # 탑다운(메모이제이션)방식은 '하향식'이라고도 한다
    # 점화식을 이해하기 쉬운 장점이 있다

#Bottom-Up
    # 가장 작은 문제들부터 답을 구해가며 전체 문제의 답을 찾는 방식
    # 바텀업 방식은 '상향식'이라고도 한다
    # 재귀 호출을하지 않기 때문에 시간과 메모리 사용량을 줄일 수 있는 장점이 있다

#앞서 계산된 결과를 저장하기 위한 DP테블 초기화
dp = [0] * 100
dp[1] = 1
dp[2] = 2
n = 99

#피보나치 수열 반복무능로 구현(Bottom-Up DP)
for i in range(3, n+1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])

#vs 분할 정복 (Divide and Conquer)

# DP와 분할 정복은 모두 '최적 부분 구조'를 가질 때 사용할 수 있다
# -->큰 문제를 작은 문제로 나눌 수 있고, 작은 문제의 답을 모아 큰 문제를 해결할 수 있는 경우

# DP와 분할정복의 차이점은 '부분 문제의 중복'이다.
#     DP문제에서는 각 문제들이 서로 영향을 미치며 부분 문제가 중복된다.
#     반면에 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다.


#TIP!!!!!!!

# 주어진 문제가 DP유형인지 파악하는 것이 중요!

#     먼저그리디, 시뮬레이션, 완전탑색 등의 알고리즘으로 문제를 풀 수 있는지 검토한 후 풀 수 없다고 생각이 들면 DP사용해보자

# 수열은배열이나 리스트로 표현할 수 있다고 했는데, 메모이제이션은 때에 따라서 다른 자료형, 예를 들어 딕셔너리 자료형을 이용할 수도 있다
# --> 사전 자료형은 수열처럼 연속적이지 않을 때 유용하다

# DP를 사용할 때, 일단 단순히 재귀 함수로 비효율적인 프로그램을 작성한 뒤에 (Top-Down)작은 문제에서 구한 답이 큰문제에서 그대로 사용될수 있으면
# 즉 메모이제이션을 적용할 수 있으면 코드를 개선하는 방법도 좋은 방법이다.

#     위의 피보나치 수열의 예제 코드처럼 재귀 함수를 적성한 뒤에 나중에 메모이제이션 기법을 저욕해 소스코드를 수정하는 것도 좋다!!!










