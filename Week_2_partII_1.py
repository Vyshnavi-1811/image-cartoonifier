#A
import matplotlib.pyplot as plt

years_experience = [1, 3, 5]
salaries = [300, 480, 570]

plt.scatter(years_experience, salaries)

plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')

plt.show()

#B
def compute_cost(years_experience, salaries, w, b):
    total_cost = 0
    num_samples = len(years_experience)

    for i in range(num_samples):
        x = years_experience[i]
        y = salaries[i]
        predicted_salary = w * x + b
        cost = (predicted_salary - y) ** 2
        total_cost += cost

    return total_cost / (2 * num_samples)

#C
def compute_gradient(years_experience, salaries, w, b):
    dw = 0
    db = 0
    num_samples = len(years_experience)

    for i in range(num_samples):
        x = years_experience[i]
        y = salaries[i]
        predicted_salary = w * x + b
        dw += (predicted_salary - y) * x
        db += predicted_salary - y

    dw /= num_samples
    db /= num_samples

    return dw, db