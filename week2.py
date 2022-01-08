#第一題
def calculate(min, max):
    sum=0
    for n in range(min,max+1):
        sum=sum+n
    print(sum)
# 請用你的程式補完這個函式的區塊
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


#第二題
def avg(data):
    sum=0
    n=-1
    while n < data["count"]-1:
        n=n+1
        sum =sum+data["employees"][n]["salary"]
    result=sum/data["count"]
    print(result)


# 請用你的程式補完這個函式的區塊
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式


#第三題
def maxProduct(nums):
    ans=float('-inf')
    N=len(nums)
    for i in range(N):
        for j in range(i+1,N):
            ans=max(ans, (nums[i])*(nums[j]))
    print(ans)
# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2


#第四題
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9