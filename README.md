# 📊 Numerical Methods Algorithms in Python

This repository contains Python implementations of fundamental numerical methods commonly used in engineering and scientific computations.

---

## 📌 Algorithms Included

### 🔹 Root Finding Methods

* Bisection Method
* Regula Falsi Method
* Newton-Raphson Method

### 🔹 Linear System Solvers

* Gauss Elimination
* Jacobi Method
* Gauss-Seidel Method

### 🔹 Interpolation Techniques

* Newton Forward Interpolation
* Newton Backward Interpolation

---

## ⚙️ Requirements

* Python 3.x
* NumPy (for matrix operations)

Install dependencies using:

```bash
pip install numpy
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/Numerical-Methods.git
cd Numerical-Methods
```

Run any file:

```bash
python bisection.py
```

---

## 🧠 Example Usage

```python
# Example function
f = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1

print("Bisection:", bisection(f, 1, 2))
print("Regula Falsi:", regula_falsi(f, 1, 2))
print("Newton Raphson:", newton_raphson(f, df, 1.5))
```

---

## 📂 Project Structure

```
Numerical-Methods/
│── bisection.py
│── regula_falsi.py
│── newton_raphson.py
│── gauss_elimination.py
│── jacobi.py
│── gauss_seidel.py
│── interpolation.py
│── README.md
```

---

## 📖 Description of Methods

### ✔️ Bisection Method

A bracketing method that repeatedly divides an interval to locate the root.

### ✔️ Regula Falsi Method

An improved bracketing method using linear interpolation.

### ✔️ Newton-Raphson Method

A fast iterative method using derivatives to approximate roots.

### ✔️ Gauss Elimination

A direct method to solve linear equations using row operations.

### ✔️ Jacobi Method

An iterative method for solving linear systems.

### ✔️ Gauss-Seidel Method

An improved iterative method using updated values immediately.

### ✔️ Newton Interpolation

Used to estimate values between known data points.

---

## 🎯 Applications

* Engineering problem solving
* Scientific computing
* Data analysis
* Numerical simulations

---

## 👨‍💻 Author

**Your Name**
B.Tech Computer Science Student

---

## ⭐ Contribute

Feel free to fork this repository and improve it!

---

## 📜 License

This project is open-source and free to use.
