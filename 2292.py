n = int(input())
pipelineNum = 1
cnt = 1
while n > pipelineNum:
    pipelineNum += 6 * cnt
    cnt += 1
print(cnt)
