total_books = int(input("Enter number of books: "))
pages = []

for i in range(total_books):
    p = int(input("Enter pages: "))
    pages.append(p)

students = int(input("Enter number of students: "))

if students > total_books:
    print("Allocation not possible")
else:
    low = max(pages)
    high = sum(pages)

    while low < high:
        limit = (low + high) // 2

        student_count = 1
        current_pages = 0

        for book in pages:
            if current_pages + book > limit:
                student_count += 1
                current_pages = book
            else:
                current_pages += book

        if student_count <= students:
            high = limit
        else:
            low = limit + 1

    print("Minimum maximum pages:", low)