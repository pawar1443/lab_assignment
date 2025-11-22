# Program to calculate Simple Interest (SI) and Compound Interest (CI) for 10 customers

def calculate_si_ci():
    customers = []

    for i in range(1, 11):
        print(f"\nEnter details for Customer {i}:")
        P = float(input("Principal Amount (P): "))
        R = float(input("Rate of Interest (R%): "))
        T = float(input("Time (T in years): "))

        # Simple Interest
        SI = (P * R * T) / 100

        # Compound Interest (Annually)
        CI = P * ((1 + R/100) ** T) - P

        customers.append({
            "Customer": i,
            "Principal": P,
            "Rate": R,
            "Time": T,
            "Simple Interest": SI,
            "Compound Interest": CI
        })

    print("\n========== Interest Details of 10 Customers ==========")
    for c in customers:
        print(f"\nCustomer {c['Customer']}:")
        print(f" Principal: {c['Principal']}")
        print(f" Rate: {c['Rate']}%")
        print(f" Time: {c['Time']} years")
        print(f" Simple Interest: {c['Simple Interest']:.2f}")
        print(f" Compound Interest: {c['Compound Interest']:.2f}")


# Run the function
calculate_si_ci()