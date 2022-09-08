# 알고리즘 스터디

### 스터디 방식

- 참고 : https://cafe.naver.com/startdevelopercareer/2?boardType=L

### 목차

1. [완전탐색 & 백트래킹](#1-완전탐색-백트래킹)
2. [BFS](#2-bfs)
3. [DFS](#3-dfs)
4. [구간합](#4-구간합)
5. [다이나믹 프로그래밍](#5-다이나믹-프로그래밍)
6. [DP 트리](#6-dp-트리)
7. [이분탐색](#7-이분탐색)
8. [다익스트라](#8-다익스트라)
9. [플로이드 와샬](#9-플로이드-와샬)
10. [위상정렬](#10-위상정렬)
11. [ETC](#11-etc)

## 1. 완전탐색 백트래킹

| 문제 이름       | 문제 링크                             | 풀이                                                                                                |
| --------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 차이를 최대로   | https://www.acmicpc.net/problem/10819 | [Python](/5.%20STUDY/BruteForce/%EC%B0%A8%EC%9D%B4%EB%A5%BC%EC%B5%9C%EB%8C%80%EB%A1%9C.py)          |
| 블랙잭          | https://www.acmicpc.net/problem/2798  | [Python](/5.%20STUDY/BruteForce/%EB%B8%94%EB%9E%99%EC%9E%AD.py)                                     |
| 스타트와 링크   | https://www.acmicpc.net/problem/14889 | [Python](/5.%20STUDY/BruteForce/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80%EB%A7%81%ED%81%AC.py)          |
| 좋은 수열       | https://www.acmicpc.net/problem/2661  | [Python](/5.%20STUDY/BruteForce/%EC%A2%8B%EC%9D%80%EC%88%98%EC%97%B4.py)                            |
| 연산자 끼워넣기 | https://www.acmicpc.net/problem/14888 | [Python](/5.%20STUDY/BruteForce/%EC%97%B0%EC%82%B0%EC%9E%90%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0.py) |
| 사다리 조작\*   | https://www.acmicpc.net/problem/15684 |                                                                                                     |
| 치킨 배달\*     | https://www.acmicpc.net/problem/15686 | [Python](/5.%20STUDY/BruteForce/%EC%B9%98%ED%82%A8%EB%B0%B0%EB%8B%AC.py)                            |

## 2. BFS

| 문제 이름       | 문제 링크                             | 풀이                                                                                                                  |
| --------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 단지번호 붙이기 | https://www.acmicpc.net/problem/2667  | [Python](/5.%20STUDY/BFS/%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0.py)                          |
| 미로 탐색       | https://www.acmicpc.net/problem/2178  | [Python]()                                                                                                            |
| 연구소          | https://www.acmicpc.net/problem/14502 | [Python](/2.%20python-for-coding-test/part3/DFS%26BFS/16%EB%B2%88%20%EC%97%B0%EA%B5%AC%EC%86%8C%EC%A0%95%EB%A6%AC.py) |
| 아기 상어       | https://www.acmicpc.net/problem/16236 | [Python](/3.%20samsung/%EC%95%84%EA%B8%B0%EC%83%81%EC%96%B4.py)                                                       |
| 다리 만들기     | https://www.acmicpc.net/problem/2146  | [Python]()                                                                                                            |
| 치즈            | https://www.acmicpc.net/problem/2638  | [Python]()                                                                                                            |

## 3. DFS

| 문제 이름               | 문제 링크                             | 풀이                                                                                         |
| ----------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------- |
| 단지번호 붙이기 (dfs로) | https://www.acmicpc.net/problem/2667  | [Python](/5.%20STUDY/DFS/%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0.py) |
| 안전 영역               | https://www.acmicpc.net/problem/2468  | [Python](/5.%20STUDY/DFS/%EC%95%88%EC%A0%84%EC%98%81%EC%97%AD.py)                            |
| 적록색약                | https://www.acmicpc.net/problem/10026 | [Python](/5.%20STUDY/DFS/%EC%A0%81%EB%A1%9D%EC%83%89%EC%95%BD.py)                            |
| 알파벳                  | https://www.acmicpc.net/problem/1987  | [Python](/5.%20STUDY/DFS/%EC%95%8C%ED%8C%8C%EB%B2%B3.py)                                     |
| 양 구출작전             | https://www.acmicpc.net/problem/16437 | [Python](/5.%20STUDY/DFS/%EC%96%91%20%EA%B5%AC%EC%B6%9C%EC%9E%91%EC%A0%84.py)                |

## 4. 구간합

| 문제 이름     | 문제 링크                             | 풀이                                                                                           |
| ------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 구간합 구하기 | https://www.acmicpc.net/problem/11660 | [Python](/5.%20STUDY/CumulativeSum/%EA%B5%AC%EA%B0%84%ED%95%A9%EA%B5%AC%ED%95%98%EA%B8%B05.py) |
| 개똥벌레      | https://www.acmicpc.net/problem/3020  | [Python](/5.%20STUDY/CumulativeSum/%EA%B0%9C%EB%98%A5%EB%B2%8C%EB%A0%88.py)                    |
| 소형기관차    | https://www.acmicpc.net/problem/2616  | [Python](/5.%20STUDY/CumulativeSum/%EC%86%8C%ED%98%95%EA%B8%B0%EA%B4%80%EC%B0%A8.py)           |

## 5. 다이나믹 프로그래밍

| 문제 이름                   | 문제 링크                                                                     | 풀이                                                                                                                             |
| --------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 1로 만들기                  | https://www.acmicpc.net/problem/1463                                          | [Python](/5.%20STUDY/DP/1%EB%A1%9C%EB%A7%8C%EB%93%A4%EA%B8%B0.py)                                                                |
| 동전1                       | https://www.acmicpc.net/problem/2293                                          | [Python](/5.%20STUDY/DP/%EB%8F%99%EC%A0%841.py)                                                                                  |
| 동전2                       | https://www.acmicpc.net/problem/2294                                          | [Python](/5.%20STUDY/DP/%EB%8F%99%EC%A0%842.py)                                                                                  |
| 이친수                      | https://www.acmicpc.net/problem/2193                                          | [Python](/5.%20STUDY/DP/%EC%9D%B4%EC%B9%9C%EC%88%98.py)                                                                          |
| 이동하기                    | https://www.acmicpc.net/problem/11048                                         | [Python](/5.%20STUDY/DP/%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0.py)                                                                 |
| 평범한 배낭                 | https://www.acmicpc.net/problem/12865                                         | [Python](/5.%20STUDY/DP/%ED%8F%89%EB%B2%94%ED%95%9C%EB%B0%B0%EB%82%AD.py)                                                        |
| 호텔                        | [https://www.acmicpc.net/problem/12865](https://www.acmicpc.net/problem/1106) | [Python](/5.%20STUDY/DP/%ED%98%B8%ED%85%94.py)                                                                                   |
| LCS                         | https://www.acmicpc.net/problem/9251                                          | [Python](/5.%20STUDY/DP/lcs.py)                                                                                                  |
| 가장 긴 증가하는 부분 수열  | https://www.acmicpc.net/problem/11053                                         | [Python](/5.%20STUDY/DP/%EA%B0%80%EC%9E%A5%EA%B8%B4%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4.py)  |
| 가장 긴 증가하는 부분 수열4 | https://www.acmicpc.net/problem/14002                                         | [Python](/5.%20STUDY/DP/%EA%B0%80%EC%9E%A5%EA%B8%B4%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B44.py) |
| 욕심쟁이 판다               | https://www.acmicpc.net/problem/1937                                          | [Python](/5.%20STUDY/DP/%EC%9A%95%EC%8B%AC%EC%9F%81%EC%9D%B4%ED%8C%90%EB%8B%A4.py)                                               |
| 로봇 조종하기               | https://www.acmicpc.net/problem/2169                                          |                                                                                                                                  |
| 구간 나누기                 | https://www.acmicpc.net/problem/2228                                          | [Python](/5.%20STUDY/DP/%EA%B5%AC%EA%B0%84%EB%82%98%EB%88%84%EA%B8%B0.py)                                                        |
| 보석 줍기                   | https://www.acmicpc.net/problem/2208                                          |                                                                                                                                  |

## 6. DP 트리

| 문제 이름    | 문제 링크                             | 풀이 |
| ------------ | ------------------------------------- | ---- |
| 사회망서비스 | https://www.acmicpc.net/problem/2533  |      |
| 트리와 쿼리  | https://www.acmicpc.net/problem/15681 |      |
| 우수마을     | https://www.acmicpc.net/problem/1949  |      |
| 트리나라     | https://www.acmicpc.net/problem/12995 |      |

## 7. 이분탐색

| 문제 이름 | 문제 링크                             | 풀이 |
| --------- | ------------------------------------- | ---- |
| 숫자카드  | https://www.acmicpc.net/problem/10815 |      |
| 피자굽기  | https://www.acmicpc.net/problem/1756  |      |
| 중량제한  | https://www.acmicpc.net/problem/1949  |      |

## 8. 다익스트라

| 문제 이름        | 문제 링크                             | 풀이 |
| ---------------- | ------------------------------------- | ---- |
| 최단 경로        | https://www.acmicpc.net/problem/1753  |      |
| 특정한 최단 경로 | https://www.acmicpc.net/problem/1504  |      |
| 달빛 여우        | https://www.acmicpc.net/problem/16118 |      |

## 9. 플로이드 와샬

| 문제 이름 | 문제 링크                             | 풀이 |
| --------- | ------------------------------------- | ---- |
| 플로이드  | https://www.acmicpc.net/problem/11404 |      |
| 키 순서   | https://www.acmicpc.net/problem/2458  |      |

## 10. 위상정렬

| 문제 이름   | 문제 링크                            | 풀이 |
| ----------- | ------------------------------------ | ---- |
| 줄세우기    | https://www.acmicpc.net/problem/2252 |      |
| 게임개발    | https://www.acmicpc.net/problem/1516 |      |
| 최종순위    | https://www.acmicpc.net/problem/3665 |      |
| 장난감 조립 | https://www.acmicpc.net/problem/2637 |      |

## 11. ETC
