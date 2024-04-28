profit = list(map(int, input("Enter profits separated by space: ").split()))
jobs = input("Enter job names separated by space: ").split()
deadline = list(map(int, input("Enter deadlines separated by space: ").split()))

max_deadline = max(deadline)
profitNJobs = list(zip(profit, jobs, deadline))
profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

slot = [0] * (max_deadline + 1)
total_profit = 0
scheduled_jobs = []

for _ in range(max_deadline + 1):
    scheduled_jobs.append('null')

for i in range(len(jobs)):
    job = profitNJobs[i]
    # Check if slot is occupied
    for j in range(job[2], 0, -1):
        if j <= max_deadline and slot[j] == 0:
            scheduled_jobs[j] = job[1]
            total_profit += job[0]
            slot[j] = 1
            break

print("Jobs scheduled:", scheduled_jobs[1:])
print("Total profit:", total_profit)
