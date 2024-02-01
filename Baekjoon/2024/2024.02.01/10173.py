while True:
    s = input()
    if s == "EOI":
        break
    s = s.lower()
    num = s.count("nemo")
    if num >= 1:
        print("Found")
    else:
        print("Missing")
    