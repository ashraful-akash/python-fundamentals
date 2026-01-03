name = "Ashraful"
age = 25
cgpa = 3.25
grade = 'A'
num = 15

print("f-STRINGS")

print(f"Name: {name}")                   # variable
print(f"Age: {age:d}")                   # integer
print(f"CGPA: {cgpa:.2f}")               # precision
print(f"Grade: {grade}")                 # char
print(f"Binary: {num:b}")                # binary
print(f"Octal: {num:o}")                 # octal
print(f"Hex: {num:X}")                   # hex

# Width, padding, alignment
print(f"Zero padded   : {num:05d}")      # 00015
print(f"Right aligned : {num:>6d}")       # right
print(f"Left aligned  : {num:<6d}")       # left
print(f"Centered      : {num:^6d}")       # center

# =====================================================
# 4. FLOAT FORMATTING DETAILS
# =====================================================
print("\n=== FLOAT FORMATTING ===")

print(f"Default      : {cgpa}")           # normal
print(f"2 decimals   : {cgpa:.2f}")       # precision
print(f"Width + prec : {cgpa:8.2f}")      # width + precision
print(f"Percentage   : {0.8575:.2%}")     # percentage

# =====================================================
# 5. STRING WIDTH & TRUNCATION
# =====================================================
print("\n=== STRING FORMATTING ===")

print(f"Right align  : '{name:>10}'")     # right aligned
print(f"Left align   : '{name:<10}'")     # left aligned
print(f"Center align : '{name:^10}'")     # centered
print(f"Truncate     : '{name:.4}'")      # first 4 chars

# =====================================================
# 6. ESCAPING BRACES
# =====================================================
print("\n=== ESCAPING BRACES ===")

print(f"Use double braces {{}} to print braces")

# =====================================================
# 7. EXPRESSIONS INSIDE f-STRINGS
# =====================================================
print("\n=== EXPRESSIONS IN f-STRINGS ===")

print(f"Age next year: {age + 1}")        # expression
print(f"CGPA rounded : {round(cgpa, 2)}") # function call